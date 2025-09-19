# breach_check.py
"""
Breach check module:
- Uses Have I Been Pwned API (HIBP).
- Falls back to GitHub common list.
- Falls back to local file common_passwords.txt.
"""

import hashlib
import requests
import time
from typing import Optional, Set, Tuple

_HIBP_URL = "https://api.pwnedpasswords.com/range/{}"
_DEFAULT_GITHUB_RAW = (
    "https://raw.githubusercontent.com/"
    "danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
)

_CACHE_TTL = 60 * 60  # 1 hour
_prefix_cache = {}    # prefix -> (timestamp, suffix_dict)


def _fetch_hibp_prefix(prefix: str, timeout: float = 10.0) -> dict:
    """Fetch suffix->count mapping for a SHA1 prefix from HIBP."""
    now = time.time()
    entry = _prefix_cache.get(prefix)
    if entry and now - entry[0] < _CACHE_TTL:
        return entry[1]

    try:
        r = requests.get(_HIBP_URL.format(prefix),
                         timeout=timeout,
                         headers={"User-Agent": "PasswordChecker/1.0"})
        r.raise_for_status()
        data = {}
        for line in r.text.splitlines():
            if ":" in line:
                suf, cnt = line.split(":", 1)
                data[suf.strip().upper()] = int(cnt.strip())
        _prefix_cache[prefix] = (now, data)
        return data
    except requests.RequestException:
        return {}


def is_pwned_hibp(password: str) -> Optional[int]:
    """Check password in HIBP. Return count or None on error."""
    if not password:
        return 0
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    data = _fetch_hibp_prefix(prefix)
    if not data and prefix not in _prefix_cache:
        return None
    return data.get(suffix, 0)


def fetch_common_from_github(url: str, timeout: float = 15.0) -> Set[str]:
    """Fetch common password list from GitHub raw."""
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return {line.strip().lower() for line in r.text.splitlines() if line.strip()}
    except requests.RequestException:
        return set()


def load_common_local(path: str = "common_passwords.txt") -> Set[str]:
    """Load local file one password per line."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            return {line.strip().lower() for line in fh if line.strip()}
    except FileNotFoundError:
        return set()


def is_password_breached(password: str,
                         try_github_fallback: bool = True,
                         github_url: Optional[str] = None,
                         local_path: Optional[str] = None) -> Tuple[bool, Optional[int], str]:
    """
    Check password against breaches.
    Returns (breached, times_seen, source).
    """
    if not password:
        return False, 0, "none"

    # 1. HIBP
    times = is_pwned_hibp(password)
    if times is not None:
        return (times > 0, times, "hibp")

    # 2. GitHub fallback
    if try_github_fallback:
        gh_url = github_url if github_url else _DEFAULT_GITHUB_RAW
        gh_set = fetch_common_from_github(gh_url)
        if gh_set:
            return (password.lower() in gh_set, None, "github")

        # 3. Local fallback
        lp = local_path if local_path else "common_passwords.txt"
        local_set = load_common_local(lp)
        if local_set:
            return (password.lower() in local_set, None, "local")

    return False, None, "none"

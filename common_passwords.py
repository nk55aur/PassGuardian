# common_passwords.py
import requests
from typing import Set

def fetch_common_passwords(url: str) -> Set[str]:
    """
    Fetch a list of common passwords from a GitHub raw link.
    Returns a set of lowercase common passwords.
    Falls back to a small default list if the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {line.strip().lower() for line in response.text.splitlines() if line.strip()}
        else:
            print("⚠️ Could not fetch passwords list, using fallback.")
            return {"password", "123456", "qwerty"}
    except Exception as e:
        print(f"⚠️ Error fetching list: {e}")
        return {"password", "123456", "qwerty"}


# 🔥 Insert your GitHub raw link here
GITHUB_PASSWORD_LIST = (
    "https://raw.githubusercontent.com/danielmiessler/"
    "SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
)

# Load common passwords at module import
COMMON_PASSWORDS: Set[str] = fetch_common_passwords(GITHUB_PASSWORD_LIST)

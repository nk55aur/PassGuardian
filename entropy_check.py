# entropy_check.py
"""
Entropy and crack-time estimation.
"""

import math


def password_entropy(password: str) -> float:
    """Estimate Shannon entropy in bits."""
    if not password:
        return 0.0

    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32  # approx special chars

    if charset == 0:
        return 0.0
    return len(password) * math.log2(charset)


def crack_time_seconds(entropy_bits: float, guesses_per_second: float = 1e9) -> float:
    """Estimate average crack time in seconds (at 1B guesses/sec)."""
    keyspace = 2 ** entropy_bits
    avg_guesses = keyspace / 2
    return avg_guesses / guesses_per_second


def crack_time_display(seconds: float) -> str:
    """Convert seconds into human-readable string."""
    intervals = [
        ("centuries", 60 * 60 * 24 * 365 * 100),
        ("years", 60 * 60 * 24 * 365),
        ("days", 60 * 60 * 24),
        ("hours", 60 * 60),
        ("minutes", 60),
        ("seconds", 1),
    ]
    for name, secs in intervals:
        if seconds >= secs:
            return f"{seconds / secs:.2f} {name}"
    return "instant"

# password_strength_main.py
"""
Main password strength checker script.
Now includes:
- Rule-based scoring
- Breach check
- Entropy & crack-time
- Password generator (from user-provided base password)
"""

import re
from common_passwords import COMMON_PASSWORDS
from breach_check import is_password_breached
from entropy_check import password_entropy, crack_time_seconds, crack_time_display
from password_generator import strengthen_password   # <--- import here


def password_strength(password: str) -> (str, list): # type: ignore
    suggestions = []
    score = 0

    # --- Basic length scoring ---
    if len(password) >= 10:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        suggestions.append("Use at least 8 characters (12+ recommended).")

    # --- Character diversity ---
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add digits.")
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters (!,@,#, etc).")

    # --- Simple patterns ---
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeated characters like 'aaa' or '111'.")
    if re.search(r"(0123|1234|2345|3456|4567|5678|6789)", password):
        suggestions.append("Avoid sequential numbers like '1234'.")
        
     # Common password check
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Your password is too common. Choose something unique!")
        
    # --- Breach check ---
    breached, times_seen, source = is_password_breached(password,
                                                        local_path="common_passwords.txt")
    if breached:
        if source == "hibp":
            suggestions.append(f"⚠️ Found in HIBP {times_seen} times. Do NOT use this password!")
        elif source == "github":
            suggestions.append("⚠️ Found in GitHub common list. Do NOT use this password!")
        elif source == "local":
            suggestions.append("⚠️ Found in local common list. Do NOT use this password!")

    # --- Entropy & crack-time ---
    entropy = password_entropy(password)
    crack_seconds = crack_time_seconds(entropy)
    crack_readable = crack_time_display(crack_seconds)
    suggestions.append(f"Entropy: {entropy:.2f} bits")
    suggestions.append(f"Estimated crack time: {crack_readable} (at 1B guesses/sec)")

    # --- Final label ---
    if breached:
        label = "❌ BREACHED — do NOT use"
    elif entropy >= 60 and score >= 6:
        label = "✅ Strong"
    elif entropy >= 40 and score >= 4:
        label = "⚠️ Moderate"
    else:
        label = "❌ Weak"

    return label, suggestions


def main():
    print("🔐 Password Strength Checker")
    print("Options: check, gen, exit")
    while True:
        choice = input("\nChoose an option (check/gen/exit): ").strip().lower()
        if choice == "exit":
            break
        elif choice == "check":
            pw = input("Enter password to check: ").strip()
            label, tips = password_strength(pw)
            print("\nResult:", label)
            for t in tips:
                print(" -", t)
        elif choice == "gen":
            base_pw = input("Enter your base password: ").strip()
            new_pw = strengthen_password(base_pw)
            print("\nGenerated stronger password:", new_pw)
            label, tips = password_strength(new_pw)
            print("Evaluation:", label)
            for t in tips:
                print(" -", t)
        else:
            print("Unknown option. Use 'check', 'gen', or 'exit'.")


if __name__ == "__main__":
    main()

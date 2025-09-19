
# password_generator.py
import secrets
import string


def strengthen_password(user_password: str, add_length: int = 16) -> str:
    """
    Take a user-provided password and generate a stronger variant.
    - Keeps original structure.
    - Adds random characters (digits/symbols) at the end for extra strength.
    - Ensures at least some uppercase/lowercase/digits/symbols are present.
    """

    if not user_password:
        raise ValueError("Password cannot be empty")

    new_password = user_password

    # Ensure at least one uppercase
    if not any(c.isupper() for c in new_password):
        new_password += user_password[0].upper()

    # Ensure at least one digit
    if not any(c.isdigit() for c in new_password):
        new_password += str(secrets.randbelow(8))

    # Ensure at least one symbol
    symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
    if not any(c in symbols for c in new_password):
        new_password += secrets.choice(symbols)

    # Add extra random characters for length increase
    pool = string.ascii_letters + string.digits + symbols
    for _ in range(add_length):
        new_password += secrets.choice(pool)

    return new_password


# quick test
'''if __name__ == "__main__":
    user_pw = input("Enter your base password: ").strip()
    print("Strengthened password:", strengthen_password(user_pw))''' 
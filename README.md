PassGuardian 🔐

A Python-based Password Strength Checker and Generator that evaluates passwords for security, checks against breach datasets, calculates entropy & crack-time, and generates stronger alternatives.

🚀 Features

✅ Rule-based scoring (length, diversity, repetition)

✅ Breach detection (local list + GitHub common passwords + optional HIBP API)

✅ Entropy calculation & crack-time estimation

✅ Secure password generator from a base word

✅ Actionable feedback with improvement tips

📂 Project Structure

PassGuardian/

│── password_strength_main.py   # Main CLI program

│── breach_check.py             # Breach lookup logic

│── entropy_check.py            # Entropy & crack-time

│── password_generator.py       # Strong password generator

│── common_passwords.py         # Loads common-password datasets

│── common_passwords.txt        # Github list link

│── requirements.txt            # Dependencies

│── README.md                   # Overview

│── PROJECT_DOCUMENTATION.md    # Technical details

⚡ Installation

Clone this repository and install dependencies:

bash:
git clone https://github.com/nk55aur/PassGuardian.git

cd PassGuardian

pip install -r requirements.txt
 
🛠️ Usage

Run the main program:

python password_strength_main.py

Choose one of the options:

check → Evaluate an existing password

gen → Generate a stronger password from a base word

exit → Quit

🧪 Example

Password Check:

Choose an option (check/gen/exit): check

Enter password to check: Password123!

Result: ⚠️ Moderate

 - Add special characters
   
 - Avoid common patterns
   
 - Entropy: 45.21 bits
   
 - Estimated crack time: 2 hours

Password Generator:

Choose an option (check/gen/exit): gen

Enter your base password: harry

Generated stronger password: harry7!XpQa

Evaluation: ✅ Strong

 - Entropy: 71.65 bits
   
 - Estimated crack time: 800 years

📦 Requirements:

Python 3.9+

requests (install via pip install -r requirements.txt)

🛤️ Roadmap

GUI version (Tkinter / Flask)

Integration with password managers

Multi-language support

Real-time API checks for leaked credentials

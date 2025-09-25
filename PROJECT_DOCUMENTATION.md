📄 Project Documentation – PassGuardian

📌 Project Overview

PassGuardian is a Python-based password security tool designed to evaluate and improve password strength.
It helps users create stronger, safer passwords by combining rule-based analysis, breach detection, entropy calculation, and a secure password generator.
This project addresses real-world cybersecurity challenges where weak or reused passwords are the leading cause of data breaches.

🚀 Key Features

Rule-Based Scoring → Evaluates length, character variety, and repetition.

Breach Detection → Compares passwords against common/breached password lists.

Entropy & Crack-Time Estimation → Provides insights into password resilience against brute force.

Secure Password Generator → Creates strong alternatives from a user’s base word.

Actionable Suggestions → Guides users to improve weak or moderate passwords.

📂 Project Structure

PassGuardian/

│── password_strength_main.py   # Main CLI program

│── breach_check.py             # Breach lookup logic

│── entropy_check.py            # Entropy & crack-time calculations

│── password_generator.py       # Strong password generator

│── common_passwords.py         # Loads common-password datasets

│── common_passwords.txt        # Github list link

│── requirements.txt            # Dependencies

│── README.md                   # Overview

│── PROJECT_DOCUMENTATION.md    # Technical documentation



🛠️ Technology Stack:

Python 3.9+ → Core programming language

requests → Fetch breached/common password lists from GitHub or APIs

re (Regex) → Pattern matching for rule-based validation

secrets → Secure random generation for password strengthening

math → Entropy and crack-time calculations

🧪 Example Usage

🔍 Password Check:

Choose an option (check/gen/exit): check

Enter password to check: Password123!

Result: ⚠️ Moderate

 - Add special characters
   
 - Avoid common patterns
   
 - Entropy: 45.21 bits
   
 - Estimated crack time: 2 hours

🔑 Password Generator:

Choose an option (check/gen/exit): gen

Enter your base password: sudhir

Generated stronger password: sudhir7!XpQa

Evaluation: ✅ Strong

 - Entropy: 71.65 bits
   
 - Estimated crack time: 800 years

⚡ Installation

Clone the repository:

git clone https://github.com/nk55aur/PassGuardian.git

cd PassGuardian

Install dependencies:

pip install -r requirements.txt

Run the program:

python password_strength_main.py

🛤️ Future Enhancements

GUI version (Tkinter or Flask web app)

Integration with popular password managers

Multi-language support for wider adoption

Real-time API checks with HaveIBeenPwned (HIBP)

Machine learning–based strength prediction



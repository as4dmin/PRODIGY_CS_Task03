

```markdown
# Password Complexity Checker

A simple Python script to assess the strength of a password based on multiple criteria. This tool evaluates passwords and provides feedback to improve their strength, helping users create secure and reliable passwords.

---

## Features

- **Length Check**:
  - Scores passwords based on their length:
    - Excellent: 12 or more characters
    - Moderate: 8–11 characters
    - Weak: Less than 8 characters
- **Uppercase and Lowercase Letters**:
  - Ensures the password includes at least one uppercase and one lowercase letter.
- **Number Check**:
  - Validates the inclusion of at least one numeric digit.
- **Special Character Check**:
  - Encourages the use of special characters (e.g., `!`, `@`, `#`, etc.).
- **Feedback**:
  - Provides specific feedback to users on how to improve their passwords.
- **Strength Categories**:
  - Classifies passwords as:
    - `Very Weak`
    - `Weak`
    - `Strong`
    - `Very Strong`

---

## How It Works

The script evaluates the password against five criteria:
1. Length of the password.
2. Presence of uppercase letters.
3. Presence of lowercase letters.
4. Inclusion of numeric characters.
5. Usage of special characters.

Each satisfied criterion adds to the overall score (maximum score: 6). Based on the score, the password is categorized into one of the four strength levels.

---

## Getting Started

### Prerequisites

Ensure Python is installed on your system (Python 3.6 or higher is recommended).

### Usage

1. Clone the repository or download the script file.
2. Run the script using a Python interpreter:
   ```bash
   python password_checker.py
   ```
3. Enter your password when prompted.
4. View the strength assessment and feedback.

---

## Example Output

```plaintext
*** PASSWORD COMPLEXITY CHECKER ***

Enter your password to assess: MyPass@123

Password strength assessment
Score: 6/6
Category: Very strong
Feedback: 
- Password length is excellent.
```

---

## Feedback Categories

- **Very Strong (Score: 6/6)**: Your password is highly secure.
- **Strong (Score: 4-5/6)**: Your password is fairly secure but could use slight improvements.
- **Weak (Score: 2-3/6)**: Your password is vulnerable and needs significant improvement.
- **Very Weak (Score: 0-1/6)**: Your password is insecure and should not be used.

---

## Contributing

Contributions to enhance the script are welcome! Feel free to submit a pull request or open an issue with suggestions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

Created by **Md Asadullah Abbasi**.
```

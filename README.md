# User Registration System

A lightweight Python module for validating user registration fields (Name, Email, Mobile, and Password) using regular expressions, built following a test-driven development (TDD) approach with `pytest`.

---

## 🚀 Features & Validation Rules

* **Name Validation:** Requires first and last names to start with a capital letter and have a minimum of 3 characters.
* **Email Validation:** Supports standard formats (e.g., `abc@bl.co`, `abc.xyz@bl.co.in`) with strict positioning for `@` and `.`.
* **Mobile Number Validation:** Validates the format `91 9876543210` (Country code + space + 10-digit number).
* **Password Validation:** Enforces secure passwords with a minimum of 8 characters, at least 1 uppercase letter, at least 1 number, and exactly 1 special character.

---

## 📁 Project Structure

```text
User_Registration_Python/
├── src/
│   ├── __init__.py
│   └── user.py          # Field validation logic
├── tests/
│   ├── __init__.py
│   └── test_user.py     # Comprehensive pytest suites
├── .gitattributes
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites
Make sure you have Python 3.x installed.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/User_Registration_Python.git
cd User_Registration_Python
```

### 2. Install dependencies
```bash
pip install pytest
```

### 3. Run the test suite
To run all validation test cases, simply execute:

```bash
pytest
```

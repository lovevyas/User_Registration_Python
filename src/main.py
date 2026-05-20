import re


# ---------------- VALIDATORS ---------------- #

def validate_name(name: str) -> bool:
    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.fullmatch(pattern, name))


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-z]{2,}(\.[a-z]{2,})?$'
    return bool(re.fullmatch(pattern, email))


def validate_mobile(number: str) -> bool:
    pattern = r'^[0-9]{2} [0-9]{10}$'
    return bool(re.fullmatch(pattern, number))

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    return True 

# ---------------- INPUT HANDLING ---------------- #

def get_input(field, validator, error):
    while True:
        value = input(f"Enter {field}: ")
        if validator(value):
            return value
        print(f"Error: {error}")


def get_name(field):
    return get_input(
        field,
        validate_name,
        "Should start with capital and have minimum 3 characters"
    )


def get_email():
    return get_input(
        "Email",
        validate_email,
        "Invalid email format (e.g., abc.xyz@bl.co.in)"
    )


def get_mobile():
    return get_input(
        "Mobile Number",
        validate_mobile,
        "Format should be: 91 9876543210"
    )

def get_password():
    return get_input("Password",
                     validate_password,
                     "Password must be at least 8 chars, contain 1 uppercase and 1 number")

# ---------------- DOMAIN MODEL ---------------- #

class User:
    def __init__(self, first_name: str, last_name: str, email: str, mobile: str, password: str):
        if not validate_name(first_name):
            raise ValueError("Invalid first name")
        if not validate_name(last_name):
            raise ValueError("Invalid last name")
        if not validate_email(email):
            raise ValueError("Invalid email")
        if not validate_mobile(mobile):
            raise ValueError("Invalid mobile number")
        if not validate_password(password):
            raise ValueError("Invalid password")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.password = password

    def __str__(self):
        return (
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Email: {self.email}\n"
            f"Mobile: {self.mobile}"
        )


# ---------------- MAIN ---------------- #

def main():
    first_name = get_name("First Name")
    last_name = get_name("Last Name")
    email = get_email()
    mobile = get_mobile()
    password = get_password()

    user = User(first_name, last_name, email, mobile, password)
    print("\nUser Registered Successfully:\n")
    print(user)


if __name__ == "__main__":
    main()
import re


def validate_email(email: str) -> bool:
    LOCAL_PART = r'[a-zA-Z0-9]+([._+-]?[a-zA-Z0-9]+)*'
    DOMAIN = r'[a-zA-Z0-9]+'
    TLD = r'[a-z]{2,}'

    pattern = rf'^{LOCAL_PART}@{DOMAIN}\.{TLD}(\.{TLD})?$'
    return bool(re.fullmatch(pattern, email))


def get_input(field, validator, error):
    while True:
        value = input(f"Enter {field}: ")
        if validator(value):
            return value
        print(f"Error: {error}")


def validate_name(name: str) -> bool:
    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.fullmatch(pattern, name))


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


class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        if not validate_name(first_name):
            raise ValueError("Invalid first name")
        if not validate_name(last_name):
            raise ValueError("Invalid last name")
        if not validate_email(email):
            raise ValueError("Invalid email")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return (
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Email: {self.email}"
        )


def main():
    first_name = get_name("First Name")
    last_name = get_name("Last Name")
    email = get_email()

    user = User(first_name, last_name, email)
    print(user)


if __name__ == "__main__":
    main()
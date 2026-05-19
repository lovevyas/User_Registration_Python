import re


def validate_first_name(name: str) -> bool:
    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.fullmatch(pattern, name))


class User:
    def __init__(self, first_name: str):
        if not validate_first_name(first_name):
            raise ValueError("Invalid first name")
        self.first_name = first_name

    def __str__(self):
        return f"First Name: {self.first_name}"


def get_input(field, validator, error):
    while True:
        value = input(f"Enter {field}: ")
        if validator(value):
            return value
        print(f"Error: {error}")


def main():
    first_name = get_input(
        "First Name",
        validate_first_name,
        "Should start with capital and have minimum 3 characters",
    )

    user = User(first_name)
    print(user)


if __name__ == "__main__":
    main()
import re


def validate_name(name: str) -> bool:
    pattern = r'^[A-Z][a-z]{2,}$'
    return bool(re.fullmatch(pattern, name))


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


class User:
    def __init__(self, first_name: str, last_name: str):
        if not validate_name(first_name):
            raise ValueError("Invalid first name")
        if not validate_name(last_name):
            raise ValueError("Invalid last name")

        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"


def main():
    first_name = get_name("First Name")
    last_name = get_name("Last Name")

    user = User(first_name, last_name)
    print(user)


if __name__ == "__main__":
    main()
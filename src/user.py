import re


# ---------------- VALIDATORS ---------------- #
import re

class UserValidator:

    @staticmethod
    def validate_name(name: str) -> bool:
        return bool(re.fullmatch(r'^[A-Z][a-z]{2,}$', name))

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(re.fullmatch(
            r'^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-z]{2,}(\.[a-z]{2,})?$',
            email
        ))

    @staticmethod
    def validate_mobile(number: str) -> bool:
        return bool(re.fullmatch(r'^[0-9]{2} [0-9]{10}$', number))

    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if len(re.findall(r'[@#$%^&+=]', password)) != 1:
            return False
        return True
# ---------------- INPUT HANDLING ---------------- #
class UserService:
    
    @staticmethod
    def create_user(first_name, last_name, email, mobile, password):

        if not UserValidator.validate_name(first_name):
            raise ValueError("Invalid first name")

        if not UserValidator.validate_name(last_name):
            raise ValueError("Invalid last name")

        if not UserValidator.validate_email(email):
            raise ValueError("Invalid email")

        if not UserValidator.validate_mobile(mobile):
            raise ValueError("Invalid mobile")

        if not UserValidator.validate_password(password):
            raise ValueError("Invalid password")

        return User(first_name, last_name, email, mobile, password)
# ---------------- DOMAIN MODEL ---------------- #

class User:
    def __init__(self, first_name, last_name, email, mobile, password):
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
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")
    password = input("Enter Password: ")

    try:
        user = UserService.create_user(
            first_name, last_name, email, mobile, password
        )
        print("\nUser Registered Successfully:\n")
        print(user)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
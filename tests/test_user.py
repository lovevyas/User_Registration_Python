from src.user import validate_email


# -------- VALID CASES -------- #
def test_valid_emails():
    valid_emails = [
        "abc@bl.co",
        "abc.xyz@bl.co",
        "abc@bl.co.in",
        "abc.xyz@bl.co.in"
    ]

    for email in valid_emails:
        assert validate_email(email) == True


# -------- INVALID CASES -------- #
def test_invalid_emails():
    invalid_emails = [
        "abc",
        "abc@",
        "@bl.co",
        "abc@.co",
        "abc@bl",
        "abc..xyz@bl.co"
    ]

    for email in invalid_emails:
        assert validate_email(email) == False
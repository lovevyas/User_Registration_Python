from src.user import UserValidator
# -------- NAME TESTS -------- #

def test_valid_names():
    assert UserValidator.validate_name("John")
    assert UserValidator.validate_name("Alice")
    assert UserValidator.validate_name("Mark")


def test_invalid_names():
    assert not UserValidator.validate_name("jo")   
    assert not UserValidator.validate_name("123")
    assert not UserValidator.validate_name("john")    
    assert not UserValidator.validate_name("J")       
    assert not UserValidator.validate_name("J1")      
    assert not UserValidator.validate_name("J@hn")    


# -------- EMAIL TESTS -------- #

def test_valid_emails():
    assert UserValidator.validate_email("abc@bl.co")
    assert UserValidator.validate_email("abc.xyz@bl.co")
    assert UserValidator.validate_email("abc@bl.co.in")
    assert UserValidator.validate_email("abc.xyz@bl.co.in")


def test_invalid_emails():
    assert not UserValidator.validate_email("abc")
    assert not UserValidator.validate_email("abc@")
    assert not UserValidator.validate_email("@bl.co")
    assert not UserValidator.validate_email("abc@.co")
    assert not UserValidator.validate_email("abc@bl")
    assert not UserValidator.validate_email("abc..xyz@bl.co")


# -------- MOBILE TESTS -------- #

def test_valid_mobile():
    assert UserValidator.validate_mobile("91 9876543210")
    assert UserValidator.validate_mobile("12 1234567890")


def test_invalid_mobile():
    assert not UserValidator.validate_mobile("919876543210")   
    assert not UserValidator.validate_mobile("91 987654321")   
    assert not UserValidator.validate_mobile("91 98765432101") 
    assert not UserValidator.validate_mobile("9a 9876543210")  
    assert not UserValidator.validate_mobile("91-9876543210")  


# -------- PASSWORD TESTS -------- #

def test_valid_password():
    assert UserValidator.validate_password("Abcdef1@")
    assert UserValidator.validate_password("Password1#")
    assert UserValidator.validate_password("Hello123$")


def test_invalid_password():
    assert not UserValidator.validate_password("abcdefg")      
    assert not UserValidator.validate_password("abcdefgh")     
    assert not UserValidator.validate_password("ABCDEFGH")     
    assert not UserValidator.validate_password("Abcdefgh")     
    assert not UserValidator.validate_password("Abcdefg1")     
    assert not UserValidator.validate_password("Abcdef1@@")    
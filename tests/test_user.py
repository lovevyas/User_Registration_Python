from src.user import (
    validate_name,
    validate_email,
    validate_mobile,
    validate_password
)

# -------- NAME TESTS -------- #

def test_valid_names():
    assert validate_name("John")
    assert validate_name("Alice")
    assert validate_name("Mark")


def test_invalid_names():
    assert not validate_name("jo")   
    assert not validate_name("123")
    assert not validate_name("john")    
    assert not validate_name("J")       
    assert not validate_name("J1")      
    assert not validate_name("J@hn")    


# -------- EMAIL TESTS -------- #

def test_valid_emails():
    assert validate_email("abc@bl.co")
    assert validate_email("abc.xyz@bl.co")
    assert validate_email("abc@bl.co.in")
    assert validate_email("abc.xyz@bl.co.in")


def test_invalid_emails():
    assert not validate_email("abc")
    assert not validate_email("abc@")
    assert not validate_email("@bl.co")
    assert not validate_email("abc@.co")
    assert not validate_email("abc@bl")
    assert not validate_email("abc..xyz@bl.co")


# -------- MOBILE TESTS -------- #

def test_valid_mobile():
    assert validate_mobile("91 9876543210")
    assert validate_mobile("12 1234567890")


def test_invalid_mobile():
    assert not validate_mobile("919876543210")   
    assert not validate_mobile("91 987654321")   
    assert not validate_mobile("91 98765432101") 
    assert not validate_mobile("9a 9876543210")  
    assert not validate_mobile("91-9876543210")  


# -------- PASSWORD TESTS -------- #

def test_valid_password():
    assert validate_password("Abcdef1@")
    assert validate_password("Password1#")
    assert validate_password("Hello123$")


def test_invalid_password():
    assert not validate_password("abcdefg")      
    assert not validate_password("abcdefgh")     
    assert not validate_password("ABCDEFGH")     
    assert not validate_password("Abcdefgh")     
    assert not validate_password("Abcdefg1")     
    assert not validate_password("Abcdef1@@")    
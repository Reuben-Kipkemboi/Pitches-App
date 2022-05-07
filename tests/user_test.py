import unittest # Importing unittest
from app.models import User # importing user class from our models

class UserModelTest(unittest.TestCase):
    #creating the instance of the user and then setting a password/passcode
    def setUp(self):
        self.new_user = User(password = 'pitches and pitches')
    #confirms that when password is being hashed and the password_secure contains a value.
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    # when user wants to access password it should throw an error/alert
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    #verifying password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('pitches&pitches'))

import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase) :
    """
    Test class that defines test cases for the credentials behaviours
    """
    def setUp(self):
        """
        Set up method to run before each test case 
        """
        self.new_credentials = Credentials("Twitter", "12345")

    def test_init(self) :
        """
        test_init test case to test if the object is initialised properly
        """
        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.account_password,"12345")

    def test_save_user(self):
        """
        test_save_user test case to test if credentials details are saved successfully
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__ == "__main__":
      unittest.main()
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

    def test_save_credentials(self):
        """
        test_save_credential test case to test if credentials details are saved successfully
        """
        self.new_credentials.save_credentials()
        self.assertEqual (len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        Method that clears the credentials_list after every test to ensure that there is no error
        """
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        """
        Method that saves multiple credentials to credentials_list
        """
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Facebook", "56789")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        """
        test_delete_credential to test if we can remove credential from list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail", "5678")

        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
    unittest.main()
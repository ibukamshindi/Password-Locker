import unittest
from user import User

class TestUser(unittest.TestCase) :

    """
    Test class that defines test cases for the user class behaviours
    """
    def setUp(self):
        """
        Set up method to run before each test case 
        """
        self.new_user = User("Juma","12345")
    
    def test_init(self) :
        """
        test_init test case to test if the object is initialised properly
        """
        self.assertEqual(self.new_user.user_name,"Juma")
        self.assertEqual(self.new_user.password,"12345")

    def test_save_user(self):
        """
        test_save_user test case to test if user details are saved successfully
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1) 

if __name__ == "__main__":
      unittest.main()



import unittest # Importing the unittest module
from user import User # Importing the user class
import pyperclip
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ani","Anipher","Chelsea") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.email,"ani")
        self.assertEqual(self.new_user.first_name,"Anipher")
        self.assertEqual(self.new_user.last_name,"Chelsea")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("vall","Valentine","Achieng") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("vall","Valentine","Achieng") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    # More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("vall","Valentine","Achieng") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
    def test_find_user_by_email(self):
        '''
        test to check if we can find a user by email and display information
        '''

        self.new_user.save_user()
        test_user = User("barry","Valentine","Achieng") # new user
        test_user.save_user()

        found_user = User.find_by_email("barry")

        self.assertEqual(found_user.first_name,test_user.first_name)
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("barry","Valentine","Achieng") # new user
        test_user.save_user()

        user_exists = User.user_exist("barry")

        self.assertTrue(user_exists)
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)
    def test_copy_first_name(self):
        '''
        Test to confirm that we are copying the first name from a found contact
        '''

        self.new_user.save_user()
        User.copy_first_name("ani")

        self.assertEqual(self.new_user.first_name,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()

import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("chelsea.ayoo@student.moringaschool.com","chelsea2021") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.email,"chelsea.ayoo@student.moringaschool.com")
        self.assertEqual(self.new_credential.password,"chelsea2021")


if __name__ == '__main__':
    unittest.main()
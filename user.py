import pyperclip
class User:
    """
    Class that generates new instances of users.
    """
    pass

    user_list = [] # Empty user list

    def __init__(self,email,first_name,last_name):

      # docstring removed for simplicity

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
    user_list = [] # Empty user list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns a user that matches that email.

        Args:
            email: Login email to search for
        Returns :
            User that matches the email.
        '''

        for user in cls.user_list:
            if user.email== email:
                return user
    @classmethod
    def user_exist(cls,email):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Login email to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.email == email:
                    return True

        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    @classmethod
    def copy_first_name(cls,email):
        user_found = User.find_by_email(email)
        pyperclip.copy(user_found.first_name)
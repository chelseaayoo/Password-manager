import pyperclip
class User:
    """
    Class that generates new instances of users.
    """
    pass

    user_list = [] # Empty user list

    def __init__(self,login_username,first_name,last_name):

      # docstring removed for simplicity

        self.login_username = login_username
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
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: Login username to search for
        Returns :
            User that matches the username.
        '''

        for user in cls.user_list:
            if user.login_username == username:
                return user
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Login username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.login_username == username:
                    return True

        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    @classmethod
    def copy_first_name(cls,username):
        user_found = User.find_by_username(username)
        pyperclip.copy(user_found.first_name)
import pyperclip
class Credential:
    """
    Class that generates new instances of credentials.
    """
    pass

    credential_list = [] # Empty credential list

    def __init__(self,login_username,password):

      # docstring removed for simplicity

        self.login_username = login_username
        self.password = password
    credential_list = [] # Empty credential list
 # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    @classmethod
    def find_by_login_username(cls,login_username):
        '''
        Method that takes in a login_username and returns a credential that matches that login_username.

        Args:
            login_username: login_username to search for
        Returns :
            Credential of person that matches the login_username.
        '''

        for credential in cls.credential_list:
            if credential.login_username == login_username:
                return credential
    @classmethod
    def credential_exist(cls,login_username):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            login_username: login_username to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.login_username == login_username:
                    return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
    @classmethod
    def copy_login_username(cls,login_username):
        credential_found = Credential.find_by_login_username(login_username)
        pyperclip.copy(credential_found.login_username)
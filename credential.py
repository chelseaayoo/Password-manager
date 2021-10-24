import pyperclip
class Credential:
    """
    Class that generates new instances of credentials.
    """
    pass

    credential_list = [] # Empty credential list

    def __init__(self,email,password):

      # docstring removed for simplicity

        self.email = email
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
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns a credential that matches that email.

        Args:
            email: email to search for
        Returns :
            Credential of person that matches the email.
        '''

        for credential in cls.credential_list:
            if credential.email == email:
                return credential
    @classmethod
    def credential_exist(cls,email):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.email == email:
                    return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
    @classmethod
    def copy_email(cls,email):
        credential_found = Credential.find_by_email(email)
        pyperclip.copy(credential_found.email)
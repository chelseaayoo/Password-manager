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
class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,email,password):

      # docstring removed for simplicity

        self.email = email
        self.password = password
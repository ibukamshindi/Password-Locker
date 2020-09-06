class Credentials:
    """
    Class that creates new instances of credentials 
    """
    def __init__(self,account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):

        """
        save_credential method saves credential objects into credential_list
        
        """
        Credentials.credentials_list.append(self)

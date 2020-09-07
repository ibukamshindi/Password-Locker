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

    def delete_credentials(self):

        """
        Method which deletes a particular credential

        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_credentials(cls):
        """
        Method which displays all current credentials
        """
        return cls.credentials_list   

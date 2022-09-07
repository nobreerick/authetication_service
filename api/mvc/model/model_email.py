class Email:
    def __init__(self,email_username,domain):
        self.email_username = email_username
        self.domain = domain
    
    def set_email_username(self, new_email_username):
        self.email_username = new_email_username
    
    def set_domain(self, new_domain):
        self.domain = new_domain

    def get_email_username(self, new_email_username):
        self.email_username = new_email_username
    
    def get_domain(self):
        return self.domain
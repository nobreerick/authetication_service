from MVC.model_email import Email 

class ControllerEmail:
    @classmethod
    def registry_email(cls, email: str ) -> Email:
        email_splited = email.split('@')
        email_username = email_splited[0]
        email_domain = email_splited[1]
        return Email(email_username, email_domain)

    @classmethod
    def validate_email(cls, email: str) -> bool:
        if len(email) <= 45 and '@' in email: return True
        else: return False

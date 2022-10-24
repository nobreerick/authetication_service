from MVC.model_tables import BaseEmail
from MVC.model_email import Email
from MVC.controller_db import DBConfig

class DaoEmail:

    @classmethod
    def insert_email(cls, Email: Email):
        
        session = DBConfig.return_session(DBConfig.return_engine())
        
        new_email = BaseEmail(email= f"{Email.get_email_username()}@{Email.get_domain()}")

        session.add(new_email)
        session.commit()

    @classmethod
    def update_email(cls, Email: Email, email_id):

        session = DBConfig.return_session(DBConfig.return_engine())

        query_list = session.query(BaseEmail).filter(BaseEmail.id == email_id).all()

        query_list[0].email = f"{Email.get_email_username()}@{Email.get_domain()}"

        session.commit()

    @classmethod
    def delete_email(cls, email_id):
        session = DBConfig.return_session(DBConfig.return_engine())

        session.query(BaseEmail).filter(BaseEmail.id == email_id).delete()

        session.commit()

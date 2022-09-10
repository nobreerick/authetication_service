from .model_tables import BasePhone
from .model_phone import Phone
from .controller_db import DBConfig

class DaoPhone:

    @classmethod
    def insert_phone(cls, Phone: Phone):
        
        session = DBConfig.return_session(DBConfig.return_engine())
        
        new_phone = BasePhone(phone_number= f"+{Phone.get_ddi()} {Phone.get_phone_number()}")

        session.add(new_phone)
        session.commit()

    @classmethod
    def update_phone(cls, Phone: Phone, phone_id):

        session = DBConfig.return_session(DBConfig.return_engine())

        query_list = session.query(BasePhone).filter(BasePhone.id == phone_id).all()

        query_list[0].phone_number = f"+{Phone.get_ddi()} {Phone.get_phone_number()}"

        session.commit()

    @classmethod
    def delete_phone(cls, phone_id):
        session = DBConfig.return_session(DBConfig.return_engine())

        session.query(BasePhone).filter(BasePhone.id == phone_id).delete()

        session.commit()

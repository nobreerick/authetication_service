from .model_tables import BaseUser
from .model_user import User
from .controller_db import DBConfig

class DaoUser:

    @classmethod
    def insert_user(cls, User: User):
        
        session = DBConfig.return_session(DBConfig.return_engine())
        
        new_user = BaseUser(username= User.get_username(), 
            password= User.get_password(), 
            active=True)

        session.add(new_user)
        session.commit()

    @classmethod
    def update_user(cls, User: User, user_id):

        session = DBConfig.return_session(DBConfig.return_engine())

        query_list = session.query(BaseUser).filter(BaseUser.id == user_id).all()

        query_list[0].username = User.get_username()
        query_list[0].password = User.get_password()
        query_list[0].active = User.get_active()

        session.commit()

    @classmethod
    def delete_user(cls, user_id):
        session = DBConfig.return_session(DBConfig.return_engine())

        session.query(BaseUser).filter(BaseUser.id == user_id).delete()

        session.commit()

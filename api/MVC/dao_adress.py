from MVC.model_tables import BaseAdress
from MVC.model_adress import Adress
from MVC.controller_db import DBConfig

class DaoAdress:

    @classmethod
    def insert_adress(cls, Adress: Adress):
        
        session = DBConfig.return_session(DBConfig.return_engine())
        
        new_adress = BaseAdress(country= Adress.get_country(), 
            state= Adress.get_state(), 
            city= Adress.get_city(), 
            street= Adress.get_street(), 
            number= Adress.get_number(), 
            postal_code= Adress.get_postal_code())

        session.add(new_adress)
        session.commit()

    @classmethod
    def update_adress(cls, Adress: Adress, adress_id):

        session = DBConfig.return_session(DBConfig.return_engine())

        query_list = session.query(BaseAdress).filter(BaseAdress.id == adress_id).all()

        query_list[0].country = Adress.get_country()
        query_list[0].state = Adress.get_state()
        query_list[0].city = Adress.get_city()
        query_list[0].street = Adress.get_street()
        query_list[0].number =  Adress.get_number()
        query_list[0].postal_code = Adress.get_postal_code()

        session.commit()

    @classmethod
    def delete_adress(cls, adress_id):
        session = DBConfig.return_session(DBConfig.return_engine())

        session.query(BaseAdress).filter(BaseAdress.id == adress_id).delete()

        session.commit()

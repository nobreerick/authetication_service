from .model_tables import BasePerson
from .model_person import Person
from .controller_db import DBConfig

class DaoPerson:

    @classmethod
    def insert_person(cls, Person: Person, user_id, email_id, phone_id, adress_id):
        
        session = DBConfig.return_session(DBConfig.return_engine())
        
        new_person = BasePerson(fname= Person.get_fname(),
            cpf= Person.get_cpf(),
            birthdate= Person.get_birthdate(), 
            user_id= user_id, 
            email_id= email_id, 
            phone_id= phone_id, 
            adress_id= adress_id)

        session.add(new_person)
        session.commit()

    @classmethod
    def update_person(cls, Person: Person, person_id):

        session = DBConfig.return_session(DBConfig.return_engine())

        query_list = session.query(BasePerson).filter(BasePerson.id == person_id).all()
        print(query_list)
        query_list[0].fname = Person.get_fname()
        query_list[0].cpf = Person.get_cpf()
        query_list[0].birthdate = Person.get_birthdate()

        session.commit()

    @classmethod
    def delete_person(cls, person_id):
        session = DBConfig.return_session(DBConfig.return_engine())

        session.query(BasePerson).filter(BasePerson.id == person_id).delete()

        session.commit()

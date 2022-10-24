from MVC.controller_db import DBConfig
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BasePerson(Base):

    __tablename__ = 'person'

    id = Column(Integer, 
        primary_key=True,
        autoincrement=True, 
        nullable=False, 
        unique=True)

    fname = Column(String(75), 
        nullable=False)

    cpf = Column(String(11), 
        nullable=False, 
        unique=True)

    birthdate = Column(DATE)

    user_id = Column(Integer, 
        ForeignKey('user.id'),
        nullable=False, 
        unique=True, 
        autoincrement='ignore_fk')

    email_id = Column(Integer, 
        ForeignKey('email.id'),
        nullable=False, 
        unique=True, 
        autoincrement='ignore_fk')

    phone_id = Column(Integer, 
        ForeignKey('phone.id'),
        nullable=False, 
        unique=True, 
        autoincrement='ignore_fk')

    adress_id = Column(Integer, 
        ForeignKey('adress.id'),
        nullable=False, 
        autoincrement='ignore_fk')

class BaseEmail(Base):

    __tablename__ = 'email'

    id = Column(Integer, 
        primary_key=True,
        autoincrement=True, 
        nullable=False, 
        unique=True)

    email = Column(String(45), 
        nullable=False, 
        unique=True)

class BasePhone(Base):

    __tablename__ = 'phone'

    id = Column(Integer, 
        primary_key=True, 
        autoincrement=True, 
        nullable=False, 
        unique=True)

    phone_number = Column(String(20),
        nullable=False, 
        unique=True)

class BaseAdress(Base):

    __tablename__ = 'adress'
    
    id = Column(Integer, 
        primary_key=True, 
        autoincrement=True, 
        nullable=False, 
        unique=True)

    country = Column(String(50),
        nullable=False)

    state = Column(String(50),
        nullable=False)

    city = Column(String(50),
        nullable=False)

    street = Column(String(70),
        nullable=False)

    number = Column(String(5),
        nullable=True)

    postal_code = Column(String(20),
        nullable=False)

class BaseUser(Base):

    __tablename__ = 'user'
    
    id = Column(Integer, 
        primary_key=True, 
        autoincrement=True, 
        nullable=False, 
        unique=True)

    username = Column(String(20),
        nullable=False, 
        unique=True)

    password = Column(String(32),
        nullable=False)

    active = Column(Boolean,
        nullable=False)

def create_all_tables(engine):
    Base.metadata.create_all(engine)

engine = DBConfig.return_engine()
create_all_tables(engine)

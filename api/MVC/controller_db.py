from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

class DBConfig:
    @classmethod
    def return_engine(cls):
        ENV = dotenv_values(".env")
        CONN = f"postgresql+psycopg2://{ENV['POSTGRES_USER']}:{ENV['POSTGRES_PASSWORD']}@{ENV['DB_HOST']}:{ENV['DB_PORT']}/{ENV['POSTGRES_DB']}"
#add:try except else finnaly to confirm connection with database
        return create_engine(CONN, echo=False)

    @classmethod
    def return_session(cls, engine):
        Session = sessionmaker(bind=engine)
        return Session()

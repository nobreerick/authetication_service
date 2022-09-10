#from MVC.dao_adress import *

#Create tables
"""
engine = DBConfig.return_engine()
create_tables(engine)
""" 
#Insert adress entry
""" 
adress = Adress('Brazil','RN','Pau dos ferros','Av dos caramunhões','s/n','59000000')
DaoAdress.insert_adress(adress)
"""
#Update adress entry
""" 
adress = Adress('USA','Georgia','Atlanta','125th Avenue','10B','30301')
DaoAdress.update_adress(adress, 3)
"""
#Delete adress entry
""" 
DaoAdress.delete_adress(1)
"""

#---------------------------------------------

#from MVC.dao_email import *

#Create tables
"""
engine = DBConfig.return_engine()
create_tables(engine)
""" 
#Insert email entry
""" 
email = Email('ericknobreds','gmail.com')
DaoEmail.insert_email(email)
"""
#Update email entry
""" 
email = Email('erick_nds','hotmail.com')
DaoEmail.update_email(email, 1)
"""
#Delete email entry
""" 
DaoEmail.delete_email(1)
"""

#---------------------------------------------

#from MVC.dao_phone import *

#Create tables
"""
engine = DBConfig.return_engine()
create_tables(engine)
""" 
#Insert phone entry
""" 
phone = Phone('55','84999998888')
DaoPhone.insert_phone(phone)
"""
#Update phone entry
""" 
phone = Phone('1','30982679341')
DaoPhone.update_phone(phone, 1)
"""
#Delete phone entry
""" 
DaoPhone.delete_phone(1)
"""

#---------------------------------------------

#from MVC.dao_user import *

#Create tables
"""
engine = DBConfig.return_engine()
create_tables(engine)
""" 
#Insert user entry
""" 
user = User('nobreerick','12345678')
DaoUser.insert_user(user)
"""
#Update user entry
""" 
user = User('erick_nobre','309879341')
user.set_active(False)
DaoUser.update_user(user, 1)
"""
#Delete user entry
""" 
DaoUser.delete_user(1)
"""

#---------------------------------------------

#from MVC.dao_person import *

#Create tables
"""
engine = DBConfig.return_engine()
create_tables(engine)
""" 
#Insert person entry
""" 
person = Person('erick nobre','01919123421','1991-03-22')
DaoPerson.insert_person(person,2,1,1,1)
"""
#Update person entry
""" 
person = Person('erick miller','09809809812','2000-01-01')
DaoPerson.update_person(person, 2)
"""
#Delete person entry
""" 
DaoPerson.delete_person(2)
"""

#---------------------------------------------

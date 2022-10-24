#controller_generic
""" 
from MVC.controller_generic import ControllerGeneric
tday = '29'
tmonth = '2'
tyear = '2021' 
"""
#---------------------------------------------------------------
# date_format(year, month, day) -> String
# print(ControllerGeneric.date_format(tyear, tmonth, tday))
#---------------------------------------------------------------
# validate_day(year, month, day) -> Bool
# print(ControllerGeneric.validate_day(tyear, tmonth, tday))
#---------------------------------------------------------------
# validate_month(month) -> Bool
# print(ControllerGeneric.validate_month(tmonth))
#---------------------------------------------------------------
# validate_year(year) -> Bool
# print(ControllerGeneric.validate_year(tyear))
#---------------------------------------------------------------
# is_date_future(year, month, day) -> Bool
# print(ControllerGeneric.is_date_future(tyear, tmonth, tday))
#---------------------------------------------------------------

#controller_person
""" 
from MVC.controller_person import ControllerPerson
cpf_invalid_same_digits = '00000000000'
cpf_invalid_bigger = '438745170041'
cpf_invalid = '12312312321'
cpf_valid = '43874517004'
tday = '18'
tmonth = '9'
tyear = '2022'
tfname = 'Hallbjorn Alf Berghild'
tfname_invalid = 'Nechtan Cyhiraeth Ceibhfhionn Airmid Teutates Cuchulainn Blathnat Sadb Shannon' 
"""
#---------------------------------------------------------------
# validate_cpf(cpf) -> bool
# print(ControllerPerson.validate_cpf(cpf_invalid_same_digits))
# print(ControllerPerson.validate_cpf(cpf_invalid_bigger))
# print(ControllerPerson.validate_cpf(cpf_invalid))
# print(ControllerPerson.validate_cpf(cpf_valid))
#---------------------------------------------------------------
# validate_fname(fname: str) -> bool
# print(ControllerPerson.validate_fname(tfname_invalid))
#---------------------------------------------------------------
# validate_birthdate(year, month, day) -> bool
# print(ControllerPerson.validate_birthdate(tyear, tmonth, tday))
#---------------------------------------------------------------'
# registry_person(fname, cpf, birthdate) -> Person
#---------------------------------------------------------------

#controller_adress
""" 
from MVC.controller_adress import ControllerAdress
country_invalid = 'United Kingdom of Great Britain and Northern Ireland'
country_valid = 'United Kingdom'
state_invalid = 'State of Rhode Island and Providence Plantations America'
state_valid = 'Rhode Island'
city_invalid = 'Krung Thep Mahanakhon Amon Rattanakosin Mahinthara Yuthaya Mahadilok Phop Noppharat Ratchathani Burirom Udomratchaniwet Mahasathan Amon Piman Awatan Sathit Sakkathattiya Witsanukam Prasit!'
city_valid = 'Bangkok'
street_invalid = 'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogochrychwyrndrobwllllantysiliogogogoch'
street_valid = '124th street'
number_invalid = '100000'
number_valid = '99999'
number_valid_empty = None
postal_code_invalid = '590000001590000001212'
postal_code_valid = '59000000'
"""
#---------------------------------------------------------------
# registry_adress(country: str, state: str, city: str, street: str, number: str, postal_code: str ) -> Adress
#---------------------------------------------------------------
# validate_country(country: str) -> bool
# print(ControllerAdress.validate_country(country_valid))
#---------------------------------------------------------------
# validate_state(state: str) -> bool
# print(ControllerAdress.validate_state(state_valid))
#---------------------------------------------------------------
# validate_city(city: str) -> bool
# print(ControllerAdress.validate_city(city_valid))
#---------------------------------------------------------------
# validate_street(street: str) -> bool
# print(ControllerAdress.validate_street(street_valid))
#---------------------------------------------------------------
# validate_number(number: str) -> bool
# print(ControllerAdress.validate_number(number_invalid))
#---------------------------------------------------------------
# validate_postal_code(postal_code: str) -> bool
# print(ControllerAdress.validate_postal_code(postal_code_valid))
#---------------------------------------------------------------

#controller_email
""" 
from MVC.controller_email import ControllerEmail
email_invalid_long = 'publictest_gov_us_publictest_gov_us@publictest.gov.us'
email_invalid_no_at = 'publictest.gov.us'
email_valid = 'publictest@test.gov.us'
"""
#---------------------------------------------------------------
# registry_email(email: str ) -> Email
#---------------------------------------------------------------
# validate_email(email: str) -> bool
# print(ControllerEmail.validate_email(email_invalid_long))
#---------------------------------------------------------------

#controller_phone
""" 
from MVC.controller_phone import ControllerPhone
phone_invalid = 'a91239412'
phone_invalid_long = '912394129123941291239412'
phone_valid = '89976541234'
ddi = '55'
"""
#---------------------------------------------------------------
# registry_phone(phone: str ) -> Phone
#---------------------------------------------------------------
# validate_phone(phone: str) -> bool
# print(ControllerPhone.validate_phone(ddi, phone_invalid_long))
#---------------------------------------------------------------
# generate_DDI_dictionary(cls, csv_file: str)
""" ddi_dict = ControllerPhone.generate_DDI_dictionary('/home/nobreerick/Estudo/PythonFull/Projetos/authetication_service/api/assets/DDI_List.csv')
for i in ddi_dict:
    print(f'{i}, {ddi_dict[i]}') """
#---------------------------------------------------------------
#controller_user

from MVC.controller_user import ControllerUser
username_valid = 'ErickMiller123456789'
username_invalid_01 = 'ErickMiller1234567890'
username_invalid_02 = 'Erick89'
password_valid = 'Ee@1231'
password_invalid = 'MONONONONO'

#---------------------------------------------------------------
# validate_username(cls, username: str) -> bool
print(ControllerUser.validate_username(username_valid))
#---------------------------------------------------------------
# validate_password(cls, password: str) -> bool
print(ControllerUser.validate_password(password_valid))
#---------------------------------------------------------------

from MVC.model_phone import Phone
from MVC.controller_generic import ControllerGeneric
import csv

class ControllerPhone:
    @classmethod
    def registry_phone(cls, phone_ddi, phone_number ) -> Phone:
        return Phone(phone_ddi, phone_number)

    @classmethod
    def generate_DDI_dictionary(cls, csv_file: str):
        with open(csv_file, newline='') as csvfile:
            Spamreader = csv.reader(csvfile, delimiter=';')
            ddi_dict = {}
            for row in Spamreader:
                ddi_dict[row[0]] = row[1]
            return ddi_dict

    @classmethod
    def validate_phone(cls, ddi: str, phone: str) -> bool:
        formated_phone = ControllerGeneric.phone_format(ddi, phone)
        if len(formated_phone) <= 20 and phone.isnumeric(): return True
        else: return False

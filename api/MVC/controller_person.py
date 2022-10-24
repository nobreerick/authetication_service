from MVC.controller_generic import ControllerGeneric
from MVC.model_person import Person


class ControllerPerson:
    @classmethod
    def registry_person(cls, fname: str, cpf: str, birthdate: str ) -> Person:
        return Person(fname, cpf, birthdate)

    @classmethod
    def validate_fname(cls, fname: str) -> bool:
        if len(fname) <= 75: return True
        else: return False

    @classmethod
    def validate_birthdate(cls, year: str, month: str, day: str) -> bool:
        year_valid = ControllerGeneric.validate_year(year)
        month_valid = ControllerGeneric.validate_month(month)
        day_valid = ControllerGeneric.validate_day(year, month, day)
        if year_valid and month_valid and day_valid:
            if not ControllerGeneric.is_date_future(year, month, day): return True
            else: return False
        else: return False
    
    @classmethod
    def validate_cpf(cls, cpf: str) -> bool:
        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

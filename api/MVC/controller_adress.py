from MVC.model_adress import Adress

class ControllerAdress:
    @classmethod
    def registry_person(cls, country: str, state: str, city: str, street: str, number: str, postal_code: str ) -> Adress:
        return Adress(country, state, city, street, number, postal_code)

    @classmethod
    def validate_country(cls, country: str) -> bool:
        if len(country) <= 50: return True
        else: return False
    
    @classmethod
    def validate_state(cls, state: str) -> bool:
        if len(state) <= 50: return True
        else: return False
    
    @classmethod
    def validate_city(cls, city: str) -> bool:
        if len(city) <= 50: return True
        else: return False

    @classmethod
    def validate_street(cls, street: str) -> bool:
        if len(street) <= 70: return True
        else: return False
    
    @classmethod
    def validate_number(cls, number: str) -> bool:
        if not number: return True
        if len(number) <= 5: return True
        else: return False

    @classmethod
    def validate_postal_code(cls, postal_code: str) -> bool:
        if len(postal_code) <= 20 and postal_code.isnumeric() : return True
        else: return False
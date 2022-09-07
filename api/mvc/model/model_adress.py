class Adress:
    def __init__(self, country, state, city, street, number, postal_code):
        self.country = country
        self.state = state
        self.city = city
        self.street = street
        self.number = number
        self.postal_code = postal_code

    def set_country(self, new_country):
        self.country = new_country
    
    def get_country(self):
        return self.country

    def set_state(self, new_state):
        self.state = new_state
    
    def get_state(self):
        return self.state   

    def set_city(self, new_city):
        self.city = new_city
    
    def get_city(self):
        return self.city

    def set_street(self, new_street):
        self.street = new_street
    
    def get_street(self):
        return self.street

    def set_number(self, new_number):
        self.number = new_number
    
    def get_number(self):
        return self.number

    def set_postal_code(self, new_postal_code):
        self.postal_code = new_postal_code
    
    def get_postal_code(self):
        return self.postal_code
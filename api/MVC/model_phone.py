class Phone:
    def __init__(self,ddi,phone_number):
        self.ddi = ddi
        self.phone_number = phone_number
    
    def set_ddi(self, new_ddi):
        self.ddi = new_ddi
    
    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def get_ddi(self):
        return self.ddi
    
    def get_phone_number(self):
        return self.phone_number

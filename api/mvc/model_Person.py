class Person:
    def __init__(self, fname, cpf, birthdate):
        self.fname = fname
        self.cpf = cpf
        self.birthdate = birthdate

    def set_fname(self, new_fname):
        self.fname = new_fname

    def set_cpf(self, new_cpf):
        self.cpf = new_cpf

    def set_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate
    
    def get_fname(self):
        return self.fname
    
    def get_cpf(self):
        return self.cpf

    def get_birthdate(self):
        return self.birthdate
    
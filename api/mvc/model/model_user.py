class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_password):
        self.password = new_password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    
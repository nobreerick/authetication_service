class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.active = True

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_password):
        self.password = new_password

    def set_active(self, new_active_state):
        self.active = new_active_state

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_active(self):
        return self.active

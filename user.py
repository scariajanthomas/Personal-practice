class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

    def validate(self, input_password):
        if self.password == input_password:
            return True
        else:
            return False
    
    def update_password(self, new_password):
        new_password = new_password.strip()
        if new_password == "":
            raise ValueError("Password cannot be empty")
        else:
            self.password = new_password

    def is_admin(self):
        if self.username == "admin":
            return True
        else:
            return False


 

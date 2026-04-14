from datetime import datetime


class Session:
    def __init__(self):
        self.is_active = False
        self.login_time = None

    def login(self):
        self.is_active = True
        self.login_time = datetime.now()

    def logout(self):
        self.is_active = False
        self.login_time = None

class User:
    def __init__(self, username, password):
        self.session = Session()
        self.username = self.validate_username(username)
        self.password = self.validate_password(password)

    def display(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

    def validate(self, input_password):
        if self.password == input_password:
            return True
        else:
            return False
            
    def validate_password(self, password):
        if password.strip() == "":
            raise ValueError("Password cannot be empty")
        return password.strip()
    
    def validate_username(self, username):
        if username.strip() == "":
            raise ValueError("Username cannot be empty")
        return username.strip()

    def update_password(self, new_password):
        self.password = self.validate_password(new_password)

    def is_admin(self):
        if self.username == "admin":
            return True
        else:
            return False

class AdminUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def change_username(self, new_username):
        self.username = self.validate_username(new_username)

    def delete_user(self, username, user_list):
        for user in user_list:
            if user.username == username:
                user_list.remove(user)
                return
        raise ValueError(f"User '{username}' not found")
    


if __name__ == "__main__":
    user1 = User("luci", "luci123")
    user1.display()
    user1.session.login()
    print(user1.session.is_active)
    user2 = AdminUser("admin", "adminpass")
    user2.change_username("Admina")
    print(user2.username)
    user2.session.logout()
    print(user2.session.is_active)
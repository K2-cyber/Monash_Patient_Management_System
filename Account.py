
# define Account class for create Account objects as the parent class for child classes
class Account:
    __email = ""  # declare email as private attribute and string
    __password = ""  # declare password as private attribute and string

    def __init__(self, user_email, user_password):  # constructor of the class account
        self.email = user_email
        self.password = user_password

    # getter method for email
    def get_email(self):
        return self.email

    # getter method for password
    def get_password(self):
        return self.password

    # setter method for email
    def set_email(self, new_email):
        self.email = new_email

    # setter method for password
    def set_password(self, new_password):
        self.password = new_password

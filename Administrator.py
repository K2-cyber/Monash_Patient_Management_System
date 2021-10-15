from Account import Account

# define Admin class to create admin objects as child class of Account class
class Admin(Account):

    # define Constructor of Admin class
    def __init__(self):
        super().__init__(user_email="admin@monash.edu", user_password="Monash1234")     # call Constructor of Super class

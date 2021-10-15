from Account import Account

# patient class inherits from Account class
class Patient(Account):
    __patient_first_name = "" # declare user_first_name attribute as private string
    __patient_last_name = ""  # declare user_last_name attribute as private string

    # Constructor of Patient class
    def __init__(self, email = "patient@monash.edu", password = "Monash1234", first_name = "Daghash", last_name = "Alqahtani"):
        super().__init__(email , password)  # call the Constructor of Super class
        self.patient_first_name = first_name
        self.patient_last_name = last_name

    # getter method for first name
    def get_first_name(self):
        return self.patient_first_name

    # getter method for last name
    def get_last_name(self):
        return self.patient_last_name

    # setter method for first name
    def set_first_name(self, first_name):
        self.patient_first_name = first_name

    #setter method for last name
    def set_last_name(self, last_name):
        self.patient_last_name = last_name

    # override string method
    def __str__(self):
        return self.patient_first_name + " " + self.patient_last_name

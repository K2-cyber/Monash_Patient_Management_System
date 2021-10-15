"""
This is a GP class which provides the structure of entity class. The GP object is created with the help of this class.
The attributes that contribute to the making of the GP object are : GP first name, GP last name, GP phone number, GP area of expertise,
GP clinic assigned and GP number of appointment

"""


class GP:
    __GP_first_name = ""  # declare GP first name as private attribute and string
    __GP_last_name = ""  # declare GP last name as private attribute and string
    __GP_phone_number = ""  # declare GP phone number as private attribute and string
    __GP_area_of_interest = ""  # declare GP area of interest as private attribute and string
    __GP_clinic_assigned = ""  # declare GP clinic assigned as private attribute and string
    __GP_number_of_appointment = int()  # declare GP number of appointment as private attribute and integer

    # define constructor of the class GP
    def __init__(self, first_name, last_name, phone_number, area_of_interest, clinic_assigned, number_of_appointment):
        self.GP_first_name = first_name
        self.GP_last_name = last_name
        self.GP_phone_number = phone_number
        self.GP_area_of_interest = area_of_interest
        self.GP_clinic_assigned = clinic_assigned
        self.GP_number_of_appointment = number_of_appointment

    # getter method for first name
    def get_GP_first_name(self):
        return self.GP_first_name

    # getter method last name
    def get_GP_last_name(self):
        return self.GP_last_name

    # getter method for phone number
    def get_GP_phone_number(self):
        return self.GP_phone_number

    # getter method for area of interest
    def get_GP_area_of_interest(self):
        return self.GP_area_of_interest

    # getter method for clinic assigned
    def get_GP_clinic_assigned(self):
        return self.GP_clinic_assigned

    # getter method for number of appointments
    def get_GP_number_of_appointment(self):
        return self.GP_number_of_appointment

    # setter method for first name
    def set_GP_first_name(self, new_first_name):
        self.GP_first_name = new_first_name

    # setter method for last name
    def set_GP_last_name(self, new_last_name):
        self.last_name = new_last_name

    # setter method for phone number
    def set_GP_phone_number(self, new_phone_number):
        self.GP_phone_number = new_phone_number

    # setter method for area of interest
    def set_GP_area_of_interest(self, new_area_of_interest):
        self.GP_area_of_interest = new_area_of_interest

    # setter method for clinic assigned
    def set_GP_clinic_assigned(self, new_clinic_assigned):
        self.GP_clinic_assigned = new_clinic_assigned

    # setter method for number of appointments
    def set_GP_number_of_appointment(self, new_number_of_appointment):
        self.GP_number_of_appointment = new_number_of_appointment

    # override string method
    def __str__(self):
        return self.GP_first_name + " " + self.GP_last_name


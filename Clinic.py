"""
This is a Clinic class which provides the structure of entity class. The Clinic object is created with the help of this class.
The attributes that contribute to the making of the Clinic object are : Clinic Branch, Clinic Address, Clinic Phone,
Clinic Opening Hours

"""


class Clinic:
    __clinic_branch = ""  # declare clinic branch as private attribute and string
    __clinic_address = ""  # declare clinic address as private attribute and string
    __clinic_phone = ""  # declare clinic phone as private attribute and string
    __clinic_opening_hours = ""  # declare clinic opening hours as private attribute and string

    # define the constructor of clinic class
    def __init__(self, branch, addr, phoneNbr, open):
        self.clinic_branch = branch
        self.clinic_address = addr
        self.clinic_phone = phoneNbr
        self.clinic_opening_hours = open

    # getter for clinic branch's name
    def get_clinic_branch(self):
        return self.clinic_branch

    # getter for clinic's address
    def get_clinic_address(self):
        return self.clinic_address

    # getter for clinic's phone number
    def get_clinic_phone(self):
        return self.clinic_phone

    # getter for clinic's opening hour
    def get_opening_hour(self):
        return self.clinic_opening_hours

    # setter for clinic's name
    def set_clinic_branch(self, new_clinic):
        self.clinic_branch = new_clinic

    # setter for clinic's address
    def set_clinic_address(self, new_address):
        self.clinic_address = new_address

    # setter for clinic's phone number
    def set_clinic_phone(self, new_phone):
        self.clinic_phone = new_phone

    # setter for clinic's opening hour
    def set_clinic_opening_hour(self, new_open):
        self.clinic_opening_hours = new_open

    # override string method to print clinic object
    def __str__(self):
        return "Branch: " + self.clinic_branch + "\n" + "Address: " + self.clinic_address + "\n" + "Phone: " + self.clinic_phone + "\n" + "Opening hours: " + self.clinic_opening_hours + "\n"


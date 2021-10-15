"""
This is an Appointment class which provides the structure of entity class. The Appointment object is created with the help of this class.
The attributes that contribute to the making of the Appointment object are : patient name, appointment date, appointment time,
appointment branch and GP assigned for the appointment

"""


class Appointment:
    __patient_name = ""  # declare patient name as private attribute and string
    __appointment_clinic_branch = "" # declare patient name as private attribute and string
    __appointment_date = ""  # declare appointment date as private attribute and string
    __appointment_time = ""  # declare appointment time as private attribute and string
    __appointment_GP = ""  # declare appointment GP as private attribute and string

    # define the constructor of appointment class
    def __init__(self, patient_name="", app_branch="", app_date="", app_time="", app_gp=""):
        self.patient_name = patient_name
        self.appointment_date = app_date
        self.appointment_time = app_time
        self.appointment_clinic_branch = app_branch
        self.appointment_GP = app_gp

    # getter for patient name
    def get_patient_name(self):
        return self.patient_name

    # getter for date
    def get_appointment_date(self):
        return self.appointment_date

    # getter for time
    def get_appointment_time(self):
        return self.appointment_time

    # getter for appointment GP
    def get_appointment_GP(self):
        return self.appointment_GP

    # getter for appointment clinic branch
    def get_appointment_clinic_branch(self):
        return self.appointment_clinic_branch

    # setter for patient's name
    def set_patient_name(self, new_name):
        self.patient_name = new_name

    # setter for appointment date
    def set_date(self, new_app_date):
        self.appointment_date = new_app_date

    # setter for appointment time
    def set_time(self, new_app_time):
        self.appointment_time = new_app_time

    # setter for appointment GP
    def set_appointment_GP(self, new_app_gp):
        self.appointment_GP = new_app_gp

    # setter for appointment clinic branch
    def set_appointment_branch(self, new_app_clinic):
        self.appointment_clinic_branch = new_app_clinic

    # override method to display appointment details
    def __str__(self):
        return "Date: " + self.appointment_date + "\n" + "Time: " + self.appointment_time + "\n" + "Clinic Branch: " + self.appointment_clinic_branch + "\n" + "GP: " + self.appointment_GP + "\n"
"""
This is a Report class which provides the structure of entity class. The Report object is created with the help of this
class.The attributes that contribute to the making of the Report object are : GP name, start date of report, end date of
report and number of patients

"""

class Report:
    __GP = ""  # # declare GP as private attribute and string
    __start_date = ""  # declare start date of report as private attribute and string
    __end_date = ""  # declare end date as private attribute and string
    __number_patient = int()    # declare number of patients as private attribute and int

    # define the constructor of class Report
    def __init__(self, GP, report_start_date, report_end_date, no_patient):
        self.GP = GP
        self.start_date = report_start_date
        self.end_date = report_end_date
        self.number_patient= no_patient

    # getter method for GP name
    def get_GP_name(self):
        return self.GP

    # getter method start date
    def get_start_date(self):
        return self.start_date

    # getter method for end date
    def get_end_date(self):
        return self.end_date

    # getter method for number of patient
    def get_number_patient(self):
        return self.number_patient

    # setter method GP name
    def set_GP_name(self, new_GP_name):
        self.GP = new_GP_name

    # setter method for start date
    def set_start_date(self, new_start_date):
        self.start_date = new_start_date

    # setter method for end date
    def set_end_date(self,new_end_date):
        self.end_date = new_end_date

    # getter method for number of patient
    def set_number_patient(self, new_no_patient):
        self.number_patient = new_no_patient


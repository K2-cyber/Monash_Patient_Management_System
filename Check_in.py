"""
This is a Check_in class which provides the structure of entity class. The Check_in object is created with the help of this class.
The attribute that contribute to the making of the Check_in object is : Number of patients

"""
class checkIn:
    # declare number of patients checked in as private attribute and integer
    __number_of_patients = int()

    # define constructor of class Check_in
    def __init__(self, number_of_patients):
        self.Check_in_number_of_patients = number_of_patients

    # getter method for number of patients checked in
    def get_Check_in_number_of_patients(self):
        return self.Check_in_number_of_patients

    # setter method for number of patients checked in
    def set_Check_in_number_of_patients(self, new_Check_in_number_of_patients):
        self.Check_in_number_of_patients = new_Check_in_number_of_patients
"""
This is an Reason class which provides the structure of entity class. The Reason object is created with the help of this class.
The attributes that contribute to the making of the Reason object are : type of reason and duration of the appointment

"""


class Reason:
    __type_of_reason = ""  # private attribute of type string
    __duration = ""  # private attribute of type string for duration of appointment

    # constructor of the reason class
    def __init__(self, reason="", time_length=""):
        self.type_of_reason = reason
        self.duration = time_length

    # getter for reason's type
    def get_reason(self):
        return self.type_of_reason

    # getter for duration
    def get_duration(self):
        return self.duration

    # setter for reason
    def set_reason(self, new_reason):
        self.type_of_reason = new_reason

    # setter for duration
    def set_duration(self, new_duration):
        self.duration = new_duration

    # string class override
    def __str__(self):
        return self.type_of_reason + self.duration

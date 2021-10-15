"""This is an Question class which provides the structure of entity class. The question object is created with the
help of this class. The attributes that contribute to the making of the question object are : question
"""


class Question:
    __question = "" # question attribute that is a private attribute of type string

    # constructor of the question class
    def __init__(self, new_question=""):
        self.question = new_question

    # getter for question
    def get_question(self):
        return self.question

    # setter for question
    def set_question(self, new_question):
        self.question = new_question



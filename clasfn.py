class Student:
    def __init__(self,name,percentage):
        self.name=name
        self.percentage=percentage
    def first_cl(self):
        if self.percentage>60:
            return True
        else:
            return False


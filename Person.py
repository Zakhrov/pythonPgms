class Person1:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"I am {self.name}")

p=Person1("john")
p.talk()

# create student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print the average


class Student:
    def __init__(self, name, physics, chemistry, maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        print("creating student database:")

    def get_avg(self):
        total = (self.physics + self.chemistry + self.maths) / 3
        return total


s1 = Student("harshit", 99, 98, 97)
print(s1.name, s1.get_avg())

s1.name="Annant"
print(s1.name, s1.get_avg())
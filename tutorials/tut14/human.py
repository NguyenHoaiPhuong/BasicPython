class Human:
    'Base class for human'
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        string = 'I am ' + self.name + '\n' \
                 'I am ' + str(self.age) + ' years old\n' \
                 'I am ' + self.sex
        return string

class Male(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = 'male'

class Female(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = 'female'
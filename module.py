class Employee:
    def __init__(self, first, last, pay):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@gmail.com"
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
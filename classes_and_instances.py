class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@wp.pl'
        self.email = '{}.{}@wp.pl'.format(first.lower(), last.lower())

emp_1 = Employee('Marcin', 'Sieciechowicz', 200_000)
emp_2 = Employee('Mikołaj', 'Sieciechowicz', 20_000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)


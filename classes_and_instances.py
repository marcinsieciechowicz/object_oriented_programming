class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@wp.pl'
        self.email = '{}.{}@wp.pl'.format(first.lower(), last.lower())

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Marcin', 'Sieciechowicz', 200_000)
emp_2 = Employee('Mikołaj', 'Sieciechowicz', 20_000)

emp_str_1 = 'Maciej-Kowalski-7000'
emp_str_2 = 'Michał-Nowak-1000'
emp_str_3 = 'Wojciech-Wiśniewski-2000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.first)
print(new_emp_1.pay)
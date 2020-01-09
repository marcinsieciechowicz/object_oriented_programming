import datetime


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

    @staticmethod
    def is_workday(day: datetime):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



class Developer(Employee):
    pass



emp_1 = Developer('Marcin', 'Sieciechowicz', 200_000)
emp_2 = Developer('Mikołaj', 'Sieciechowicz', 20_000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


my_date = datetime.date(2016, 7, 11)

print(Developer.is_workday(my_date))

emp_str_1 = 'Maciej-Kowalski-7000'
emp_str_2 = 'Michał-Nowak-1000'
emp_str_3 = 'Wojciech-Wiśniewski-2000'

new_emp_1 = Developer.from_string(emp_str_1)

print(new_emp_1.first)
print(new_emp_1.pay)

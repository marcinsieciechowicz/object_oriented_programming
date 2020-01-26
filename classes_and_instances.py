import datetime


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@wp.pl'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self, ):
        print('Delete Name!')
        self.first = None
        self.last = None

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
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def del_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Marcin', 'Sieciechowicz', 200_000)
emp_2 = Employee('Mikołaj', 'Sieciechowicz', 20_000)

emp_1.fullname = 'Szuszwol Schafer'

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
# print(len(emp_1))
# mgr_1 = Manager('Marcin', 'Smith', 9000, [emp_1])

# print(issubclass(Manager, Developer))

# print(emp_1)
# print(emp_1.prog_lang)

# print(emp_1.__repr__())
# print(emp_1.__str__())
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

emp_str_1 = 'Maciej-Kowalski-7000'
emp_str_2 = 'Michał-Nowak-1000'
emp_str_3 = 'Wojciech-Wiśniewski-2000'

# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.first)
# print(new_emp_1.pay)

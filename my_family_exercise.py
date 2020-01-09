from enum import Enum


class Sex(Enum):
    MALE: 'm'
    FEMALE: 'f'


class Sieciechowicz_fam_member(object):
    last = 'Sieciechowicz'
    num_of_membs = 0

    def __str__(self) -> str:
        return f'{self.first} {Sieciechowicz_fam_member.last} ({self.sex})'

    def __init__(self, first, sex):
        self.first = first
        self.sex = sex

        Sieciechowicz_fam_member.num_of_membs += 1

    lista = ['Marcin', 'male']

    @classmethod
    def from_string(cls, str):
        first, sex = str.split()
        return cls(first, sex)

    @classmethod
    def from_list(cls, lst):
        first, sex = lst
        return cls(first, sex)
    @classmethod
    def from_dict(cls, dict):
        first, sex = dict['first'], dict['sex']
        return cls(first, sex)

s_szuszwol = 'Marcin male'
szuszwol = Sieciechowicz_fam_member.from_string(s_szuszwol)

lst_Szuszwol = ['Macrin', 'male']
szuszwol = Sieciechowicz_fam_member.from_list(lst_Szuszwol)

dict_szuszwol = {'first': 'Marcin', 'sex': 'male'}
szuszwol = Sieciechowicz_fam_member.from_dict(dict_szuszwol)

# szuszwol = Sieciechowicz_fam_member('Marcin', Sex.MALE)
# Natalia = Sieciechowicz_fam_member('Natalia', Sex.FEMALE)
# Małgorzata = Sieciechowicz_fam_member('Małgorzata', 'female')
# Mikołaj = Sieciechowicz_fam_member('Mikołaj', 'male')


# print(szuszwol)
# print(Natalia)
# print(Małgorzata)
# print(Mikołaj)

# print(szuszwol.__dict__)
# print(object.__dict__)

print(szuszwol)

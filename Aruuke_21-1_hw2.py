class Company(object):
    def __init__(self, company_name, company_bank):
        self.company_name = company_name
        self.company_bank = company_bank


class Person(Company):
    salary = 0

    def __init__(self, company_name, company_bank, first_name, last_name):
        super().__init__(company_name, company_bank)
        self.first_name = first_name
        self.last_name = last_name


    def get_salary(self):

        if self.company_bank < self.salary:
            print('У компании не достаточно средств!')
        elif self.company_bank > self.salary:
            Person.salary += 5000
            self.company_bank = self.company_bank - self.salary
            print("Вам перечислили зарплату!")


    def person_info(self):
        print(self.first_name)
        print(self.last_name)
        print(Person.salary)


aru = Person(company_name='Pinterest', company_bank=1000000, first_name='Aruuke', last_name='Atabekova')
aru.get_salary()
aru.person_info()




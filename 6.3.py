class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'

p = Position('John', 'Galt', 'CEO', 15000, 2000)
print(p.get_full_name() + ',' + p.position + ',' + p.get_total_income())
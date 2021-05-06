
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

worker = Position('Ivan', 'Ivanov', 'Boss', 500, 50)

print(worker.name)
print(worker.surname)
print(worker.position)

worker.get_total_income()
worker.get_full_name()
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисую карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисую маркером')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()

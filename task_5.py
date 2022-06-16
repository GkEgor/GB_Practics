

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. (class_Stationery)')

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Используем {self.title}. Запуск отрисовки. (class_Pen)')

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Используем {self.title}. Запуск отрисовки. (class_Pencil)')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Используем {self.title}. Запуск отрисовки. (class_Handle)')

base = Stationery('Маркет')
base = base.draw()

pen = Pen('Ручку')
pen = pen.draw()

pencil = Pencil('Карандаш')
pencil = pencil.draw()

handle = Handle('Маркер')
handle = handle.draw()


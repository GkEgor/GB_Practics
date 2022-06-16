

class Car:
    def __init__(self, name, color, speed, is_police = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        if self.is_police == True:
            print(f'Полицеский автомобиль {self.color} {self.name} начал движение')
        else:
            print(f'{self.color} {self.name} начал движение')

    def stop(self):
        if self.is_police == True:
            print(f'Полицейский автомобиль {self.color} {self.name} остановился')
        else:
            print(f'{self.color} {self.name} остановился')

    def turn(self, duration):
        print(f'{self.color} {self.name} {duration}')

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')

class Town_car(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.speed} км/ч. Ограничение скорости 60 км/ч. Сбавьте скорость!')
        else:

            print(f'Текущая скорость {self.speed} км/ч')

class Sport_car(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
            print(f'Текущая скорость {self.speed} км/ч')

class Work_car(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.speed} км/ч. Ограничение скорости 40 км/ч. Сбавьте скорость!')
        else:

            print(f'Текущая скорость {self.speed} км/ч')

class Police_car(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
            print(f'Текущая скорость {self.speed} км/ч')



town_car = Town_car('Киа Стингер', 'Желтый', 120)
print(f'модель: {town_car.name}, цвет: {town_car.color}, текущая скорость: {town_car.speed} км/ч, полицейский статус: {town_car.is_police}')
town_car.go()
town_car.show_speed()
town_car.turn('повернул направо')
town_car.stop()

sport_car = Sport_car('Мерседес МакЛарен', 'Белый', 230)
print(f'\nмодель: {sport_car.name}, цвет: {sport_car.color}, текущая скорость км/ч: {sport_car.speed}, полицейский статус: {sport_car.is_police}')
sport_car.go()
sport_car.show_speed()
sport_car.turn('гоняется на треке')
sport_car.stop()

work_car = Work_car('Боб Кат', 'Оранжевый', 39)
print(f'\nмодель: {work_car.name}, цвет: {work_car.color}, текущая скорость: {work_car.speed} км/ч, полицейский статус: {work_car.is_police}')
work_car.go()
work_car.show_speed()
work_car.turn('поверннул налево')
work_car.stop()

police_car = Police_car('Шкода Суперб', 'Белый', 140, True)
print(f'\nмодель: {police_car.name}, цвет: {police_car.color}, текущая скорость: {police_car.speed} км/ч, полицейский статус: {police_car.is_police}')
police_car.go()
police_car.show_speed()
police_car.turn(f'Гонится за нарушителем')
police_car.stop()






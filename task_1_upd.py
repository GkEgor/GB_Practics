from time import sleep

class Traffic_lights:

    def __init__(self, color_1, color_2, color_3):
        self._color_1 = color_1
        self._color_2 = color_2
        self._color_3 = color_3
        while True:
            if self._color_1 != 'красный':
                print('Неверный порядок светофора, первый цвет должен быть "красный"')
                self._color_1 = input('Введите первый цвет светофора еще раз ')
            if self._color_2 != 'желтый':
                print('Неверный порядок светофора, второй цвет должен быть "желтый"')
                self._color_2 = input('Введите второй цвет светофора еще раз ')
            if self._color_3 != 'зеленый':
                print('Неверный порядок светофора, третий цвет должен быть "зеленый"')
                self._color_3 = input('Введите третий цвет светофора еще раз ')

            print(f'Горит {self._color_1} сигнал светофора')
            sleep(7)
            print(f'Горит {self._color_2} сигнал светофора')
            sleep(2)
            print(f'Горит {self._color_3} сигнал светофора')
            break

traffic = Traffic_lights(input('Введите первый сигнал светофора ').lower(),
                         input('Введите второй сигнал светофора ').lower(),
                         input('Введите третий сигнал светофора ').lower())
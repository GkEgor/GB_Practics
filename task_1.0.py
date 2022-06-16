from time import sleep

class Traffic_lights:

    _color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in Traffic_lights._color:
            print(f'Сигнал светофора - {Traffic_lights._color[0]}')
            sleep(7)
            print(f'Сигнал светофора - {Traffic_lights._color[1]}')
            sleep(2)
            print(f'Сигнал светофора - {Traffic_lights._color[2]}')
            break

traffic_light = Traffic_lights.running('_color')




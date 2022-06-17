from time import sleep

class Traffic_lights:

    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
            print(f'Сигнал светофора - {Traffic_lights.__color[0]}')
            sleep(7)
            print(f'Сигнал светофора - {Traffic_lights.__color[1]}')
            sleep(2)
            print(f'Сигнал светофора - {Traffic_lights.__color[2]}')


traffic_light = Traffic_lights.running('__color')



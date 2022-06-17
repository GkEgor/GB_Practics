

class Worker:
    name = input('Введите имя сотрудника: ').capitalize()
    surname = input('Введите фамилию сотрудика: ').capitalize()
    position = input('Введите должность сотрудника: ').capitalize()
    try:
        _income = {"wage": int(input('Введите оклад сотрудника (без ".", "_" и ","): ')), "bonus": int(input('Введите бонус сотрудника (без ".", "_" и ","): '))}
    except:
        print('Нужно вводить без ".", " " и ",".')
        _income = {"wage": int(input('Введите оклад сотрудника (без "." и "_"): ')),
                   "bonus": int(input('Введите бонус сотрудника (без "." и "_"): '))}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника {Worker.surname} {Worker.name}')

    def get_total_income(self):
        v_sum = 0
        for v in Worker._income.values():
            v_sum += v
        print(f'Заработная плата составляет {v_sum} рублей. Из них оклад составляет {Worker._income["wage"]} руб., а премия {Worker._income["bonus"]} руб.')

full_name = Position.get_full_name(Worker)
full_salary = Position.get_total_income(Worker)


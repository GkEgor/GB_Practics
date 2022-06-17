

class Road:
    _length = int(input('Введите длину дороги в метрах '))
    _width = int(input('Введите ширину дороги в метрах '))
    # asphalt_mass = int(input('Введите массу асфальта для покрытия одного кв. метра'))     # дополнительный атрибут с возможностью ввода массы асфальта на 1 кв метр
    # asphalt_thickness = int(input('Введите толщину слоя асфальта в см '))                 # дополнительный атрибут с возможностью выбора толщины слоя асфальта
    # total_weight = int((_length * _width * asphalt_mass * asphalt_thickness) / 1000)      # total с двумя дополнительными атрибутами
    total_weight = int((_length * _width * 25 * 1) / 1000)
    print(f'Масса асфальта при толщине слоя в 1см на всей площади дороги составит {total_weight} т.')


road_weight = Road

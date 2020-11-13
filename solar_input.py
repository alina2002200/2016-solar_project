# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star": 
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet": 
                planet = Planet()
                parse_star_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    
    star.R = float(line.split()[1])
    star.color = line.split()[2]
    star.m = float(line.split()[3])
    star.x = float(line.split()[4])
    star.y = float(line.split()[5])
    star.Vx = float(line.split()[6])
    star.Vy = float(line.split()[7])

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = float(line.split()[1])
    planet.color = line.split()[2]
    planet.m = float(line.split()[3])
    planet.x = float(line.split()[4])
    planet.y = float(line.split()[5])
    planet.Vx = float(line.split()[6])
    planet.Vy = float(line.split()[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "{0} {1} {2} {3} {4} {5} {6} {7} \n".format(obj.type.capitalize(),
                obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))

def statappend(stat_filename, planet, star, time):
    '''Добавляет статистику в данный момент в конец файла статистики.
    
    Параметры:
    
    **stat_filename** - имя файла статистики
    **planet** - планета, по которой ведётся статистика
    **star** - звезда, по которой ведётся статистика
    **time** - значение времени в текущий момент
    '''
    with open(stat_filename, 'a') as stat_file:
        stat_file.write("{0} {1} {2} \n".format(str(time), str((planet.Vx**2 + planet.Vy**2)**0.5),
            str(((star.x - planet.x)**2 + (star.y - planet.y)**2)**0.5)))

def stat_read(stat_filename):
    '''Считывает статистику из файла статистики для построения графиков.
    
    Параметры:
    
    **stat_filename** - имя файла статистики
    
    Возвращает:
    
    **time_list** - упорядоченный список значений времени
    **mod_list** - упорядоченный список значений модуля скорости
    **dist_list** - упорядоченный список значений расстояния
    '''
    time_list = []
    mod_list = []
    dist_list = []
    with open(stat_filename, 'r') as stat_file:
        for line in stat_file:
            time_list.append(float(line.split()[0]))
            mod_list.append(float(line.split()[1]))
            dist_list.append(float(line.split()[2]))
    return time_list, mod_list, dist_list

if __name__ == "__main__":
    print("This module is not for direct call!")

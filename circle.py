import math
"Импортируем библиотеку math для работы с числом пи"

def area(r):
    """
    Площадь круга

        Параметры:
            :param: r(int, float, double) радиус круга

        Возврощаемое значение
            :return: Pi * (r**2)  (float, double)Площадь круга

    Пример вызова:
        input(3)
        output(28.274333882308138)
    """
    return math.pi * r * r

def perimeter(r):
    """
    Длина окружности

        Параметры:
            :param: r(int, float, double) радиус круга

        Возврощаемое значение
            :return: 2 * Pi * r (float, double) Площадь круга

    Пример вызова:
        input(2)
        output(12.566370614359172)
    """
    return 2 * math.pi * r


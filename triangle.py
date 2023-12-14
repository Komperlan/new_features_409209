def area(a, h):
    """
    Получает площадь треугольника по стороне и высоте

    Параметры
        :param a: сторона  (int, float)
        :param h: высота (int, float)
    Возврпщает
        :return: a * h / 2 Площадь(половина произведения a на h) (int, float)


    Пример:
        a = 6
        h = 4
        :return 12
    """
    if(a <= 0 or h <= 0):
        return "Wrong input parameters"
    return a * h / 2

def perimeter(a, b, c):
    """
    Возвращает периметр треугольника по его сторонам

    Параметры
        :param a: сторона 1 (int, float)
        :param b: сторона 2 (int, float)
        :param c: сторона 3 (int, float)
    Возврощает
        :return: a + b + c перимитер сумма a, b, c  (int, float)

    Пример:
        input (1, 2, 3)
        output(6)
    """
    if(a <= 0 or a <= 0 or b <= 0):
        return "Wrong input parameters"
    return a + b + c

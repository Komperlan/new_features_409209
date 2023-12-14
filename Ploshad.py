def Ploshad(a, h):
    """
    Возврощает площадь прямоугольника

    Параметры:
        :param a: (int, float, double) длина прямоугольника
        :param h: (int, float, double) ширина прямоугольника
    Возврощаемое значение:
        :return: a * h произведение длины на ширину
    Пример вызова:
        input(2, 4)
        output(8)
    """
    if(a <= 0 or h <= 0):
        return "Wrong input parameters"
    return a*h
def perimetr(a, b):
    """
    Возвращает периметр прямоугольника

    Параметры:
        a(int, float, double) длина стороны
        b(int, float, double) длина стороны
    Возврощаемое значение:
           2*(a+b) (float, double) периметр

    Пример вызова:
        input(2, 4)
        output(12)
    """
    if(a <= 0 or b <= 0):
        return "Wrong input parameters"
    return 2*(a+b)

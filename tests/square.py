
def area(a):
    """
    приниает число и возвращает его квадрат (площадь квадарата)
    Параметры:
        :param a: (int, float, double) длина стороны
    Возврощаемое значение
        :return: area (float, double) Площадь квадрата

    Пример вызова:
        input(2)
        output(4)
    """
    if(a <= 0):
        return "Wrong input parameters"
    return a * a



def perimeter(a):
    """
    Принимает длину стороны и возвращает перимитр

    Параметры:
        :param a:(int, float, double) длина стороны
    Возврощаемое значение
        :return: (float, double) периметр квадрата

    Пример вызова:
        input(2)
        output(8)
    """
    if(a <= 0):
        return "Wrong input parameters"
    return 4 * a

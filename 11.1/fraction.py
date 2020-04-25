# КП СР-11.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from enum import Enum
from copy import copy


class Fraction:
    '''Класс Fraction реализует работу с математическими дробями'''

    class Type(Enum):
        '''Класс Type содержит сведения о типах математических дробей'''
        simple = 1
        mixed = 2
        decimal = 3

        def __str__(self):
            '''Вернуть название типа дроби'''
            return self.name.title()

        def describe(self):
            '''Вернуть описание типа дроби'''
            if self is Fraction.Type.simple:
                return 'Обыкновенная'
            elif self is Fraction.Type.mixed:
                return 'Смешанная'
            elif self is Fraction.Type.decimal:
                return 'Десятичная'

    def __init__(self, numerator, denominator,
                 negative=False, integer=0, decimal=None):
        '''Конструктор класса

        Аргументы:
            numerator (int): числитель дроби
            denominator (int): делитель дроби
            integer (int): целая часть
            decimal (float): десятичная дробь

        Исключения:
            ValueError: если использованы недопустимые значения
            TypeError: если один из аргументов не имеет тип int
        '''
        if isinstance(numerator, int):
            if isinstance(denominator, int):
                if isinstance(negative, bool):
                    if isinstance(integer, int):
                        self._negative = negative
                        if decimal is None:
                            if numerator == 0:
                                raise ValueError(
                                 'Числитель не должен быть равен нулю!')
                            if denominator == 0:
                                raise ValueError(
                                 'Знаменатель не должен быть равен нулю!')
                            self._numerator = numerator
                            self._denominator = denominator
                            if integer == 0:
                                self._type = Fraction.Type.simple
                            else:
                                self._integer = integer
                                self._type = Fraction.Type.mixed
                        elif isinstance(decimal, float):
                            self._type = Fraction.Type.decimal
                            self._decimal = decimal
                        else:
                            raise TypeError(
                             'Не могу получить десятичную дробь из {0}'
                             .format(type(decimal)))
                    else:
                        raise TypeError(
                         'Не могу получить целую часть из {0}'
                         .format(type(integer)))
                else:
                    raise TypeError(
                     'Не могу получить знак дроби из {0}'
                     .format(type(integer)))
            else:
                raise TypeError(
                 'Не могу получить знаменатель из {0}'
                 .format(type(denominator)))
        else:
            raise TypeError(
             'Не могу получить числитель из {0}'
             .format(type(numerator)))

    @staticmethod
    def from_decimal(decimal):
        '''Конструктор класса для десятичной дроби

        Аргументы:
            decimal (float/int): десятичная дробь

        Исключения:
            ValueError: если использованы недопустимые значения
            TypeError: если аргумент decimal не имеет тип float или int
        '''
        if isinstance(decimal, float):
            if decimal >= 0.0:
                negative = False
            else:
                negative = True
            return Fraction(0, 0, negative, 0, decimal)
        elif isinstance(decimal, int):
            if decimal > 0:
                negative = False
            else:
                negative = True
            return Fraction(0, 0, negative, 0, float(decimal))
        else:
            raise TypeError(
             'Не могу получить десятичную дробь из {0}'
             .format(type(decimal)))

    @staticmethod
    def from_string(fraction_string):
        '''Создать экземпляр класса из строкового значения

        Аргументы:
            fraction (str): математическая дробь

        Исключения:
            ValueError: если использованы недопустимые значения
            TypeError: если fraction_string не имеет тип str
        '''
        if isinstance(fraction_string, str):
            if '/' in fraction_string:
                slash_index = fraction_string.find('/')
                try:
                    denominator = int(fraction_string[slash_index+1:])
                except ValueError:
                    raise ValueError(
                     'Не могу получить знаменатель дроби из {0}'
                     .format(fraction_string))
                remain = fraction_string[:slash_index]
                if ' ' in remain:
                    space_index = remain.find(' ')
                    try:
                        numerator = int(remain[space_index+1:])
                    except ValueError:
                        raise ValueError(
                         'Не могу получить числитель дроби из {0}'
                         .format(fraction_string))
                    try:
                        integer = int(remain[:space_index])
                    except ValueError:
                        raise ValueError(
                         'Не могу получить целую часть дроби из {0}'
                         .format(fraction_string))
                    negative = False
                    if integer < 0:
                            negative = True
                            integer = abs(integer)
                    return Fraction(
                             numerator, denominator, negative, integer)
                else:
                    try:
                        numerator = int(remain)
                        negative = False
                        if numerator < 0:
                            negative = True
                            numerator = abs(numerator)
                        return Fraction(
                         numerator, denominator, negative)
                    except ValueError:
                        raise ValueError(
                         'Не могу получить числитель дроби из {0}'
                         .format(fraction_string))
            else:
                decimal = float(fraction_string)
                return Fraction.from_decimal(decimal)
        else:
            raise TypeError(
             'Не могу получить дробь из {0}'
             .format(type(fraction_string)))

    def __str__(self):
        '''Вернуть строковое представление класса'''
        if not self._negative:
            sign = ''
        else:
            sign = '-'
        if self._type == Fraction.Type.simple:
            return '{0}{1}/{2}'.format(sign, self._numerator, self._denominator)
        elif self._type == Fraction.Type.mixed:
            return '{0}{1} {2}/{3}'.format(
                sign, self._integer, self._numerator, self._denominator)
        elif self._type == Fraction.Type.decimal:
            if self._decimal == 0.0:
                return '0'
            else:
                return str(self._decimal)

    def get_type(self):
        '''Вернуть тип дроби'''
        return self._type

    def to_simple(self):
        '''Преобразование дроби в обыкновенную дробь'''
        if self._type == Fraction.Type.simple:
            return self
        elif self._type == Fraction.Type.mixed:
            return Fraction(
             self._integer * self._denominator + self._numerator,
             self._denominator, self._negative)
        elif self._type == Fraction.Type.decimal:
            return self.to_mixed().to_simple()

    def to_mixed(self):
        '''Преобразование дроби в смешанную дробь'''
        if self._type == Fraction.Type.mixed:
            return self
        elif self._type == Fraction.Type.simple:
            if self._numerator > 0:
                if self._numerator > self._denominator:
                    integer = self._numerator//self._denominator
                    numerator = self._numerator - integer * self._denominator
                    if numerator == 0:
                        raise ValueError(
                         'Не могу преобразовать {} в смешанную дробь.'
                         .format(self))
                    return Fraction(
                     numerator, self._denominator, self._negative, integer)
                else:
                    raise ValueError(
                     'Не могу преобразовать {} в смешанную дробь.'
                     .format(self))
            return Fraction(
             self._integer * self._numerator, self._denominator, self._negative)
        elif self._type == Fraction.Type.decimal:
            decimal_in_str = str(abs(self._decimal))
            dot_index = decimal_in_str.find('.')
            integer = int(decimal_in_str[:dot_index])
            numerator = int(decimal_in_str[dot_index+1:])
            denominator = 10 ** len(decimal_in_str[dot_index+1:])
            if numerator != 0 or integer != 0:
                return Fraction(numerator, denominator, self._negative, integer)
            else:
                raise ValueError(
                 'Не могу преобразовать {} в смешанную дробь.'
                 .format(self))

    def to_decimal(self):
        '''Преобразование дроби в десятичную дробь'''
        if self._type == Fraction.Type.decimal:
            return self
        elif self._type == Fraction.Type.simple:
            decimal = self._numerator / self._denominator
            if self._negative:
                decimal = -decimal
            return Fraction.from_decimal(decimal)
        elif self._type == Fraction.Type.mixed:
            decimal = self._integer * self._denominator + self._numerator
            decimal /= self._denominator
            if self._negative:
                decimal = -decimal
            return Fraction.from_decimal(decimal)

    def to_integer(self):
        '''Преобразовать дробь в целое число (если возможно)'''
        if self._type == Fraction.Type.simple:
            if self._numerator % self._denominator == 0:
                result = int(self._numerator / self._denominator)
                if self._negative:
                    result = -result
                return result
        elif self._type == Fraction.Type.mixed:
            return self.to_simple().to_integer()
        elif self._type == Fraction.Type.decimal:
            if float(int(self._decimal)) == self._decimal:
                return int(self._decimal)
            else:
                raise ValueError(
                 'Невозможно преобразовать в целое число дробь {}'.format(self))

    def get_integer(self):
        '''Получить целую часть дроби'''
        if self._type == Fraction.Type.simple:
            try:
                integer = self.to_mixed().get_integer()
                return integer
            except ValueError:
                return 0
        elif self._type == Fraction.Type.mixed:
            if self._negative:
                return -self._integer
            return self._integer
        elif self._type == Fraction.Type.decimal:
            return self.to_mixed().get_integer()

    def get_numerator(self):
        '''Получить числитель дроби'''
        if self._type in (Fraction.Type.simple, Fraction.Type.mixed):
            return self._numerator
        elif self._type == Fraction.Type.decimal:
            return self.to_mixed().get_numerator()

    def get_denominator(self):
        '''Получить делитель дроби'''
        if self._type == Fraction.Type.simple:
            return self._denominator
        elif self._type == Fraction.Type.mixed:
            return self._denominator
        elif self._type == Fraction.Type.decimal:
            return self.to_mixed().get_denominator()

    @staticmethod
    def __nod__(a, b):
        '''Найти наибольший общий делитель для переданных значений

        Аргументы:
            a, b (int): целые числа для нахождения их НОД

        Исключения:
            TypeError: если один из аргументов не имеет тип int
        '''
        if isinstance(a, int) and isinstance(b, int):
            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                else:
                    b = b % a
            return a+b
        else:
            raise TypeError(
             'Не могу выполнить операцию для {0} и {1}'
             .format(type(a), type(b)))

    @staticmethod
    def __nok__(a, b):
        '''Найти наименьшее общее кратное для переданных значений

        Аргументы:
            a, b (int): целые числа для нахождения их НОК

        Исключения:
            TypeError: если один из аргументов не имеет тип int
        '''
        if isinstance(a, int) and isinstance(b, int):
            return a*b // Fraction.__nod__(a, b)
        else:
            raise TypeError(
             'Не могу выполнить операцию для {0} и {1}'
             .format(type(a), type(b)))

    def reduce(self):
        '''Сократить дробь, если это возможно'''
        if self._type in (Fraction.Type.simple, Fraction.Type.mixed):
            nod = Fraction.__nod__(self._numerator, self._denominator)
            if nod == 1:
                return self
            else:
                self._numerator //= nod
                self._denominator //= nod
                return self
        elif self._type == Fraction.Type.decimal:
            raise TypeError(
             'Данная операция не применима для типа дроби {0}'
             .format(Fraction.Type.decimal))

    def __eq__(self, other):
        '''Вернуть ответ, одинаковые ли дроби

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            subtraction = self - other
            try:
                subtraction = subtraction.to_integer()
                return 0 == subtraction
            except ValueError:
                return False
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __ne__(self, other):
        '''Вернуть ответ, разные ли дроби

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            return not self == other
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __lt__(self, other):
        '''Вернуть ответ, меньше ли дробь self, чем other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            fl1 = self.to_decimal()
            fl2 = other.to_decimal()
            return 0 > fl1._decimal - fl2._decimal
        else:
            raise TypeError("Не могу выполнить операцию для {0} и {1}".
                            format(self.__class__, type(other)))

    def __gt__(self, other):
        '''Вернуть ответ, больше ли дробь self, чем other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            fl1 = self.to_decimal()
            fl2 = other.to_decimal()
            return 0 < fl1._decimal - fl2._decimal
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __le__(self, other):
        '''Вернуть ответ, дробь self меньше или равно дроби other или нет

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            fl1 = self.to_decimal()
            fl2 = other.to_decimal()
            return 0 >= fl1._decimal - fl2._decimal
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __ge__(self, other):
        '''Вернуть ответ, дробь self больше или равно дроби other или нет

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            fl1 = self.to_decimal()
            fl2 = other.to_decimal()
            return 0 <= fl1._decimal - fl2._decimal
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __add__(self, other):
        '''Создать новый объект как сумму дробей self и other
        Если типы дробей self и other отличаются, то дробь other преобразуется
         к типу дроби self

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            if self._type == Fraction.Type.simple:
                self_reduced = copy(self)
                self_reduced.reduce()
                other_reduced = copy(other)
                # Если дробь other не simple, преобразуем в нее
                if other_reduced._type == Fraction.Type.mixed:
                    other_reduced = other_reduced.to_simple()
                elif other_reduced._type == Fraction.Type.decimal:
                    if other_reduced._decimal == 0.0:
                        return self
                    else:
                        other_reduced = other_reduced.to_simple()
                other_reduced.reduce()
                # Находим НОК для знаменателей
                denominator = Fraction.__nok__(
                 self_reduced._denominator, other_reduced._denominator)
                # Приводим числители к общему знаменателю
                numerator1 = denominator // self_reduced._denominator
                numerator1 *= self_reduced._numerator
                numerator2 = denominator // other_reduced._denominator
                numerator2 *= other_reduced._numerator
                # Если дроби имеют отриц. знак,
                # переносим знаки в числитель для корректного вычисления
                if self._negative:
                    numerator1 = -(numerator1)
                if other._negative:
                    numerator2 = -(numerator2)
                numerator = numerator1 + numerator2
                # Если числитель в рез-те имеет отриц. знак,
                # переносим знак в атрибут _negative дроби
                negative = False
                if numerator < 0:
                    negative = True
                    numerator = abs(numerator)
                # Если числитель равен 0,
                # возвращаем дробь decimal со значением 0.0
                if numerator == 0:
                    return Fraction.from_decimal(0.0)
                else:
                    return Fraction(numerator, denominator, negative).reduce()
            elif self._type == Fraction.Type.mixed:
                # Для дробей mixed операция производится путем
                # преобразования дробей в тип simple
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed,
                                   Fraction.Type.decimal):
                    result = self.to_simple() + other
                    # Пытаемся преобразовать результирующую дробь в тип mixed
                    try:
                        result = result.to_mixed()
                    # Иначе оставляем дробь с типом simple
                    except ValueError:
                        pass
                    return result
            elif self._type == Fraction.Type.decimal:
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed):
                    other = other.to_decimal()
                return Fraction.from_decimal(self._decimal + other._decimal)
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __sub__(self, other):
        '''Создать новый объект как разность дробей self и other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            return self + (-other)
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __neg__(self):
        '''Создать новый объект путем отрицания переданной дроби'''
        other = copy(self)
        if other._type == Fraction.Type.decimal:
            other._decimal = -other._decimal
            other._negative = not other._negative
        elif other._type in (Fraction.Type.simple, Fraction.Type.mixed):
            other._negative = not other._negative
        return other

    def abs(self):
        '''Создать новый объект путем превращения
         переданной дроби в положительную'''
        other = copy(self)
        if other._type == Fraction.Type.decimal:
            if other._negative:
                other._decimal = -other._decimal
                other._negative = False
        elif other._type in (Fraction.Type.simple, Fraction.Type.mixed):
            other._negative = False
        return other

    def __mul__(self, other):
        '''Создать новый объект как произведение дробей self и other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            if self._type == Fraction.Type.simple:
                # Разбираемся со знаками
                negative = self._negative != other._negative
                if self._negative != other._negative:
                    negative = True
                else:
                    negative = False
                # Сокращаем дроби
                self_red = copy(self)
                self_red.reduce()
                other_red = copy(other)
                # Если дробь other не simple, преобразуем в нее
                if other_red._type == Fraction.Type.mixed:
                    other_red = other_red.to_simple()
                elif other_red._type == Fraction.Type.decimal:
                    if other_red._decimal == 0.0:
                        return other_red
                    else:
                        other_red = other_red.to_simple()
                other_red.reduce()
                numerator = self_red._numerator * other_red._numerator
                denominator = self_red._denominator * other_red._denominator
                return Fraction(numerator, denominator, negative).reduce()
            elif self._type == Fraction.Type.mixed:
                # Для дробей mixed операция производится путем
                # преобразования дробей в тип simple
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed,
                                   Fraction.Type.decimal):
                    result = self.to_simple() * other
                    # Пытаемся преобразовать результирующую дробь в тип mixed
                    try:
                        result = result.to_mixed()
                    # Иначе оставляем дробь с типом simple
                    except ValueError:
                        pass
                    return result
            elif self._type == Fraction.Type.decimal:
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed):
                    other = other.to_decimal()
                return Fraction.from_decimal(self._decimal * other._decimal)
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __truediv__(self, other):
        '''Создать новый объект путем деления дроби self на дробь other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            if self._type == Fraction.Type.simple:
                # Разбираемся со знаками
                negative = self._negative != other._negative
                if self._negative != other._negative:
                    negative = True
                else:
                    negative = False
                # Сокращаем дроби
                self_red = copy(self)
                self_red.reduce()
                other_red = copy(other)
                # Если дробь other не simple, преобразуем в нее
                if other_red._type == Fraction.Type.mixed:
                    other_red = other_red.to_simple()
                elif other_red._type == Fraction.Type.decimal:
                    if other_red._decimal == 0.0:
                        return other_red
                    else:
                        other_red = other_red.to_simple()
                other_red.reduce()
                numerator = self_red._numerator * other_red._denominator
                denominator = self_red._denominator * other_red._numerator
                return Fraction(numerator, denominator, negative).reduce()
            elif self._type == Fraction.Type.mixed:
                # Для дробей mixed операция производится путем
                # преобразования дробей в тип simple
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed,
                                   Fraction.Type.decimal):
                    result = self.to_simple() / other
                    # Пытаемся преобразовать результирующую дробь в тип mixed
                    try:
                        result = result.to_mixed()
                    # Иначе оставляем дробь с типом simple
                    except ValueError:
                        pass
                    return result
            elif self._type == Fraction.Type.decimal:
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed):
                    other = other.to_decimal()
                return Fraction.from_decimal(self._decimal / other._decimal)
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __floordiv__(self, other):
        '''Создать новый объект путем целочисленного деления дроби self на дробь other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            if self._type == Fraction.Type.simple:
                # Разбираемся со знаками
                negative = self._negative != other._negative
                if self._negative != other._negative:
                    negative = True
                else:
                    negative = False
                # Сокращаем дроби
                self_red = copy(self)
                self_red.reduce()
                other_red = copy(other)
                # Если дробь other не simple, преобразуем в нее
                if other_red._type == Fraction.Type.mixed:
                    other_red = other_red.to_simple()
                elif other_red._type == Fraction.Type.decimal:
                    if other_red._decimal == 0.0:
                        return other_red
                    else:
                        other_red = other_red.to_simple()
                other_red.reduce()
                numerator = self_red._numerator * other_red._denominator
                denominator = self_red._denominator * other_red._numerator
                result = Fraction(numerator, denominator, negative).reduce()
                return Fraction.from_decimal(result.get_integer())
            elif self._type == Fraction.Type.mixed:
                # Для дробей mixed операция производится путем
                # преобразования дробей в тип simple
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed,
                                   Fraction.Type.decimal):
                    result = self.to_simple() / other
                    # Пытаемся преобразовать результирующую дробь в тип mixed
                    try:
                        result = result.to_mixed()
                    # Иначе оставляем дробь с типом simple
                    except ValueError:
                        pass
                    return result
            elif self._type == Fraction.Type.decimal:
                if other._type in (Fraction.Type.simple, Fraction.Type.mixed):
                    other = other.to_decimal()
                return Fraction.from_decimal((self._decimal // other._decimal))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __mod__(self, other):
        '''Вернуть остаток от деления дроби self на дробь other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            return self - self // other * other
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __pow__(self, other):
        '''Создать новый объект путем возведения дроби self в степень other

        Исключения:
            TypeError: если other не имеет тип Fraction
        '''
        if isinstance(other, self.__class__):
            pass
        elif isinstance(other, int):
            if other == 0:
                return Fraction.from_decimal(1)
            result = copy(self)
            for i in range(1, other):
                result *= self
            return result
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

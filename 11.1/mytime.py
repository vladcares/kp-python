# КП СР-11.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com


class Time:
    '''Класс Time реализует работу с переменными, содержащими время'''

    MIN_VALUE = 0
    SEC_MINUTE_MAX = 59
    HOUR_MAX = 23

    def __init__(self, hour, minute, second):
        '''Конструктор класса

        Аргументы:
            hour (int): час
            minute (int): минута
            second (int): секунда

        Исключения:
            ValueError: если использованы недопустимые значения
            TypeError: если один из аргументов не имеет тип int
        '''
        if isinstance(hour, int):
            if isinstance(minute, int):
                if isinstance(second, int):
                    if Time.check_hour(hour):
                        self._hour = hour
                    else:
                        raise ValueError(
                         'Значение часа должно быть в пределах {0} - {1}'
                         .format(Time.MIN_VALUE, Time.HOUR_MAX))
                    if Time.check_minute(minute):
                        self._minute = minute
                    else:
                        raise ValueError(
                         'Значение минуты должно быть в пределах {0} - {1}'
                         .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
                    if Time.check_second(second):
                        self._second = second
                    else:
                        raise ValueError(
                         'Значение секунды должно быть в пределах {0} - {1}'
                         .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
                else:
                    raise TypeError(
                     "Не могу получить значение секунды из {0}"
                     .format(type(second)))
            else:
                raise TypeError(
                 "Не могу получить значение минуты из {0}"
                 .format(type(minute)))
        else:
            raise TypeError(
             "Не могу получить значение часа из {0}"
             .format(type(hour)))

    def __eq__(self, other):
        '''Вернуть ответ, одинаковое ли время

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            if self._hour != other._hour:
                return False
            if self._minute != other._minute:
                return False
            if self._second != other._second:
                return False
            return True
        elif isinstance(other, str):
            return Time.__eq__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __ne__(self, other):
        '''Вернуть ответ, разное ли время

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            return not (self == other)
        elif isinstance(other, str):
            return not (self == Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __lt__(self, other):
        '''Вернуть ответ, меньше ли время self, чем other

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            if self._hour > other._hour:
                return False
            elif self._hour < other._hour:
                return True
            else:
                if self._minute > other._minute:
                    return False
                elif self._minute < other._minute:
                    return True
                else:
                    if self._second >= other._second:
                        return False
                    else:
                        return True
        elif isinstance(other, str):
            return Time.__lt__(self, Time.from_string(other))
        else:
            raise TypeError("Не могу выполнить операцию для {0} и {1}".
                            format(self.__class__, type(other)))

    def __gt__(self, other):
        '''Вернуть ответ, больше ли время self, чем other

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            if self._hour < other._hour:
                return False
            elif self._hour > other._hour:
                return True
            else:
                if self._minute < other._minute:
                    return False
                elif self._minute > other._minute:
                    return True
                else:
                    if self._second <= other._second:
                        return False
                    else:
                        return True
        elif isinstance(other, str):
            return Time.__gt__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __le__(self, other):
        '''Вернуть ответ, время self меньше или равно времени other или нет

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            if self._hour > other._hour:
                return False
            elif self._hour < other._hour:
                return True
            else:
                if self._minute > other._minute:
                    return False
                elif self._minute < other._minute:
                    return True
                else:
                    if self._second <= other._second:
                        return True
                    else:
                        return False
        elif isinstance(other, str):
            return Time.__le__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __ge__(self, other):
        '''Вернуть ответ, время self больше или равно времени other или нет

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            if self._hour < other._hour:
                return False
            elif self._hour > other._hour:
                return True
            else:
                if self._minute < other._minute:
                    return False
                elif self._minute > other._minute:
                    return True
                else:
                    if self._second >= other._second:
                        return True
                    else:
                        return False
        elif isinstance(other, str):
            return Time.__ge__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __add__(self, other):
        '''Создать новый объект как сумму времени self и other

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            # Складываем значения часов
            hour = self._hour + other._hour
            # Складываем значения минут
            minute = self._minute + other._minute
            # Складываем значения секунд
            second = self._second + other._second

            # Если значение превысило макс. знач., увеличиваем знач. минуты на 1
            if second > Time.SEC_MINUTE_MAX:
                second -= 60
                minute += 1

            # Если значение превысило макс. знач., увеличиваем знач. часа на 1
            if minute > Time.SEC_MINUTE_MAX:
                minute -= 60
                hour += 1

            if hour > Time.HOUR_MAX:
                hour -= 24

            return Time(hour, minute, second)
        elif isinstance(other, str):
            return Time.__add__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __sub__(self, other):
        '''Создать новый объект как разность времени self и other

        Исключения:
            TypeError: если other не имеет тип Time или str
        '''
        if isinstance(other, self.__class__):
            # Вычитаем значения часов
            hour = self._hour - other._hour
            # Вычитаем значения минут
            minute = self._minute - other._minute
            # Вычитаем значения секунд
            second = self._second - other._second

            # Если значение меньше мин. знач., уменьшаем знач. минуты на 1
            if second < Time.MIN_VALUE:
                second += 60
                minute -= 1

            # Если значение меньше мин. знач., уменьшаем знач. часа на 1
            if minute < Time.MIN_VALUE:
                minute += 60
                hour -= 1

            if hour < Time.MIN_VALUE:
                hour += 24

            return Time(hour, minute, second)
        elif isinstance(other, str):
            return Time.__sub__(self, Time.from_string(other))
        else:
            raise TypeError(
             "Не могу выполнить операцию для {0} и {1}"
             .format(self.__class__, type(other)))

    def __str__(self):
        '''Вернуть строковое представление класса'''
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

    @staticmethod
    def from_string(time_string):
        '''Создать экземпляр класса из строкового значения

        Аргументы:
            time_string (str): время в формате hh:mm:ss

        Исключения:
            ValueError: если использованы недопустимые значения
            TypeError: если time_string не имеет тип str
        '''
        if isinstance(time_string, str):
            if (len(time_string) != 8):
                raise ValueError(
                 'Значение времени должно содержать 8 символов!')
            if (time_string.count(":") != 2):
                raise ValueError(
                 'Значение времени должно содержать 2 разделительных ":"!')
            hour_string = time_string[:2]
            minute_string = time_string[3:5]
            second_string = time_string[6:8]
            hour = int(hour_string)
            minute = int(minute_string)
            second = int(second_string)
            if Time.check_hour(hour):
                if Time.check_minute(minute):
                    if Time.check_second(second):
                        return Time(hour, minute, second)
                    else:
                        raise ValueError(
                         'Значение секунды должно быть в пределах {0} - {1}'
                         .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
                else:
                    raise ValueError(
                     'Значение минуты должно быть в пределах {0} - {1}'
                     .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
            else:
                raise ValueError(
                 'Значение часа должно быть в пределах {0} - {1}'
                 .format(Time.MIN_VALUE, Time.HOUR_MAX))
        else:
            raise TypeError(
             "Не могу получить значение времени из {0}"
             .format(type(hour)))

    @staticmethod
    def check_hour(hour):
        '''Проверка значения часа

        Аргументы:
            hour (int): час

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        valid = True
        if not Time.MIN_VALUE <= hour <= Time.HOUR_MAX:
            valid = False
        return valid

    @staticmethod
    def check_minute(minute):
        '''Проверка значения минуты

        Аргументы:
            minute (int): минута

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        valid = True
        if not Time.MIN_VALUE <= minute <= Time.SEC_MINUTE_MAX:
            valid = False
        return valid

    @staticmethod
    def check_second(second):
        '''Проверка значения секунды

        Аргументы:
            second (int): секунда

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        valid = True
        if not Time.MIN_VALUE <= second <= Time.SEC_MINUTE_MAX:
            valid = False
        return valid

    def set_hour(self, hour):
        '''Установить час

        Аргументы:
            hour (int): час

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        if isinstance(hour, int):
            if Time.check_hour(hour):
                self._hour = hour
            else:
                raise ValueError(
                 'Значение часа должно быть в пределах {0} - {1}'
                 .format(Time.MIN_VALUE, Time.HOUR_MAX))
        else:
            raise TypeError(
             "Не могу получить значение часа из {0}"
             .format(type(hour)))

    def set_minute(self, minute):
        '''Установить минуту

        Аргументы:
            minute (int): час

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        if isinstance(minute, int):
            if Time.check_minute(minute):
                self._minute = minute
            else:
                raise ValueError(
                 'Значение минуты должно быть в пределах {0} - {1}'
                 .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
        else:
            raise TypeError(
             "Не могу получить значение минуты из {0}"
             .format(type(minute)))

    def set_second(self, second):
        '''Установить секунду

        Аргументы:
            hour (int): секунда

        Исключения:
            ValueError: если использовано недопустимое значение
            TypeError: если аргумент не имеет тип int
        '''
        if isinstance(second, int):
            if Time.check_second(second):
                self._second = second
            else:
                raise ValueError(
                 'Значение секунды должно быть в пределах {0} - {1}'
                 .format(Time.MIN_VALUE, Time.SEC_MINUTE_MAX))
        else:
            raise TypeError(
             "Не могу получить значение секуды из {0}"
             .format(type(second)))

    def get_hour(self):
        '''Получить значение часа
        '''
        return self._hour

    def get_minute(self):
        '''Получить значение минуты
        '''
        return self._minute

    def get_second(self):
        '''Получить значение секунды
        '''
        return self._second

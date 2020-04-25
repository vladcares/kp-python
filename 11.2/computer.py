# КП СР-11.2
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from enum import Enum
import json


class Computer:
    """ Базовый класс для всех компьютерных устройств """

    UNDEFINED = 'не указано'

    def __init__(self, name, manufacturer, model):
        """Конструктор класса
        Аргументы:
            name (str): имя компьютера (псевдоним)
            manufacturer (str): производитель
            model (str): модель
        """
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        # Характеристики пока не указаны
        self._builtin_memory = Computer.UNDEFINED
        self._ram_memory = Computer.UNDEFINED

    def __str__(self):
        return '{1}{0}Компьютер "{2}"{0}{1}{0}Производитель: {3}{0}' \
               'Модель: {4}{0}{1}{0}'.format(
                '\r\n', '-'*30, self.name, self.manufacturer, self.model)

    @property
    def builtin_memory(self):
        """Объём встроенной памяти"""
        return self._builtin_memory

    @builtin_memory.setter
    def builtin_memory(self, value):
        assert isinstance(value, int), ('Значение объёма встроенной памяти '
                                        'должно быть числом')
        self._builtin_memory = value

    @property
    def ram_memory(self):
        """Объём оперативной памяти"""
        return self._ram_memory

    @ram_memory.setter
    def ram_memory(self, value):
        assert isinstance(value, int), ('Значение объёма оперативной памяти '
                                        'должно быть числом')
        self._ram_memory = value

    def print_specifications(self):
        """Печать характеристик"""
        spec_str = '{2}{0}Компьютер "{1}"{0}{2}{0}'.format(
            '\r\n', self.name, '-'*30)
        spec_str += 'Характеристики\r\n'
        spec_str += 'Объём встроенной памяти: {}'.format(
            self.builtin_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Объём оперативной памяти: {}'.format(
            self.ram_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += '-'*30 + '\r\n'
        print(spec_str)

    def save(self, filename):
        """Сохранение содержимого объекта в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        data = {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "builtin_memory": self._builtin_memory,
            "ram_memory": self._ram_memory
        }
        json_data = json.dumps(data, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка содержимого объекта из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        enough_data = True
        if "name" in json_data:
            name = json_data["name"]
        else:
            enough_data = False
        if "manufacturer" in json_data:
            manufacturer = json_data["manufacturer"]
        else:
            enough_data = False
        if "model" in json_data:
            model = json_data["model"]
        else:
            enough_data = False

        if not enough_data:
            return None
        computer = Computer(name, manufacturer, model)
        if "builtin_memory" in json_data:
            computer._builtin_memory = json_data["builtin_memory"]
        if "ram_memory" in json_data:
            computer._ram_memory = json_data["ram_memory"]
        return computer


class Smartphone(Computer):
    """ Класс объектов 'смартфон' """

    class OperatingSystem:
        """Класс OperatingSystem содержит сведения об операционной системе"""

        class Type(Enum):
            """Класс OperatingSystem.Type содержит типы операционных систем"""
            Android = 1
            iOS = 2
            WindowsPhone = 3
            BlackBerry = 4
            SailfishOS = 5
            Tizen = 6
            UbuntuTouch = 7

            def __str__(self):
                return self.name

        def __init__(self, os_type, os_version):
            """Конструктор класса
            Аргументы:
                os_type (OperatingSystem.Type): тип ОС
                os_version (str): версия ОС
            """
            self.os_type = os_type
            self.os_version = os_version

        def __str__(self):
            return '{} {}'.format(self.os_type, self.os_version)

    def __init__(self, name, manufacturer, model, mobile_os):
        """Конструктор класса
        Аргументы:
            name (str): имя смартфона (псевдоним)
            manufacturer (str): производитель
            model (str): модель
            mobile_os (OperatingSystem): мобильная ОС
        """
        Computer.__init__(self, name, manufacturer, model)
        self.mobile_os = mobile_os
        # Характеристики пока не указаны
        self._sim_type = Computer.UNDEFINED
        self._sim_count = Computer.UNDEFINED

    def __str__(self):
        return '{1}{0}Смартфон "{2}"{0}{1}{0}Производитель: {3}{0}' \
               'Модель: {4}{0}ОС: {5}{0}{1}{0}'.format(
                '\r\n', '-'*30, self.name, self.manufacturer, self.model,
                self.mobile_os)

    @property
    def sim_type(self):
        """Тип SIM-карты"""
        return self._sim_type

    @sim_type.setter
    def sim_type(self, value):
        self._sim_type = value

    @property
    def sim_count(self):
        """Количество слотов для SIM-карт"""
        return self._sim_count

    @sim_count.setter
    def sim_count(self, value):
        assert isinstance(value, int), ('Значение кол-ва слотов для SIM-карт '
                                        'должно быть числом')
        self._sim_count = value

    def print_specifications(self):
        """Печать характеристик"""
        spec_str = '{2}{0}Смартфон "{1}"{0}{2}{0}'.format(
            '\r\n', self.name, '-'*30)
        spec_str += 'Характеристики\r\n'
        spec_str += 'Объём встроенной памяти: {}'.format(
            self.builtin_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Объём оперативной памяти: {}'.format(
            self.ram_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Тип SIM-карты: {}\r\n'.format(self.sim_type)
        spec_str += 'Количество SIM-карт: {}\r\n'.format(self.sim_count)
        spec_str += '-'*30 + '\r\n'
        print(spec_str)

    def save(self, filename):
        """Сохранение содержимого объекта в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        mobile_os = self.mobile_os
        data = {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "mobile_os": {
                "os_type": mobile_os.os_type.name,
                "os_version": mobile_os.os_version
            },
            "builtin_memory": self._builtin_memory,
            "ram_memory": self._ram_memory,
            "sim_type": self._sim_type,
            "sim_count": self._sim_count
        }
        json_data = json.dumps(data, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка содержимого объекта из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        enough_data = True
        if "name" in json_data:
            name = json_data["name"]
        else:
            enough_data = False
        if "manufacturer" in json_data:
            manufacturer = json_data["manufacturer"]
        else:
            enough_data = False
        if "model" in json_data:
            model = json_data["model"]
        else:
            enough_data = False
        if "mobile_os" in json_data:
            mobile_os_json = json_data["mobile_os"]
            if "os_type" in mobile_os_json and "os_version" in mobile_os_json:
                os_members = Smartphone.OperatingSystem.Type.__members__
                os_type_dict = {name: member
                                for name, member in os_members.items()}
                if mobile_os_json["os_type"] in os_type_dict:
                    os_type = os_type_dict[mobile_os_json["os_type"]]
                    mobile_os = Smartphone.OperatingSystem(
                        os_type, mobile_os_json["os_version"])
                else:
                    enough_data = False
            else:
                enough_data = False
        else:
            enough_data = False

        if not enough_data:
            return None
        smartphone = Smartphone(name, manufacturer, model, mobile_os)
        if "builtin_memory" in json_data:
            smartphone._builtin_memory = json_data["builtin_memory"]
        if "ram_memory" in json_data:
            smartphone._ram_memory = json_data["ram_memory"]
        if "sim_type" in json_data:
            smartphone._sim_type = json_data["sim_type"]
        if "sim_count" in json_data:
            smartphone._sim_count = json_data["sim_count"]
        return smartphone


class PersonalComputer(Computer):
    """ Класс объектов 'Персональный компьютер' """

    class OperatingSystem:
        """Класс OperatingSystem содержит сведения об операционной системе"""

        class Type(Enum):
            """Класс OperatingSystem.Type содержит типы операционных систем"""
            MicrosoftWindows = 0
            OSX = 1
            Linux = 2
            Solaris = 3
            FreeBSD = 4
            Android = 5
            FirefoxOS = 6

            def __str__(self):
                if self.value == 0:
                    return 'Microsoft Windows'
                elif self.value == 1:
                    return 'OS X'
                elif self.value == 6:
                    return 'Firefox X'
                else:
                    return self.name

        def __init__(self, os_type, os_version):
            """Конструктор класса
            Аргументы:
                os_type (OperatingSystem.Type): тип ОС
                os_version (str): версия ОС
            """
            self.os_type = os_type
            self.os_version = os_version

        def __str__(self):
            return '{} {}'.format(self.os_type, self.os_version)

    def __init__(self, name, manufacturer, model, pc_os):
        """Конструктор класса
        Аргументы:
            name (str): имя ПК (псевдоним)
            manufacturer (str): производитель
            model (str): модель
            pc_os (OperatingSystem): мобильная ОС
        """
        Computer.__init__(self, name, manufacturer, model)
        self.pc_os = pc_os
        # Характеристики пока не указаны
        self._builtin_memory = Computer.UNDEFINED
        self._ram_memory = Computer.UNDEFINED

    def save(self, filename):
        """Сохранение содержимого объекта в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        pc_os = self.pc_os
        data = {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "pc_os": {
                "os_type": pc_os.os_type.name,
                "os_version": pc_os.os_version
            },
            "builtin_memory": self._builtin_memory,
            "ram_memory": self._ram_memory
        }
        json_data = json.dumps(data, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка содержимого объекта из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        enough_data = True
        if "name" in json_data:
            name = json_data["name"]
        else:
            enough_data = False
        if "manufacturer" in json_data:
            manufacturer = json_data["manufacturer"]
        else:
            enough_data = False
        if "model" in json_data:
            model = json_data["model"]
        else:
            enough_data = False
        if "pc_os" in json_data:
            pc_os_json = json_data["pc_os"]
            if "os_type" in pc_os_json and "os_version" in pc_os_json:
                os_members = PersonalComputer.OperatingSystem.Type.__members__
                os_type_dict = {name: member
                                for name, member in os_members.items()}
                if pc_os_json["os_type"] in os_type_dict:
                    os_type = os_type_dict[pc_os_json["os_type"]]
                    pc_os = PersonalComputer.OperatingSystem(
                        os_type, pc_os_json["os_version"])
                else:
                    enough_data = False
            else:
                enough_data = False
        else:
            enough_data = False

        if not enough_data:
            return None
        pc = PersonalComputer(name, manufacturer, model, pc_os)
        if "builtin_memory" in json_data:
            pc._builtin_memory = json_data["builtin_memory"]
        if "ram_memory" in json_data:
            pc._ram_memory = json_data["ram_memory"]
        return pc


class DesktopComputer(PersonalComputer):
    """ Класс объектов 'Настольный компьютер' """

    def __init__(self, name, manufacturer, model, pc_os):
        """Конструктор класса
        Аргументы:
            name (str): имя ПК (псевдоним)
            manufacturer (str): производитель
            model (str): модель
            pc_os (OperatingSystem): мобильная ОС
        """
        PersonalComputer.__init__(self, name, manufacturer, model, pc_os)
        # Характеристики пока не указаны
        self._form_factor = Computer.UNDEFINED

    def __str__(self):
        return '{1}{0}Настольный компьютер "{2}"{0}{1}{0}' \
               'Производитель: {3}{0}Модель: {4}{0}{1}{0}'.format(
                '\r\n', '-'*30, self.name, self.manufacturer, self.model)

    @property
    def form_factor(self):
        """Форм-фактор"""
        return self._form_factor

    @form_factor.setter
    def form_factor(self, value):
        self._form_factor = value

    def print_specifications(self):
        """Печать характеристик"""
        spec_str = '{2}{0}Компьютер "{1}"{0}{2}{0}'.format(
            '\r\n', self.name, '-'*30)
        spec_str += 'Характеристики\r\n'
        spec_str += 'Объём встроенной памяти: {}'.format(
            self.builtin_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Объём оперативной памяти: {}'.format(
            self.ram_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Форм-фактор корпуса: {}\r\n'.format(
            self.form_factor)
        spec_str += '-'*30 + '\r\n'
        print(spec_str)

    def save(self, filename):
        """Сохранение содержимого объекта в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        pc_os = self.pc_os
        data = {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "pc_os": {
                "os_type": pc_os.os_type.name,
                "os_version": pc_os.os_version
            },
            "builtin_memory": self._builtin_memory,
            "ram_memory": self._ram_memory,
            "form_factor": self._form_factor
        }
        json_data = json.dumps(data, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка содержимого объекта из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        enough_data = True
        if "name" in json_data:
            name = json_data["name"]
        else:
            enough_data = False
        if "manufacturer" in json_data:
            manufacturer = json_data["manufacturer"]
        else:
            enough_data = False
        if "model" in json_data:
            model = json_data["model"]
        else:
            enough_data = False
        if "pc_os" in json_data:
            pc_os_json = json_data["pc_os"]
            if "os_type" in pc_os_json and "os_version" in pc_os_json:
                os_members = PersonalComputer.OperatingSystem.Type.__members__
                os_type_dict = {name: member
                                for name, member in os_members.items()}
                if pc_os_json["os_type"] in os_type_dict:
                    os_type = os_type_dict[pc_os_json["os_type"]]
                    pc_os = PersonalComputer.OperatingSystem(
                        os_type, pc_os_json["os_version"])
                else:
                    enough_data = False
            else:
                enough_data = False
        else:
            enough_data = False

        if not enough_data:
            return None
        pc = PersonalComputer(name, manufacturer, model, pc_os)
        if "builtin_memory" in json_data:
            pc._builtin_memory = json_data["builtin_memory"]
        if "ram_memory" in json_data:
            pc._ram_memory = json_data["ram_memory"]
        if "form_factor" in json_data:
            pc._form_factor = json_data["form_factor"]
        return pc


class Laptop(PersonalComputer):
    """ Класс объектов 'Ноутбук' """

    def __init__(self, name, manufacturer, model, pc_os):
        """Конструктор класса
        Аргументы:
            name (str): имя ПК (псевдоним)
            pc_os (OperatingSystem): мобильная ОС
        """
        PersonalComputer.__init__(self, name, manufacturer, model, pc_os)
        # Характеристики пока не указаны
        self._laptop_type = Computer.UNDEFINED

    def __str__(self):
        return '{1}{0}Ноутбук "{2}"{0}{1}{0}Производитель: {3}{0}' \
               'Модель: {4}{0}{1}{0}'.format(
                '\r\n', '-'*30, self.name, self.manufacturer, self.model)

    @property
    def laptop_type(self):
        """Тип ноутбука"""
        return self._laptop_type

    @laptop_type.setter
    def laptop_type(self, value):
        self._laptop_type = value

    def print_specifications(self):
        """Печать характеристик"""
        spec_str = '{2}{0}Компьютер "{1}"{0}{2}{0}'.format(
            '\r\n', self.name, '-'*30)
        spec_str += 'Характеристики\r\n'
        spec_str += 'Тип: {}\r\n'.format(
            self.laptop_type)
        spec_str += 'Объём встроенной памяти: {}'.format(
            self.builtin_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Объём оперативной памяти: {}'.format(
            self.ram_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += '-'*30 + '\r\n'
        print(spec_str)

    def save(self, filename):
        """Сохранение содержимого объекта в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        pc_os = self.pc_os
        data = {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "pc_os": {
                "os_type": pc_os.os_type.name,
                "os_version": pc_os.os_version
            },
            "builtin_memory": self._builtin_memory,
            "ram_memory": self._ram_memory,
            "laptop_type": self._laptop_type
        }
        json_data = json.dumps(data, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка содержимого объекта из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        enough_data = True
        if "name" in json_data:
            name = json_data["name"]
        else:
            enough_data = False
        if "manufacturer" in json_data:
            manufacturer = json_data["manufacturer"]
        else:
            enough_data = False
        if "model" in json_data:
            model = json_data["model"]
        else:
            enough_data = False
        if "pc_os" in json_data:
            pc_os_json = json_data["pc_os"]
            if "os_type" in pc_os_json and "os_version" in pc_os_json:
                os_members = PersonalComputer.OperatingSystem.Type.__members__
                os_type_dict = {name: member
                                for name, member in os_members.items()}
                if pc_os_json["os_type"] in os_type_dict:
                    os_type = os_type_dict[pc_os_json["os_type"]]
                    pc_os = PersonalComputer.OperatingSystem(
                        os_type, pc_os_json["os_version"])
                else:
                    enough_data = False
            else:
                enough_data = False
        else:
            enough_data = False

        if not enough_data:
            return None
        pc = PersonalComputer(name, manufacturer, model, pc_os)
        if "builtin_memory" in json_data:
            pc._builtin_memory = json_data["builtin_memory"]
        if "ram_memory" in json_data:
            pc._ram_memory = json_data["ram_memory"]
        if "laptop_type" in json_data:
            pc._laptop_type = json_data["laptop_type"]
        return pc


class Tablet(PersonalComputer):
    """ Класс объектов 'Планшетный компьютер' """

    def __str__(self):
        return '{1}{0}Планшетный компьютер "{2}"{0}{1}{0}' \
               'Производитель: {3}{0}Модель: {4}{0}{1}{0}'.format(
                '\r\n', '-'*30, self.name, self.manufacturer, self.model)

    def print_specifications(self):
        """Печать характеристик"""
        spec_str = '{2}{0}Планшетный компьютер "{1}"{0}{2}{0}'.format(
            '\r\n', self.name, '-'*30)
        spec_str += 'Характеристики\r\n'
        spec_str += 'Объём встроенной памяти: {}'.format(
            self.builtin_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += 'Объём оперативной памяти: {}'.format(
            self.ram_memory)
        if self.builtin_memory != Computer.UNDEFINED:
            spec_str += ' ГБ'
        spec_str += '\r\n'
        spec_str += '-'*30 + '\r\n'
        print(spec_str)

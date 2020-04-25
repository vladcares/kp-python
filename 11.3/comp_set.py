# КП СР-11.3
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

import json
from computer import Computer


class CompSet:
    """ Класс-контейнер для набора объектов класса Computer
    и его наследуемых классов """

    def __init__(self):
        """ Конструктор класса """
        self.__set = []

    def __str__(self):
        """ Строковое представление класса """
        set_str = ''
        for comp in self.__set:
            set_str += comp.name + ', '
        set_str = set_str = '[' + set_str[:-2] + ']'
        return set_str

    def add(self, comp):
        """ Добавление объекта """
        self.__set.append(comp)

    def remove(self, comp):
        """ Удаление объекта """
        self.__set.remove(comp)

    def __getitem__(self, k):
        """ Доступ по индексу или срезу """
        if isinstance(k, slice):
            new_comp_set = CompSet()
            for i in range(*k.indices(len(self))):
                new_comp_set.add(self[i])
            return new_comp_set
        elif isinstance(k, int):
            return self.__set[k]
        else:
            raise(TypeError, "Invalid argument type")

    def __setitem__(self, k, v):
        """ Присвоение по индексу или срезу """
        if isinstance(k, slice):
            ii = 0
            for i in range(*k.indices(len(self))):
                self[i] = v[ii]
                ii += 1
        elif isinstance(k, int):
            self.__set[k] = v
        else:
            raise(TypeError, "Invalid argument type")

    def __delitem__(self, k):
        """ Удаление по индексу или срезу """
        if isinstance(k, slice):
            # Удаляем элементы с конца, чтобы индексы не смещались
            for i in reversed(range(*k.indices(len(self)))):
                del self[i]
        elif isinstance(k, int):
            del self.__set[k]
        else:
            raise(TypeError, "Invalid argument type")

    def __len__(self):
        """ Количество элементов в наборе """
        return len(self.__set)

    def __add__(self, other):
        """ Конкатенация """
        new_comp_set = CompSet()
        for comp in self.__set:
            new_comp_set.add(comp)
        for comp in other.__set:
            new_comp_set.add(comp)
        return new_comp_set

    def save(self, filename):
        """Сохранение набора в файл в формате JSON
        Аргументы:
            filename (str): имя файла
        """
        data_set = []
        for comp in self.__set:
            data_set.append(comp.get_dict())
        json_data = json.dumps(data_set, ensure_ascii=False)
        with open(filename, 'w') as json_file:
            json_file.write(json_data)

    @classmethod
    def load(cls, filename):
        """Загрузка набора из файла формата JSON
        Аргументы:
            filename (str): имя файла
        """
        with open(filename) as json_file:
            json_data = json.load(json_file)
        comp_set = CompSet()
        for comp_data in json_data:
            comp = Computer.from_dict(comp_data)
            if comp:
                comp_set.add(comp)
        return comp_set

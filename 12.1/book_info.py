# КП СР-12.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

import re


class BookInfo:
    """ Класс, получающий и хранящий информацию о книге """

    NOT_FOUND = 'информация не найдена'
    AUTHOR_REG = 'Author" attribute_no="252\|(?P<author>[а-яА-ЯёЁ\-\s.]+)\*"'
    TITLE_REG = 'Title">(?P<title>[а-яА-ЯёЁ\-\s:]+)<'
    PUBLISHER_REG = 'Publisher" attribute_no="27\|' \
                    '(?P<publisher>[а-яА-ЯёЁ\-\s:]+)\*"'
    YEAR_REG = 'Year">.*(?P<year>\d{4})'
    DESCRIPTION_REG = 'Description">(?P<description>' \
                      '.*[\n]*.*[\n]*.*[\n]*.*)<\/span>'
    PRICE_REG = 'Price"><b>Цена</b>: (?P<price>\d* р.)'

    def __init__(self, source_file, output_file):
        """ Конструктор класса
        Аргументы:
            source_file (str) - имя файла-источника данных о книге
            output_file (str) - имя выходного файла с информацией о книге
        """
        self.source_file = source_file
        self.output_file = output_file
        self.source_data = ''
        # Значения по умолчанию
        self.author = BookInfo.NOT_FOUND
        self.title = BookInfo.NOT_FOUND
        self.publisher = BookInfo.NOT_FOUND
        self.year = BookInfo.NOT_FOUND
        self.description = BookInfo.NOT_FOUND
        self.price = BookInfo.NOT_FOUND

    def __str__(self):
        """ Строковое представление класса """
        book_info_str = 'Информация о книге' + '\r\n'
        book_info_str += 'Автор: ' + self.author + '\r\n'
        book_info_str += 'Название: ' + self.title + '\r\n'
        book_info_str += 'Издательство: ' + self.publisher + '\r\n'
        book_info_str += 'Год издания: ' + self.year + '\r\n'
        book_info_str += 'Цена: ' + self.price + '\r\n'
        book_info_str += 'Описание:' + '\r\n' + self.description
        return book_info_str

    def get_source_data(self):
        """ Получение данных из файла источника """
        with open(self.source_file) as source_file:
            self.source_data = source_file.read()
        return bool(self.source_data)

    def get_book_info(self):
        """ Получение информации о книге """
        self.get_author()
        self.get_title()
        self.get_publisher()
        self.get_year()
        self.get_description()
        self.get_price()

    def get_author(self):
        """ Получение информации об авторе """
        match = re.search(BookInfo.AUTHOR_REG, self.source_data)
        if match:
            self.author = match.group('author')

    def get_title(self):
        """ Получение информации о названии """
        match = re.search(BookInfo.TITLE_REG, self.source_data)
        if match:
            self.title = match.group('title')

    def get_publisher(self):
        """ Получение информации об издательстве """
        match = re.search(BookInfo.PUBLISHER_REG, self.source_data)
        if match:
            self.publisher = match.group('publisher')

    def get_year(self):
        """ Получение информации о годе издания """
        match = re.search(BookInfo.YEAR_REG, self.source_data)
        if match:
            self.year = match.group('year')

    def get_description(self):
        """ Получение информации об описании """
        match = re.search(BookInfo.DESCRIPTION_REG, self.source_data)
        if match:
            self.description = match.group('description')

    def get_price(self):
        """ Получение информации о цене """
        match = re.search(BookInfo.PRICE_REG, self.source_data)
        if match:
            self.price = match.group('price')

    def write_book_info(self):
        """ Запись информации о книге в файл """
        with open(self.output_file, 'wb') as output_file:
            output_file.write(str(self).encode('utf-8'))

# КП СР-12.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from book_info import BookInfo

import sys

if len(sys.argv) == 3:
    book_info = BookInfo(sys.argv[1], sys.argv[2])
    if (book_info.get_source_data()):
        book_info.get_book_info()
        book_info.write_book_info()
        print('Выполнена запись информации о книге в выходной файл')
    else:
        print('Не удалось получить данные из файла-источника')
else:
    print('Приложение было запущено с некорректными параметрами')

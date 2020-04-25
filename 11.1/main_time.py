# КП СР-11.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from mytime import Time

# Конструкторы
time_object1 = Time(15, 20, 35)
time_object2 = Time.from_string('19:58:45')

# Вывод
print('Время 1: ', time_object1)
print('Время 2: ', time_object2)
print()

# Установка отдельных значений времени
print('Для "Время 1" устанавливаем 12 часов...')
time_object1.set_hour(12)
print('Время 1: ', time_object1)

print('Для "Время 1" устанавливаем 30 минут...')
time_object1.set_minute(30)
print('Время 1: ', time_object1)

print('Для "Время 1" устанавливаем 55 секунд...')
time_object1.set_second(55)
print('Время 1: ', time_object1)
print()

# Получение отдельных значений времени
print('Получаем часы у "Время 2": ', str(time_object2.get_hour()))
print('Получаем минуты у "Время 2": ', str(time_object2.get_minute()))
print('Получаем секунды у "Время 2": ', str(time_object2.get_second()))
print()

# Операции сложения и вычитания времени
print('Сложим "Время 1" и "Время 2":')
print(time_object1)
print('+'*8)
print(time_object2)
print('='*8)
print(time_object1+time_object2)
print()

print('Сложим "Время 1" и "11:29:05":')
print(time_object1)
print('+'*8)
print("11:29:05")
print('='*8)
print(time_object1+'11:29:05')
print()

print('Из "Время 1" вычтим "Время 2":')
print(time_object1)
print('-'*8)
print(time_object2)
print('='*8)
print(time_object1-time_object2)
print()

print('Из "Время 1" вычтим "11:29:05":')
print(time_object1)
print('-'*8)
print('11:29:05')
print('='*8)
print(time_object1-'11:29:05')
print()

# Выполняем операции сравнения времени
print('Время 1: ', time_object1)
print('Время 2: ', time_object2)
print()

print('Сравним время:')
print('"Время 1" == "Время 2": ', time_object1 == time_object2)
print('"Время 2" == "19:58:45": ', time_object2 == '19:58:45')
print('"Время 1" != "Время 2": ', time_object1 != time_object2)
print('"Время 2" != "19:58:45": ', time_object2 != '19:58:45')
print()

print('"Время 1" < "Время 2": ', time_object1 < time_object2)
print('"Время 2" < "19:58:45": ', time_object2 < '19:58:45')
print()

print('"Время 1" > "Время 2": ', time_object1 > time_object2)
print('"Время 2" > "19:58:45": ', time_object2 > '19:58:45')
print()

print('"Время 1" <= "Время 2": ', time_object1 < time_object2)
print('"Время 2" <= "19:58:45": ', time_object2 < '19:58:45')
print()

print('"Время 1" >= "Время 2": ', time_object1 >= time_object2)
print('"Время 2" >= "19:58:45": ', time_object2 >= '19:58:45')
print()

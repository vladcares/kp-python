# КП СР-11.3
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from computer import Computer
from computer import Smartphone
from computer import PersonalComputer
from computer import DesktopComputer
from computer import Laptop
from computer import Tablet
from comp_set import CompSet

# Создаём различные объекты
comp = Computer('IBM Personal Computer', 'IMB', 'PC 5150')

my_phone_os = Smartphone.OperatingSystem(
    Smartphone.OperatingSystem.Type.Android, '4.4.4')
my_phone = Smartphone('Мой телефон', 'Xiaomi', 'Redmi 2', my_phone_os)
my_phone.sim_type = 'micro SIM'
my_phone.sim_count = 2
my_phone.builtin_memory = 8
my_phone.ram_memory = 1


pc_os = PersonalComputer.OperatingSystem(
    PersonalComputer.OperatingSystem.Type.OSX, 'Sierra (10.12)')
pc = PersonalComputer('Яблоко', 'Apple', 'MacBook5,2', pc_os)
pc.builtin_memory = 160
pc.ram_memory = 2


desktop_pc_os = DesktopComputer.OperatingSystem(
    DesktopComputer.OperatingSystem.Type.Linux, 'Debian 8.6 (Jessie)')
desktop_pc = DesktopComputer('Настольный ПК', 'ASUS', 'K31AN', desktop_pc_os)
desktop_pc.builtin_memory = 500
desktop_pc.ram_memory = 4
desktop_pc.form_factor = 'Mini-Tower'


my_job_notebook_os = Laptop.OperatingSystem(
    Laptop.OperatingSystem.Type.MicrosoftWindows, '10')
my_job_notebook = Laptop('Мой рабочий ноутбук', 'Lenovo', 'E440',
                         my_job_notebook_os)
my_job_notebook.laptop_type = 'Традиционный'
my_job_notebook.builtin_memory = 450
my_job_notebook.ram_memory = 8

tablet_pc_os = Tablet.OperatingSystem(
    Tablet.OperatingSystem.Type.Android, '6.0')
tablet_pc = Tablet('Планшет', 'Samsung', 'Galaxy Tab A 10.1', tablet_pc_os)
tablet_pc.builtin_memory = 16
tablet_pc.ram_memory = 2

# Выполняем действия с набором объектов
computer_set = CompSet()
computer_set.add(comp)
computer_set.add(my_phone)
computer_set.add(pc)
computer_set.add(desktop_pc)
computer_set.add(my_job_notebook)
computer_set.add(tablet_pc)
print('Набор:')
print(computer_set)
print('Удаляем объект "Мой телефон" из набора:')
computer_set.remove(my_phone)
print(computer_set)
print()

print('1-ый элемент в наборе:')
print(computer_set[0])

print('Текущий набор:')
print(computer_set)
print('Заменяем 1-ый элемент набора:')
computer_set[0] = my_phone
print(computer_set)
print()

print('Текущий набор:')
print(computer_set)
print('Удаляем 3-ий элемент в наборе:')
del computer_set[2]
print(computer_set)
print()

print('Текущий набор:')
print(computer_set)
print('Получаем срез из набора (3 и 4 элементы):')
print(computer_set[2:4])
print()

print('Текущий набор:')
print(computer_set)
print('Присваиваем срезу из набора (2 и 3 элементы):')
computer_set[1:3] = [comp, desktop_pc]
print(computer_set)
print()

print('Текущий набор:')
print(computer_set)
print('Удаляем срез (3-4 элементы):')
del computer_set[2:4]
print(computer_set)
print()

print('Конкатенация:')
print('Набор 1:')
print(computer_set)
print('Набор 2:')
computer_set2 = CompSet()
computer_set2.add(my_job_notebook)
computer_set2.add(tablet_pc)
print(computer_set2)
computer_set = computer_set + computer_set2
print('Набор 1 + Набор 2:')
print(computer_set)
print()

computer_set.save('computer_set.json')
print('Набор был сохранен в файл')

new_computer_set = CompSet.load('computer_set.json')
print('Набор загружен из файла:')
print(new_computer_set)

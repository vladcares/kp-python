# КП СР-11.2
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from computer import Computer
from computer import Smartphone
from computer import PersonalComputer
from computer import DesktopComputer
from computer import Laptop
from computer import Tablet

comp = Computer('IBM Personal Computer', 'IMB', 'PC 5150')
print(comp)
comp.print_specifications()
comp.save('computer.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    comp2 = Computer.load('computer.json')
    if comp2:
        print("Загруженный объект:\r\n" + str(comp2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")
print()

my_phone_os = Smartphone.OperatingSystem(
    Smartphone.OperatingSystem.Type.Android, '4.4.4')
my_phone = Smartphone('Мой телефон', 'Xiaomi', 'Redmi 2', my_phone_os)
my_phone.sim_type = 'micro SIM'
my_phone.sim_count = 2
my_phone.builtin_memory = 8
my_phone.ram_memory = 1
print(my_phone)
my_phone.print_specifications()
my_phone.save('my_phone.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    my_phone2 = Smartphone.load('my_phone.json')
    if my_phone2:
        print("Загруженный объект:\r\n" + str(my_phone2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")
print()

pc_os = PersonalComputer.OperatingSystem(
    PersonalComputer.OperatingSystem.Type.OSX, 'Sierra (10.12)')
pc = PersonalComputer('Яблоко', 'Apple', 'MacBook5,2', pc_os)
pc.builtin_memory = 160
pc.ram_memory = 2
print(pc)
pc.print_specifications()
pc.save('pc.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    pc2 = PersonalComputer.load('pc.json')
    if pc2:
        print("Загруженный объект:\r\n" + str(pc2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")
print()

desktop_pc_os = DesktopComputer.OperatingSystem(
    DesktopComputer.OperatingSystem.Type.Linux, 'Debian 8.6 (Jessie)')
desktop_pc = DesktopComputer('Настольный ПК', 'ASUS', 'K31AN', desktop_pc_os)
desktop_pc.builtin_memory = 500
desktop_pc.ram_memory = 4
desktop_pc.form_factor = 'Mini-Tower'
print(desktop_pc)
desktop_pc.print_specifications()
desktop_pc.save('desktop_pc.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    desktop_pc2 = DesktopComputer.load('desktop_pc.json')
    if desktop_pc2:
        print("Загруженный объект:\r\n" + str(desktop_pc2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")
print()

my_job_notebook_os = Laptop.OperatingSystem(
    Laptop.OperatingSystem.Type.MicrosoftWindows, '10')
my_job_notebook = Laptop('Мой рабочий ноутбук', 'Lenovo', 'E440',
                         my_job_notebook_os)
my_job_notebook.laptop_type = 'Традиционный'
my_job_notebook.builtin_memory = 450
my_job_notebook.ram_memory = 8
print(my_job_notebook)
my_job_notebook.print_specifications()
my_job_notebook.save('my_job_notebook.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    my_job_notebook2 = Laptop.load('my_job_notebook.json')
    if my_job_notebook2:
        print("Загруженный объект:\r\n" + str(my_job_notebook2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")
print()

tablet_pc_os = Tablet.OperatingSystem(
    Tablet.OperatingSystem.Type.Android, '6.0')
tablet_pc = Tablet('Планшет', 'Samsung', 'Galaxy Tab A 10.1', tablet_pc_os)
tablet_pc.builtin_memory = 16
tablet_pc.ram_memory = 2
print(tablet_pc)
tablet_pc.print_specifications()
tablet_pc.save('tablet_pc.json')
print('Выполнено сохранение данных об объекте в файл.')
print()

print('Выполняется загрузка данных об объекте из файла.')
try:
    tablet_pc2 = Laptop.load('tablet_pc.json')
    if tablet_pc2:
        print("Загруженный объект:\r\n" + str(tablet_pc2))
    else:
        print('Не удалось загрузить данные.')
except FileNotFoundError:
    print("Файл не найден!")

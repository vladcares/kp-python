# КП СР-12.3
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from backup import Backup
import sys

if len(sys.argv) == 2:
    backup = Backup()
    if backup is not None:
        backup.copy_project(sys.argv[1])
    else:
        print('Не удалось загрузить настройки')
else:
    print('Приложение было запущено с некорректными параметрами')

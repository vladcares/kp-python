# КП СР-12.3
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from datetime import datetime
import json
from os import listdir, makedirs
from os.path import isfile, join, exists, getmtime
from shutil import copyfile


class Backup:
    """ Класс реализует копирование файлов и папок """

    SETTINGS_FILENAME = 'settings.json'

    def __init__(self):
        """ Конструктор класса """
        with open(Backup.SETTINGS_FILENAME,
                  encoding="UTF-8") as settings_file:
                settings = json.load(settings_file)
        if 'log_filename' in settings:
            self._log_filename = settings['log_filename']
        else:
            return None
        if 'confirm' in settings:
            self._confirm = settings['confirm']
        else:
            return None
        if 'projects' in settings:
            self._projects = settings['projects']
        else:
            return None
        self._log('Настройки были успешно загружены')

    def _now(self):
        """ Строка с текущими датой и временем """
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _log(self, text):
        """ Запись об игре в журнал и в консоль """
        text = self._now() + ' '*4 + text
        with open(self._log_filename, 'a',
                  encoding="UTF-8") as self._log_file:
            self._log_file.write(text + '\n')

    def _copy_confirmed(self):
        """ Подтверждение копирования """
        if not self._confirm:
            return True
        else:
            ans = ''
            while ans not in ('да', 'нет'):
                ans = input(
                    'Вы уверены, что хотите скопировать '
                    'данные файлы (да/нет)? ')
                ans = ans.lower()
            if ans == 'да':
                self._log('Пользователь подтвердил операцию копирования')
            else:
                self._log(
                    'Пользователь не подтвердил операцию копирования\n')
            return ans == 'да'

    def _check_project_info(self, project):
        """ Проверка наличия данных о проекте в настройках """
        if project not in self._projects:
            msg = 'Не удалось найти сведения о проекте {} ' \
                  'в настройках'.format(project)
            self._log(msg + '\n')
            print(msg)
            return False
        result = True
        if 'src' not in self._projects[project]:
            msg = 'Не удалось найти сведения об источниках проекта {} ' \
                  'в настройках'.format(project)
            self._log(msg)
            print(msg)
            result = False
        if 'dest' not in self._projects[project]:
            msg = 'Не удалось найти сведения о целевых папках проекта {} ' \
                  'в настройках'.format(project)
            self._log(msg)
            print(msg)
            result = False
        if not result:
            self._log('Копирование не удалось\n')
        return result

    def _explore_files(self, path, datetime_cond):
        """ Определяет файлы для копирования """
        if not datetime_cond:
            return [f for f in listdir(path) if isfile(join(path, f))]
        else:
            files = []
            for f in listdir(path):
                if isfile(join(path, f)):
                    mod_date = datetime.fromtimestamp(getmtime(join(path, f)))
                    if mod_date > datetime_cond:
                        files.append(f)
            return files

    def copy_project(self, project):
        """ Копирование файлов проекта """
        if not self._check_project_info(project):
            return
        src = self._projects[project]['src']
        dest = self._projects[project]['dest']
        datetime_cond = False
        if 'datetime' in self._projects[project]:
            datetime_cond = datetime.strptime(
                self._projects[project]['datetime'], '%Y-%m-%d %H:%M')
        operations = []
        for src_path, dest_path in zip(src, dest):
            operation = {}
            files = self._explore_files(src_path, datetime_cond)
            operation['files'] = files
            operation['src'] = src_path
            operation['dest'] = dest_path
            operations.append(operation)
            print('Список файлов для папки {}:'.format(src_path))
            print('\r\n'.join(files))
        files = [f for operation in operations for f in operation['files']]
        print('Количество файлов: {}'.format(len(files)))
        print()

        if self._copy_confirmed():
            self._log('Выполняется копирование файлов...')
            print('Начало копирования: ' + self._now())
            start_time = datetime.now()
            for operation in operations:
                for f in operation['files']:
                    dest_path = operation['dest']
                    self._log(
                        'Выполняется копирование файла {} из папки {} '
                        'в папку {}'.format(
                            f, operation['src'], dest_path))
                    if not exists(dest_path):
                        makedirs(dest_path)
                    copyfile(join(operation['src'], f),
                             join(dest_path, f))
            end_time = datetime.now()
            print('Окончание копирования: ' + self._now())
            delta = end_time - start_time
            combined = delta.seconds + delta.microseconds/1E6
            time_elapsed = 'Затрачено времени: {} сек'.format(combined)
            print(time_elapsed)
            self._log(time_elapsed + '\n')

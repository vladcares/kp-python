# КП СР-12.2
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from datetime import datetime
import random


class GuessNumGame:
    """ Класс для реализации игры "Угадай число" """

    LOG_FILENAME = 'guessnum_log.txt'

    def __init__(self):
        """ Конструктор класса """
        self._log('Инициализация игры', True)
        self._nums = []
        self._tries_num = 0
        random.seed()

    def _now(self):
        """ Строка с текущими датой и временем """
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _tf(self, text):
        """ Форматирование сообщения """
        return self._now() + ' '*4 + text

    def _log(self, text, console=False):
        """ Запись об игре в журнал и в консоль """
        text = self._now() + ' '*4 + text
        with open(GuessNumGame.LOG_FILENAME, 'a',
                  encoding="UTF-8") as self._log_file:
            self._log_file.write(text + '\n')
        if console:
            print(text)

    def start(self):
        """ Начало игры """
        self._log('Игра запущена')
        print(self._tf('Загадай целое число'))
        self.input_range()

        if self._a == self._b:
            self.finish(self._a)
        elif self._a < self._b:
            # Все возможные числа
            self._nums = [x for x in range(self._a, self._b+1)]
            self._log('Диапозон возможных чисел : {}'.format(str(self._nums)))
            # Количество чисел в диапозоне
            nums_count = len(self._nums)
            # Попытки угадать число
            ans = 'нет'
            num = self.guess()
            while ans == 'нет':
                self._tries_num += 1
                print(self._tf('Попытка {}: возможно это число {}?'.format(
                    self._tries_num, num)))
                self._log('Номер попытки: {}. Число: {}'.format(
                    self._tries_num, num))

                ans = self.get_answer('Число угадано или нет?')
                if ans == 'да':
                    break
                    self.finish(num)
                elif ans == 'нет':
                    # Если число не в начале и не в конце диапазона
                    if self._nums.index(num) not in (0, nums_count-1):
                        # то пытаемся сократить диапозон
                        print(self._tf(
                            'Загаданное число больше числа {}?'.format(num)))
                        ans_bigger = self.get_answer(
                            'Загаданное число больше числа {}?'.format(num))
                        if ans_bigger == 'да':
                            self._log(
                                'Загаданное число больше числа ' + str(num))
                            self._a = num+1
                        elif ans_bigger == 'нет':
                            self._log(
                                'Загаданное число меньше числа ' + str(num))
                            self._b = num-1
                        else:
                            pass
                        self._nums = [x for x in range(self._a, self._b+1)]
                    elif self._nums.index(num) == 0:
                        self._nums.remove(num)
                        self._a = num+1
                    elif self._nums.index(num) == nums_count-1:
                        self._nums.remove(num)
                        self._b = num-1

                    nums_count = len(self._nums)

                    self._log(
                        'Диапозон возможных чисел изменился: {}'.format(
                            str(self._nums)))

                    if nums_count == 1:
                        # Осталось одно неназванное число
                        self._tries_num += 1
                        num = self._nums[0]
                        break
                    num = self.guess()
                else:
                    pass
            self.finish(num)
        else:
            pass

    def input_range(self):
        """ Ввод диапозона чисел """
        print(self._tf('Введи интервал, в который входит это число [a; b]:'))
        self._a = int(input(self._tf('a: ')))
        self._b = int(input(self._tf('b: ')))
        while self._a > self._b:
            print(self._tf('Неверный ввод. Повтори попытку.'))
            self._a = int(input(self._tf('a: ')))
            self._b = int(input(self._tf('b: ')))
        self._log('Пользователь ввёл диапозон чисел: [{}; {}]'.format(
            self._a, self._b))

    def get_answer(self, question):
        """ Получение ответа: да или нет """
        answer = input(self._tf('(Да/Нет): ')).lower()
        while answer not in ('да', 'нет'):
            print(self._tf('Неверный ввод. {}'.format(question)))
            answer = input(self._tf('(Да/Нет): ')).lower()
        return answer

    def guess(self):
        """ Попытка угадать число """
        return random.randint(self._a, self._b)

    def finish(self, num):
        """ Окончание игры """
        print(self._tf('Число угадано! Это: ' + str(num)))
        print(self._tf('Число попыток: ' + str(self._tries_num)))
        print(self._tf('Спасибо за игру!'))
        self._log('Загаданное число: ' + str(num))
        self._log('Число попыток: ' + str(self._tries_num))
        self._log('Игра завершена\n')

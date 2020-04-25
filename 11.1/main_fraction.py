# КП СР-11.1
# Радионов Владислав Вячеславович
# radionov.vladislav@gmail.com

from fraction import Fraction
from copy import copy

# Типы дробей
print('Типы дробей:')
for fraction_type in Fraction.Type:
    print('{0} - {1}'.format(fraction_type, fraction_type.describe()))
print()

# Конструкторы
print('-'*30)
print('1. {0} дробь'.format(Fraction.Type.simple.describe()))
print('-'*30)
print('1) Обычный конструктор:')
fr_simple_pos = Fraction(3, 12)
print('Положительная дробь: {}'.format(fr_simple_pos))
fr_simple_neg = Fraction(3, 12, True)
print('Отрицательная дробь: {}'.format(fr_simple_neg))
print()
print('2) Конструктор из строкового значения:')
print('Положительная дробь: {}'.format(Fraction.from_string('11/6')))
print('Отрицательная дробь: {}'.format(Fraction.from_string('-11/6')))
print()

print('-'*30)
print('2. {0} дробь'.format(Fraction.Type.mixed.describe()))
print('-'*30)
print('1) Обычный конструктор:')
fr_mixed_pos = Fraction(1, 4, False, 25)
print('Положительная дробь: {}'.format(fr_mixed_pos))
fr_mixed_neg = Fraction(1, 4, True, 25)
print('Отрицательная дробь: {}'.format(fr_mixed_neg))
print()
print('2) Конструктор из строкового значения:')
print('Положительная дробь: {}'.format(Fraction.from_string('10 12/15')))
print('Отрицательная дробь: {}'.format(Fraction.from_string('-10 12/15')))
print()

print('-'*30)
print('3. {0} дробь'.format(Fraction.Type.decimal.describe()))
print('-'*30)
print('1) Обычный конструктор:')
fr_decimal_pos = Fraction.from_decimal(1.125)
print('Положительная дробь: {}'.format(fr_decimal_pos))
fr_decimal_neg = Fraction.from_decimal(-1.125)
print('Отрицательная дробь: {}'.format(fr_decimal_neg))
print()
print('2) Конструктор из строкового значения:')
print('Положительная дробь: {}'.format(Fraction.from_string('25.57')))
print('Отрицательная дробь: {}'.format(Fraction.from_string('-25.57')))
print()
print()

# Получение типа дроби
print('Получаем типы:')
print('{0}: {1} ({2})'.format(
 fr_simple_neg, fr_simple_neg.get_type(), fr_simple_neg.get_type().describe()))
print('{0}: {1} ({2})'.format(
 fr_mixed_pos, fr_mixed_pos.get_type(), fr_mixed_pos.get_type().describe()))
print('{0}: {1} ({2})'.format(
 fr_decimal_pos, fr_decimal_pos.get_type(),
 fr_decimal_pos.get_type().describe()))
print()
print()

# Получение целой части, числителя и делителя дроби
print('Получаем целую часть:')
print('{0} ({1}): {2}'.format(
 fr_simple_pos, fr_simple_pos.get_type(), fr_simple_pos.get_integer()))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), fr_mixed_neg.get_integer()))
print('{0} ({1}): {2}'.format(
 fr_decimal_neg, fr_decimal_neg.get_type(), fr_decimal_neg.get_integer()))
print()

print('Получаем числитель:')
print('{0} ({1}): {2}'.format(
 fr_simple_pos, fr_simple_pos.get_type(), fr_simple_pos.get_numerator()))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), fr_mixed_neg.get_numerator()))
print('{0} ({1}): {2}'.format(
 fr_decimal_neg, fr_decimal_neg.get_type(), fr_decimal_neg.get_numerator()))
print()

print('Получаем знаменатель:')
print('{0} ({1}): {2}'.format(
 fr_simple_pos, fr_simple_pos.get_type(), fr_simple_pos.get_denominator()))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), fr_mixed_neg.get_denominator()))
print('{0} ({1}): {2}'.format(
 fr_decimal_neg, fr_decimal_neg.get_type(), fr_decimal_neg.get_denominator()))
print()
print()

# Сокращение дроби
print('Сокращаем дроби:')
fr_simple_pos_reduced = copy(fr_simple_pos)
fr_mixed_neg_reduced = copy(fr_mixed_neg)
fr_decimal_pos_reduced = copy(fr_decimal_pos)
fr_simple_pos_reduced.reduce()
fr_mixed_neg_reduced.reduce()
print('{0} ({1}): {2}'.format(
 fr_simple_pos, fr_simple_pos.get_type(), fr_simple_pos_reduced))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), fr_mixed_neg_reduced))
try:
    fr_decimal_pos_reduced.reduce()
except TypeError:
    msg = 'операция не применима'
    print('{0} ({1}): {2}'.format(
     fr_decimal_pos, fr_decimal_pos.get_type(), msg))
print()
print()

# Преобразование дробей в разные типы
print('Преобразуем дроби в разные типы')
print('-'*30)
print(Fraction.Type.simple, '->', Fraction.Type.mixed)
print('-'*30)
try:
    print(fr_simple_pos, '->', fr_simple_pos.to_mixed())
except ValueError:
    print(fr_simple_pos, '->', 'невозможно преобразовать')
fr_simple_neg_new = Fraction(30, 9, True)
print(fr_simple_neg_new, '->', fr_simple_neg_new.to_mixed())
print()

print('-'*30)
print(Fraction.Type.simple, '->', Fraction.Type.decimal)
print('-'*30)
print(fr_simple_pos, '->', fr_simple_pos.to_decimal())
print(fr_simple_neg, '->', fr_simple_neg.to_decimal())
print()

print('-'*30)
print(Fraction.Type.simple, '-> int')
print('-'*30)
print(Fraction(-1, 1), '->', Fraction(1, 1).to_integer())
print(Fraction(150, 25), '->', Fraction(150, 25).to_integer())
print()

print('-'*30)
print(Fraction.Type.mixed, '->', Fraction.Type.simple)
print('-'*30)
print(fr_mixed_pos, '->', fr_mixed_pos.to_simple())
print(fr_mixed_neg, '->', fr_mixed_neg.to_simple())
print()

print('-'*30)
print(Fraction.Type.mixed, '->', Fraction.Type.decimal)
print('-'*30)
print(fr_mixed_pos, '->', fr_mixed_pos.to_decimal())
print(fr_mixed_neg, '->', fr_mixed_neg.to_decimal())
print()

print('-'*30)
print(Fraction.Type.mixed, '-> int')
print('-'*30)
print(Fraction(40, 8, True, 23), '->', Fraction(40, 8, True, 23).to_integer())
print(Fraction(56, 4, False, 1), '->', Fraction(56, 4, False, 1).to_integer())
print()

print('-'*30)
print(Fraction.Type.decimal, '->', Fraction.Type.simple)
print('-'*30)
print(fr_decimal_pos, '->', fr_decimal_pos.to_simple())
print(fr_decimal_neg, '->', fr_decimal_neg.to_simple())
print()

print('-'*30)
print(Fraction.Type.decimal, '->', Fraction.Type.mixed)
print('-'*30)
print(fr_decimal_pos, '->', fr_decimal_pos.to_mixed())
print(fr_decimal_neg, '->', fr_decimal_neg.to_mixed())
print()
print()

print('-'*30)
print(Fraction.Type.decimal, '-> int', )
print('-'*30)
print(Fraction.from_decimal(0.0), '->', Fraction.from_decimal(0.0).to_integer())
print(Fraction.from_decimal(-125.0),
      '->', Fraction.from_decimal(-125.0).to_integer())
print()
print()

# Выполняем арифметические операции с дробями
print('Выполняем операцию отрицания:')
print('{0} ({1}): {2}'.format(
 fr_simple_pos, fr_simple_pos.get_type(), -fr_simple_pos))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), -fr_mixed_neg))
print('{0} ({1}): {2}'.format(
 fr_decimal_pos, fr_decimal_neg.get_type(), -fr_decimal_pos))
print()

print('Выполняем операцию превращения дроби в положительную:')
print('{0} ({1}): {2}'.format(
 fr_simple_neg, fr_simple_neg.get_type(), fr_simple_pos.abs()))
print('{0} ({1}): {2}'.format(
 fr_mixed_neg, fr_mixed_neg.get_type(), fr_mixed_neg.abs()))
print('{0} ({1}): {2}'.format(
 fr_decimal_neg, fr_decimal_neg.get_type(), fr_decimal_neg.abs()))
print()

print('Выполняем операцию сложения для дробей:')
print('Первый слагаемый Simple => результат Simple (если возможно)')
result = fr_simple_pos + fr_simple_neg
print('{0} + {1} = {2} ({3})'.format(
 fr_simple_pos, fr_simple_neg, result, result.get_type()))
result = fr_simple_pos + Fraction.from_decimal(0.0)
print('{0} + {1} = {2} ({3})'.format(
 fr_simple_pos, Fraction.from_decimal(0.0), result, result.get_type()))
result = fr_simple_neg_new + fr_simple_neg_new
print('{0} + {1} = {2} ({3})'.format(
 fr_simple_neg_new, fr_simple_neg_new, result, result.get_type()))
result = fr_simple_pos + fr_mixed_neg
print('{0} + {1} = {2} ({3})'.format(
 fr_simple_pos, fr_mixed_neg, result, result.get_type()))
result = -fr_simple_pos + fr_decimal_pos
print('{0} + {1} = {2} ({3})'.format(
 -fr_simple_pos, fr_decimal_pos, result, result.get_type()))
print()

print('Первый слагаемый Mixed => результат Mixed (если возможно)')
result = fr_mixed_pos + fr_mixed_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_mixed_pos, fr_mixed_pos, result, result.get_type()))
result = fr_mixed_pos + fr_mixed_neg
print('{0} + {1} = {2} ({3})'.format(
 fr_mixed_pos, fr_mixed_neg, result, result.get_type()))
result = fr_mixed_neg + fr_simple_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_mixed_neg, fr_simple_pos, result, result.get_type()))
result = fr_mixed_neg + fr_decimal_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_mixed_neg, fr_decimal_pos, result, result.get_type()))
print()

print('Первый слагаемый Decimal => результат Decimal')
result = fr_decimal_pos + fr_decimal_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_decimal_pos, fr_decimal_pos, result, result.get_type()))
result = fr_decimal_pos + fr_decimal_neg
print('{0} + {1} = {2} ({3})'.format(
 fr_decimal_pos, fr_decimal_neg, result, result.get_type()))
result = fr_decimal_neg + fr_simple_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_decimal_neg, fr_simple_pos, result, result.get_type()))
result = fr_decimal_neg + fr_mixed_pos
print('{0} + {1} = {2} ({3})'.format(
 fr_decimal_neg, fr_mixed_pos, result, result.get_type()))
print()

print('Выполняем операцию вычитания для дробей:')
print('Simple')
result = fr_simple_pos - fr_mixed_neg
print('{0} - {1} = {2} ({3})'.format(
    fr_simple_pos, fr_mixed_neg, result, result.get_type()))
result = fr_mixed_neg - fr_decimal_neg
print('Mixed')
print('{0} - {1} = {2} ({3})'.format(
    fr_mixed_neg, fr_decimal_neg, result, result.get_type()))
result = fr_decimal_pos - fr_simple_pos
print('Decimal')
print('{0} - {1} = {2} ({3})'.format(
    fr_decimal_pos, fr_simple_pos, result, result.get_type()))
print()

print('Сравниваем, одинаковые ли дроби:')
print('Simple')
print('{0} = {1} ({2})'.format(
    fr_simple_pos, fr_decimal_neg, fr_simple_pos == fr_decimal_neg))
print('Mixed')
print('{0} = {1} ({2})'.format(
    fr_mixed_neg, fr_mixed_neg, fr_mixed_neg == fr_mixed_neg))
print('Decimal')
print('{0} = {1} ({2})'.format(
    fr_decimal_pos, fr_simple_neg, fr_decimal_pos == fr_simple_neg))
print()

print('Сравниваем, разные ли дроби:')
print('Simple')
print('{0} != {1} ({2})'.format(
    fr_simple_pos, fr_decimal_neg, fr_simple_pos != fr_decimal_neg))
print('Mixed')
print('{0} != {1} ({2})'.format(
    fr_mixed_neg, fr_mixed_neg, fr_mixed_neg != fr_mixed_neg))
print('Decimal')
print('{0} != {1} ({2})'.format(
    fr_decimal_pos, fr_simple_neg, fr_decimal_pos != fr_simple_neg))
print()

print('Сравниваем, меньше ли дробь 1, чем дробь 2:')
print('Simple')
print('{0} < {1} ({2})'.format(fr_simple_pos, fr_decimal_neg,
                               fr_simple_pos < fr_decimal_neg))
print('Mixed')
print('{0} < {1} ({2})'.format(fr_mixed_neg, fr_mixed_neg,
                               fr_mixed_neg < fr_mixed_neg))
print('Decimal')
print('{0} < {1} ({2})'.format(fr_decimal_neg, fr_simple_pos,
                               fr_decimal_neg < fr_simple_pos))
print()

print('Сравниваем, больше ли дробь 1, чем дробь 2:')
print('Simple')
print('{0} > {1} ({2})'.format(fr_simple_pos, fr_decimal_neg,
                               fr_simple_pos > fr_decimal_neg))
print('Mixed')
print('{0} > {1} ({2})'.format(fr_mixed_neg, fr_mixed_neg,
                               fr_mixed_neg > fr_mixed_neg))
print('Decimal')
print('{0} > {1} ({2})'.format(fr_decimal_neg, fr_simple_pos,
                               fr_decimal_neg > fr_simple_pos))
print()

print('Сравниваем, дробь 1 меньше или равна дроби 2:')
print('Simple')
print('{0} <= {1} ({2})'.format(fr_simple_pos, fr_decimal_neg,
                                fr_simple_pos <= fr_decimal_neg))
print('Mixed')
print('{0} <= {1} ({2})'.format(fr_mixed_neg, fr_mixed_neg,
                                fr_mixed_neg <= fr_mixed_neg))
print('Decimal')
print('{0} <= {1} ({2})'.format(fr_decimal_neg, fr_simple_pos,
                                fr_decimal_neg <= fr_simple_pos))
print()

print('Сравниваем, дробь 1 больше или равна дроби 2:')
print('Simple')
print('{0} >= {1} ({2})'.format(fr_simple_pos, fr_decimal_neg,
                                fr_simple_pos >= fr_decimal_neg))
print('Mixed')
print('{0} >= {1} ({2})'.format(fr_mixed_neg, fr_mixed_neg,
                                fr_mixed_neg >= fr_mixed_neg))
print('Decimal')
print('{0} >= {1} ({2})'.format(fr_decimal_neg, fr_simple_pos,
                                fr_decimal_neg >= fr_simple_pos))
print()

print('Умножаем дробь 1 на дробь 2:')
print('Simple')
print('{0} * {1} = {2}'.format(fr_simple_pos, fr_decimal_neg,
                               fr_simple_pos * fr_decimal_neg))
print('Mixed')
print('{0} * {1} = {2}'.format(fr_mixed_neg, fr_mixed_neg,
                               fr_mixed_neg * fr_mixed_neg))
print('Decimal')
print('{0} * {1} = {2}'.format(fr_decimal_neg, fr_simple_pos,
                               fr_decimal_neg * fr_simple_pos))
print()

print('Делим дробь 1 на дробь 2:')
print('Simple')
print('{0} / {1} = {2}'.format(fr_simple_pos, fr_decimal_neg,
                               fr_simple_pos / fr_decimal_neg))
print('Mixed')
print('{0} / {1} = {2}'.format(fr_mixed_neg, fr_mixed_neg,
                               fr_mixed_neg / fr_mixed_neg))
print('Decimal')
print('{0} / {1} = {2}'.format(fr_decimal_neg, fr_simple_pos,
                               fr_decimal_neg / fr_simple_pos))
print()

print('Целочисленно делим дробь 1 на дробь 2:')
print('Simple')
print('{0} // {1} = {2}'.format(fr_simple_pos, fr_decimal_neg,
                                fr_simple_pos // fr_decimal_neg))
print('Mixed')
print('{0} // {1} = {2}'.format(fr_mixed_neg, fr_mixed_neg,
                                fr_mixed_neg // fr_mixed_neg))
print('Decimal')
print('{0} // {1} = {2}'.format(fr_decimal_neg, fr_simple_pos,
                                fr_decimal_neg // fr_simple_pos))
print()

print('Вычисляем остаток от деления дроби 1 на дробь 2:')
print('Simple')
print('{0} % {1} = {2}'.format(fr_simple_pos, fr_decimal_neg,
                               fr_simple_pos % fr_decimal_neg))
print('Mixed')
print('{0} % {1} = {2}'.format(fr_mixed_neg, fr_mixed_neg,
                               fr_mixed_neg % fr_mixed_neg))
print('Decimal')
print('{0} % {1} = {2}'.format(fr_decimal_neg, fr_simple_pos,
                               fr_decimal_neg % fr_simple_pos))
print()

print('Целочисленно делим дробь 1 на дробь 2:')
print('Simple')
print('{0} // {1} = {2}'.format(fr_simple_pos, fr_decimal_neg,
                                fr_simple_pos // fr_decimal_neg))
print('Mixed')
print('{0} // {1} = {2}'.format(fr_mixed_neg, fr_mixed_neg,
                                fr_mixed_neg // fr_mixed_neg))
print('Decimal')
print('{0} // {1} = {2}'.format(fr_decimal_neg, fr_simple_pos,
                                fr_decimal_neg // fr_simple_pos))
print()

print('Возводим дробь в степень:')
print('Simple')
print('{0} ** {1} = {2}'.format(fr_simple_pos, 0,
                                fr_simple_pos ** 0))
print('Mixed')
print('{0} ** {1} = {2}'.format(fr_mixed_neg, 1,
                                fr_mixed_neg ** 1))
print('Decimal')
print('{0} ** {1} = {2}'.format(fr_decimal_neg, 3,
                                fr_decimal_neg ** 3))
print()


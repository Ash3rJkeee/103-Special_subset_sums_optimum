# todo 1) Написать алгоритм проверки условия 1 (S(B) != S(C)) и ( S(B) > S(C) if len(B) > len(C) )   ГОТОВО

# todo 2) Написать функцию генерации предположительного множества A = B + С при n=7, удовлетворяющего условию провеки
#  (todo1) по формуле A6 = {a1, a2, ... , an}, A7 = {b, a1+b, a2+b, ... ,an+b}, где b - "средний" элемент предыдущей
#  строки      ГОТОВО

# todo 3) Написать функцию уточнения множества А для минимизации S(A)    ГОТОВО

import math
import datetime
import itertools


def conditional_test(many):
    """На вход принимает список. Возвращает результат проверки множества, соответствующего данному списку на условие
    задачи."""
    combinations = set()

    # создаем множество всех возможных подмножеств
    for i in range(1, len(many)):
        combinations.update(itertools.combinations(many, i))

    # преобразуем в список и сортируем для удобства печати при необходимости
    combinations = list(combinations)
    combinations.sort()

    # перебираем все возможные пары подмножеств для сравнения между собой
    for i in combinations:
        b_ = list(combinations)
        b_.remove(i)
        for j in b_:
            set_i = set(i)
            set_j = set(j)
            sum_i = sum(list(set_i))
            sum_j = sum(list(set_j))

            # определяем непересекающиеся подмножества и проводим над ними проверку по условию
            if set_i.isdisjoint(set_j):
                if sum_i == sum_j:
                    return False
                if len(list(set_i)) > len(list(set_j)):
                    if sum_i <= sum_j:
                        return False
                if len(list(set_i)) < len(list(set_j)):
                    if sum_i >= sum_j:
                        return False
    return True


def many_generator(many):
    """На вход функция получает прошлое множество для n-1. Сама считает n-1 и возвращает приближенное к оптимальному
    множество для n."""
    average = math.ceil(sum(many)/len(many))
    a = [average]
    for i in range(len(many)):
        a.append(average + many[i])
    return a


def many_clarification(many):
    """Функция на входе получает приближенное к минимальному множество и возвращает минимизированное"""
    sum_many = sum(many)
    a = list(range(0, 7))
    a_out = many[:]
    delta = 3
    for zero in range(many[0] - delta, many[0] + delta):
        a[0] = zero

        for first in range(a[0] + 1, many[1] + delta):
            a[1] = first

            for second in range(a[1] + 1, many[2] + delta):
                a[2] = second

                for third in range(a[2] + 1, many[3] + delta):
                    a[3] = third

                    for fourth in range(a[3] + 1, many[4] + delta):
                        a[4] = fourth

                        for fifth in range(a[4] + 1, many[5] + delta):
                            a[5] = fifth

                            for sixth in range(a[5] + 1, many[6] + delta):
                                a[6] = sixth
                                sum_a = sum(a)
                                print("\r", end="")
                                print("Кандидат а=", a, end="")
                                if conditional_test(a):
                                    if sum_a < sum_many:
                                        sum_many = sum_a
                                        a_out = a[:]
    return a_out


a6 = [11, 18, 19, 20, 22, 25]

print("Программа поиска множества a7 для 103 задачи проекта Эйлера.")
print()

start = datetime.datetime.now()

a7 = many_generator(a6)
print("приближенное a7 = ", a7, "sum a7 = ", sum(a7))
print()

a7 = many_clarification(a7)

stop = datetime.datetime.now()

ellapsed_time = stop - start

print()
print()
print("Вычисления закончены и заняли", ellapsed_time.seconds, "секунд.")
print("Множество a7 =", a7, "sum a7= ", sum(a7))

a7_string = ""
for i in a7:
    a7_string += str(i)

print("Строка ответа =", a7_string)

# Output:
# Программа поиска множества a7 для 103 задачи проекта Эйлера.
#
# приближенное a7 =  [20, 31, 38, 39, 40, 42, 45] sum a7 =  255
#
# Кандидат а= [22, 33, 40, 41, 42, 44, 47]
#
# Вычисления закончены и заняли 1405 секунд.
# Множество a7 = [20, 31, 38, 39, 40, 42, 45] sum a7=  255
# Строка ответа = 20313839404245
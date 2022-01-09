'''Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.'''

import cProfile
import math
import timeit


def primes_eratosphen(n):
    '''Нахождение n-го по счету простого числа (первое = 2) c помощью решета Эратосфена'''

    end = math.ceil(2 * n * math.log(n))  # согласно функции распеределения простых чисел до (2 * n * ln(n))
    sieve = [i for i in range(end)]
    sieve[1] = 0

    for i in range(2, end):
        if sieve[i] != 0:
            j = i * 2
            while j < end:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n-1]

# cProfile.run('primes_eratosphen(10**3)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.004    0.004    0.005    0.005 task02.py:16(primes_eratosphen)
#         1    0.001    0.001    0.001    0.001 task02.py:20(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task02.py:30(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('primes_eratosphen(10**4)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.097    0.097 <string>:1(<module>)
#         1    0.073    0.073    0.095    0.095 task02.py:16(primes_eratosphen)
#         1    0.017    0.017    0.017    0.017 task02.py:20(<listcomp>)
#         1    0.005    0.005    0.005    0.005 task02.py:30(<listcomp>)
#         1    0.000    0.000    0.097    0.097 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('primes_eratosphen(10**5)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.023    0.023    1.322    1.322 <string>:1(<module>)
#         1    1.098    1.098    1.299    1.299 task02.py:16(primes_eratosphen)
#         1    0.138    0.138    0.138    0.138 task02.py:20(<listcomp>)
#         1    0.063    0.063    0.063    0.063 task02.py:30(<listcomp>)
#         1    0.000    0.000    1.322    1.322 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''Рост длительности выполнения операции нелинеен
Также видно, что формирование самого списка также занимает приличную долю
длительности выполнения кода'''

def primes_2(n):
    '''n-ое простое число с помощью арифметической проверки'''
    count = 1
    number = 1
    sieve = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2
        for i in sieve:
            if number % i == 0:
                break
        else:
            count += 1
            sieve.append(number)

    return number

# cProfile.run('primes_2(10**3)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.044    0.044 <string>:1(<module>)
#         1    0.044    0.044    0.044    0.044 task02.py:70(primes_2)
#         1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('primes_2(10**4)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.724    2.724 <string>:1(<module>)
#         1    2.721    2.721    2.724    2.724 task02.py:70(primes_2)
#         1    0.000    0.000    2.724    2.724 {built-in method builtins.exec}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('primes_2(10**5)')
# Здесь пришлось оборвать выполнение программы на 74562 вызове
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000  154.880  154.880 <string>:1(<module>)
#         1  154.857  154.857  154.880  154.880 task02.py:70(primes_2)
#         1    0.000    0.000  154.880  154.880 {built-in method builtins.exec}
#     74562    0.023    0.000    0.023    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''Выполнение воторой функции оказалось длительнее, рост длительности нелинейный 
(при чем быстрее рост длительности, чем в певой функции)'''

#print(primes_eratosphen(10**4) == primes_2(10**4))


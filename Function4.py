def max_number(a, b):
    if a<=b:
        return b
    if a>=b:
        return a

# Вывод: 55
print(max_number(55, 10))


def empty_function():
    pass

# Автотест для функции max_number(a, b) из первого задания
def max_number(a, b):
    assert a<=b
    return b


# Вывод: 55
print(max_number(10, 55))
# Вывод: AssertionError: a>b
print(max_number(55, 10))
# Вывод: В "Online Python Compiler" выдает правильный результат - 10, в PyCharm ругается. Скриншот прилагаю.
print(max_number(10, 10))


# Автотест для функции max_number(a, b) из первого задания
def max_number(a, b):
    assert a>=b
    return a


# Вывод: AssertionError: a<b
print(max_number(10, 55))
# Вывод: 55
print(max_number(55, 10))
# Вывод: В "Online Python Compiler" выдает правильный результат - 10, в PyCharm ругается. Скриншот прилагаю.
print(max_number(10, 10))



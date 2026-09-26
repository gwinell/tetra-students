"""Учебный модуль к седьмому уроку: функции и импорт."""


def greet(name):
    """Возвращает приветствие для указанного имени."""
    return f"Привет, {name}!"


def add_numbers(first, second):
    """Возвращает сумму двух чисел."""
    return first + second


def is_adult(age):
    """Возвращает True, если возраст не меньше 18."""
    if age >= 18:
        return True
    else:
        return False


def count_long_words(words, minimum_length):
    """Считает слова, длина которых не меньше заданной."""
    count = 0
    for word in words:
        if len(word) >= minimum_length:
            count = count + 1
    return count

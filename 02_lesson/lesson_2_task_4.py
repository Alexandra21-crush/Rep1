def fizz_buzz(n):
    """
    Функция выводит числа от 1 до n, заменяя:
    - числа, кратные 3, на 'Fizz'
    - числа, кратные 5, на 'Buzz'
    - числа, кратные и 3, и 5, на 'FizzBuzz'
    """
    for i in range(1, n + 1):
        if i % 15 == 0:  # Проверка делимости на 3 и 5 (15 = НОК 3 и 5)
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример использования
fizz_buzz(20)

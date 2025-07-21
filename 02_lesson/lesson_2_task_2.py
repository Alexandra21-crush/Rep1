def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


year = 2000  # Проверка для 2000 года (високосный)
result = is_year_leap(year)
print(f"год {year}: {result}")

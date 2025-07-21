def month_to_season(month):

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"


# Пример использования
if __name__ == "__main__":
    test_month = 2
    print(f"Месяц {test_month} это сезон: {month_to_season(test_month)}")

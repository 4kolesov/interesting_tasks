def check_leap_year(year: int) -> int:
    """Проверка високосный год или нет."""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def days_in_year(year: int) -> int:
    """Получить колечество дней в году."""
    if check_leap_year(year):
        return 366
    return 365


def get_days_in_month(year: int, month: int) -> int:
    """Получить количество дней в месяце."""
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap_year(year) and month == 2:
        return 29
    return days_in_month[month]


def get_days_between_dates(date_1: str, date_2: str) -> int:
    """Получить количество дней между датами."""
    year_1, month_1, day_1 = [int(number) for number in date_1.split('-')]
    year_2, month_2, day_2 = [int(number) for number in date_2.split('-')]

    if year_1 > year_2:
        year_1, year_2 = year_2, year_1
        month_1, month_2 = month_2, month_1
        day_1, day_2 = day_2, day_1

    if year_1 == year_2 and month_1 > month_2:
        month_1, month_2 = month_2, month_1
        day_1, day_2 = day_2, day_1

    if year_1 == year_2:
        if month_1 == month_2:
            return abs(day_2 - day_1)
        days = get_days_in_month(year_1, month_1) - day_1
        for month in range(month_1 + 1, month_2):
            days += get_days_in_month(year_1, month)
        return days + day_2
    days = get_days_in_month(year_1, month_1) - day_1
    for month in range(month_1 + 1, 13):
        days += get_days_in_month(year_1, month)
    for month in range(1, month_2):
        days += get_days_in_month(year_2, month)
    for year in range(year_1 + 1, year_2):
        days += days_in_year(year)
    days += day_2
    return days


if __name__ == '__main__':
    import unittest

    class TestBetweenDays(unittest.TestCase):
        def test_days_01(self):
            date1 = '2019-06-29'
            date2 = '2019-06-30'
            call = get_days_between_dates(date1, date2)
            result = 1
            self.assertEqual(
                call, result, 'Неправильный результат'
            )

        def test_days_02(self):
            date1 = '2020-01-15'
            date2 = '2019-12-31'
            call = get_days_between_dates(date1, date2)
            result = 15
            self.assertEqual(
                call, result, 'Неправильный результат'
            )

    unittest.main()

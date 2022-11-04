from operator import truediv


def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


days_list = [0, 30, 30, 28, 30, 31, 31, 30, 30, 31, 28, 30, 31]
# print(leap_year(2020))
def year_in_days(year, month):
    if leap_year(year) and month == 2:
        return 29
    else:
        return days_list[month]


print(year_in_days(2016, 9))

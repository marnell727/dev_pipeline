def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_days_in_month(month,year):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2:
        leap = is_leap_year(year)
        if leap:
            return 29
        else:
            return 28

def get_starting_day_of_week(month,year):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + 1) % 7

def print_month_calendar(month_string,month,year):
    m = "M"
    t = "T"
    w = "W"
    f = "F"
    s = "S"
    days_in_month = get_days_in_month(month,year)
    start_day_of_week = get_starting_day_of_week(month,year)
    month_year = f'{month_string} {str(year)}'
    print(f'{month_year:^31}\n\n{s:>4}{m:>4}{t:>4}{w:>4}{t:>4}{f:>4}{s:>4}\n')
    print('    ' * start_day_of_week, end = '')
    for day in range(1, days_in_month + 1):
        print(f'{day:>4}',end = '')
        if (day + start_day_of_week) % 7 == 0:
            print('\n')

print_month_calendar('September',9,2021)
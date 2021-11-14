def dynamic_calendar():
    month = int(input("Enter a month number (1-12): "))
    year = int(input("Enter a year after 1970: "))
    m = "M"
    t = "T"
    w = "W"
    f = "F"
    s = "S"
    month_year = month + str(year)
    print(f'{month_year:^31}\n\n{s:>4}{m:>4}{t:>4}{w:>4}{t:>4}{f:>4}{s:>4}\n')
    print('    ' * start_day_of_week, end = '')
    for day in range(1, days_in_month + 1):
        print(f'{day:>4}',end = '')
        if (day + start_day_of_week) % 7 == 0:
            print('\n')

print_month_calendar('September',2021,5,30)
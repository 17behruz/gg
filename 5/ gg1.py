def day_of_year(day, month, year):

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    return sum(days_in_month[:month-1]) + day


A = int(input("Введите число: "))
B = int(input("Введите месяц: "))
C = int(input("Введите год: "))

print("Порядковый номер даты:", day_of_year(A, B, C))
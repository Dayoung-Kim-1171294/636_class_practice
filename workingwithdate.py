import datetime
from datetime import date

x = date.today()
print(x)

#strftime: string format time
# Thursday, November 27, 2025
print(date.today().strftime("%A, %B %d, %Y"))

def get_current_time():
    return date.today()

# <class 'datetime.date'>
print(type(get_current_time()))

# create specific date
print(datetime.datetime(2000, 5, 17, 11, 23, 45))

def enter_date():
    day = input("Enter day (1-31): ")
    month = input("Enter month (1-12): ")
    year = input("Enter year (e.g., 2024): ")

    try:
        user_date = date(int(year), int(month), int(day))
        print("You entered the date:", user_date.strftime("%A, %B %d, %Y"))
    except ValueError as e:
        print("Invalid date, error:", e)
        return enter_date()

enter_date()

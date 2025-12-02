from datetime import timedelta, datetime, date

year = timedelta(days=365)
# print("One year duration:", year)

five_years = year * 5
# print(five_years.days)
five_half_years = year * 5.5
# print(five_half_years.days)

year_input = int(input ("Enter year: "))
month_input = int(input("Enter month: "))
day_input = int(input("Enter day: "))
input_date = date(year_input, month_input, day_input)
# print("Input date:", input_date)
future_date = input_date + five_years
# print ("Date after five years:", future_date)

today = date.today()
past_date = today - five_years
print("Date five years ago:", past_date)
date_diff = today - input_date
print("Difference between today and input date:", date_diff.days)
if date_diff.days > five_half_years.days:
    print("Older than five and a half years")
else:
    print("Younger than five and a half years")
from datetime import date, timedelta


year = int(input())
month = int(input())
day = 22
pycon = date(day=day, month=month, year=year)
while pycon.weekday() != 3:
    pycon += timedelta(days=1)

print(pycon.strftime('%d.%m.%Y'))
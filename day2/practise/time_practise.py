from datetime import datetime

now=datetime.now()
Day=now.day
Month=now.month
Year=now.year
Hour=now.hour
Minute=now.minute
Second=now.second

print(now)
print(Day)
print(Month)
print(Year)

formatted=now.strftime("%d/%m/%Y  %H:%M:%S")

print(formatted)


print(f"Today is day {Day} of this week and full standard format {Day}/{Month}/{Year}")




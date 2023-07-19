from datetime import datetime, timedelta
import time

# datetime - используем для работы с датами, временем
# time - более точное время но используется для работы в системе, для подсчета скорости работы ф-ций

print(time.time())  # 1689757002.235668
current_dt = datetime.now()
print(current_dt)  # 2023-07-19 11:56:42.235667

print(current_dt.year)  # 2023
print(current_dt.month)  # 7
print(current_dt.day)  # 19
print(current_dt.hour)  # 12
print(current_dt.minute)  # 0
print(current_dt.second)  # 21
print(current_dt.microsecond)  # 925352
print(current_dt.date())  # 2023-07-19
print(current_dt.time())  # 12:03:52.849982

custom_dt = datetime(year=1970, month=1, day=1, hour=0, minute=1)
print(custom_dt)  # 1970-01-01 00:01:00
print(custom_dt.weekday())  # 3
print(current_dt.weekday())  # 2

custom_dt_1 = datetime(year=1970, month=1, day=1)
custom_dt_2 = datetime(year=1970, month=1, day=2)
result = custom_dt_2 - custom_dt_1
print(result)  # 1 day, 0:00:00

custom_dt_1 += timedelta(days=1)
print(custom_dt_1)  # 1970-01-02 00:00:00

delta = timedelta(hours=1)
custom_dt_2 += delta
print(custom_dt_2)  # 1970-01-02 01:00:00

delta = timedelta(weeks=3)
custom_dt_2 += delta
print(custom_dt_2)  # 1970-01-23 01:00:00

now = datetime.now()

formated_date = now.strftime("%a %d. %m. %Y %H: %M")
print(formated_date)  # Wed 19. 07. 2023 12: 35

custom_dt = datetime.strptime(
    "Wed 19. 07. 2023 12: 35", "%a %d. %m. %Y %H: %M")

print(custom_dt)  # 2023-07-19 12:35:00

print(custom_dt.timestamp())  # 1689759300.0
print(datetime.fromtimestamp(1689759300.0))  # 2023-07-19 12:35:00

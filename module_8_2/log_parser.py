from datetime import datetime

# 22.07.2023 14:11:25 - INFO - Generating map size_m: 27 size_n: 24
log_times = []
logs = []

with open("logs.txt", "r") as f:
    for line in f:
        logs.append(line)
        time = datetime.strptime(line.split(" - ")[0], "%d.%m.%Y %H:%M:%S")
        log_times.append(time)

start_date = input("Start date  in format (dd.mm.yyyy HH:MM:SS): ")
start_date = datetime.strptime(start_date, "%d.%m.%Y %H:%M:%S")
end_date = input("End date in format (dd.mm.yyyy HH:MM:SS): ")
end_date = datetime.strptime(end_date, "%d.%m.%Y %H:%M:%S")

for log, log_time in zip(logs, log_times):
    if start_date < log_time < end_date:
        print(log)

from datetime import datetime

# уровни параметров(log_level,info_level,warning_level,error_level)


def log_message(message, log_level="INFO"):
    with open("logs.txt", "a") as f:
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f.write(f"{now} - {log_level} - {message}\n")

import re

bad_regexp = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
ips = ["0.0.0.0", "0000", "128.10.13.41", "123.45.84",
       "123,123,123,123", "12364165243", "245.520.18.17"]

for ip in ips:
    result = re.search(bad_regexp, ip)

    if result is None:
        print(f"Negative - {ip}")
    else:
        print(f"Positive - {result.group()}")

import re

regexp = r'^\+?(38)?8?[- \(]?0\d{2}[- \)]?\d{3}[- ]?\d{2}[- ]?\d{2}$'
phone_numbers = ["+380681231234", "0681245678",
                 "12345", "0681231234", "380681231234", "+38068 123 12 34", "+38(068)1231234", "+38(068)123 12 34", "068 123 12 34", "068-123-12 34", "068-123-12-34", "1 2 3", "1-2", "1 2-3", "38068123123416253", "+390681231234", "+30681231234"]

for number in phone_numbers:
    result = re.search(regexp, number)

    if result is None:
        print(f"Bad number - {number}")
    else:
        print(f"Good number - {result.group()}")

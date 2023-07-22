from datetime import datetime


def for_testing():
    my_list = []
    for i in range(0, 1000_000):
        my_list.append(i)


def comprehensions_testing():
    my_comp_list = [i for i in range(0, 1000_000)]


n = 100
for_times = []
comprehensions_times = []
for iteration in range(0, n):
    start = datetime.now().timestamp()
    for_testing()
    end = datetime.now().timestamp()
    result = end - start
    print("for results", result)
    for_times.append(result)

    start = datetime.now().timestamp()
    comprehensions_testing()
    end = datetime.now().timestamp()
    result = end - start
    print("comprehensions results", result)
    comprehensions_times.append(result)


print("for average", sum(for_times) / n)  # for average 0.18135514974594116
print("average", sum(comprehensions_times) / n)  # average 0.12320459842681884
# вывод - на данный момент comprehansions всё-таки немного быстрее

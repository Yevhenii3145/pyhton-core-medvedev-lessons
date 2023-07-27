def decorator(func):

    def inner(*args, **kwargs):

        print("Before", end=" ")
        result = func(*args, **kwargs)
        print("After", end=" ")
        return result
    return inner


@decorator
def sum(iterable, func=sum):
    print("|This is castom|", end=" ")
    return func(iterable)


# вызываем нашу кастомную задекорированную ф-ю sum
print(sum([1, 2, 3, 4, 5]))  # Before |This is castom| After 15

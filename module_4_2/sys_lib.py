import sys

print(sys.argv)
arg_1 = sys.argv[2]
print(arg_1)


def func(my_list):
    print(my_list)


a = [1, 2, 4, 5, 7]
func(a)

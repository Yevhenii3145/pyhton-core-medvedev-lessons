class OutOfBoundError(Exception):
    pass


try:
    raise OutOfBoundError("You are out of bound")
except OutOfBoundError as error:
    print(error)  # You are out of bound

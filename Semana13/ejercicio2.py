def only_numbers(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise Exception(f"argument {value} is not a number")
            
        for key, value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise Exception(f"argument {value} is not a number")

        return func(*args, **kwargs)
    return wrapper

@only_numbers
def add(a, b):
    return a + b

print(add(3, 4))
print(add(3, "hola"))
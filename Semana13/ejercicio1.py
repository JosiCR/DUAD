def print_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"calling function: ¨{func.__name__}")
        print(f"arguments: {args}")
        print(f"keyword  arguments: {kwargs}")
        
        result = func(*args, **kwargs)

        print(f"returned: {result}")
        return result
    return wrapper

@print_params_and_return
def add_number(a, b):
    return a + b

add_number (3, 5)
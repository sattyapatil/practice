from functools import wraps


def add_new(*args, **kwargs):
    num = kwargs['value']

    def decorator_function(func):

        @wraps(func)
        def wrapper_function(*args, **kwargs):

            result = func(*args, **kwargs) * num

            return result

        return wrapper_function
    return decorator_function


@add_new(value=6)
def sum_of(a, b):
    return a+b


result = sum_of
print(result)




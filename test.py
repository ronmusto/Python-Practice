import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function {func.__name__} called with arguments {args}, {kwargs}. Execution time: {duration: .4f} seconds.")
        return result
    return wrapper    
@log_decorator
def test_func(a, b):
    return a + b

# Test the decorated function
test_func(5, 3)
import functools
import time

def retry(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == retries - 1:
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator


if __name__ == "__main__":
    @retry(retries=2, delay=0.5)
    def test_func():
        return "Успешно"
    print(test_func())

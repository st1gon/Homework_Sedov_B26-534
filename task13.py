import time
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"Время выполнения: {time.perf_counter() - self.start_time:.4f} с")
        return False


@contextmanager
def timer():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        print(f"Время выполнения: {time.perf_counter() - start_time:.4f} с")


def some_function():
    sum(range(5_000_000))


with Timer():
    some_function()

with timer():
    some_function()

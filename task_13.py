import time
from contextlib import contextmanager


def some_function():
    time.sleep(0.5)


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f"Время выполнения: {self.end - self.start:.4f} сек.")


@contextmanager
def Timer_gen():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"Время выполнения: {end - start:.4f} сек.")


print("Через класс:")
with Timer():
    some_function()

print("\nЧерез contextmanager:")
with Timer_gen():
    some_function()
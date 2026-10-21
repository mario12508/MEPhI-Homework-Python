from contextlib import contextmanager


@contextmanager
def log_operation(filename, operation):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"START: {operation}\n")
        f.flush()
        try:
            yield
        except Exception:
            f.write(f"ERROR: {operation}\n")
            f.flush()
            raise
        else:
            f.write(f"END: {operation}\n")
            f.flush()


with log_operation("operation.log", "Data processing"):
    print("Выполняется обработка данных...")

print("\nПроверка с исключением:")
try:
    with log_operation("operation.log", "Data processing"):
        raise ValueError("Что-то пошло не так")
except ValueError as e:
    print(f"Исключение перехвачено снаружи: {e}")

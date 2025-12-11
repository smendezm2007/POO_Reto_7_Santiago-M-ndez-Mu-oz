import time
from functools import wraps


def timing(label: str | None = None):
    """Decorador para medir el tiempo de ejecucion de una funcion."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            name = label or func.__name__
            print(f"[Timing] {name} tomo {elapsed:.4f} ms")
            return result
        return wrapper
    return decorator

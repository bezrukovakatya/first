from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """Декоратор. Считает и выводит количество вызовов декорируемой функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('Функция {func} была вызвана: {count} раз'.format(
            func=func.__name__, count=wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('this is test code/\\')


test()
test()
test()
test()

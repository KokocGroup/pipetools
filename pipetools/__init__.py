from collections import defaultdict
from functools import wraps


def groupby(func):
    @wraps(func)
    def wrapper(iterable):
        result = defaultdict(list)
        for item in iterable:
            result[item].append(item)
        return zip(result.keys(), map(func, result.values()))
    return wrapper


def sort(func, **kwargs):
    @wraps(func)
    def wrapper(iterable):
        return sorted(iterable, key=func, reverse=kwargs.get('reverse', False))
    return wrapper


def select(func):
    @wraps(func)
    def wrapper(iterable):
        return filter(func, iterable)
    return wrapper


class List(list):
    def __or__(self, op):
        if hasattr(op, 'func_globals') and op.func_globals['__package__'] == 'pipetools':
            return List(op(self))
        return List(map(op, self))



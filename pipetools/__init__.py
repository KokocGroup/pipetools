from functools import wraps


def groupby(func):
    @wraps(func)
    def wrapper(iterable):
        iterable = List(iterable)
        current_group = []
        result = []
        for num, item in enumerate(sorted(iterable)):
            if num != 0:
                if item not in current_group:
                    result.append((current_group[0], func(current_group)))
                    current_group = [item]
                    continue
            current_group.append(item)
        return List(result)

    return wrapper


def sort(func, **kwargs):
    @wraps(func)
    def wrapper(iterable):
        return List(sorted(iterable, key=func, reverse=kwargs.get('reverse', False)))
    return wrapper


def select(func):
    @wraps(func)
    def wrapper(iterable):
        return List(filter(func, iterable))
    return wrapper


class List(list):
    def __or__(self, op):
        if hasattr(op, 'func_globals') and op.func_globals['__package__'] == 'pipetools':
            return List(op(self))
        return List(map(op, self))



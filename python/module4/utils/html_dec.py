from functools import wraps


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text_message = func(*args, **kwargs)
        return f'<b>{text_message}</b>'
    return wrapper


def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text_message = func(*args, **kwargs)
        return f'<i>{text_message}</i>'
    return wrapper


def underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text_message = func(*args, **kwargs)
        return f'<u>{text_message}</u>'
    return wrapper

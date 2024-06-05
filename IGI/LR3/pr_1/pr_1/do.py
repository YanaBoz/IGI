def funcInfoDec(func):
    """Prints name and documentation of a current function."""
    def wrapper(*args, **kwargs):
        print(f'Сalling {func.name}() that {func.doc}')
        result = func(*args, **kwargs)
        return result
    return wrapper
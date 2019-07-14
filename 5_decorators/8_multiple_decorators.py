def add_brackets(func):
    def wrapper(name):
        return f"[ {func(name)} ]"

    return wrapper


def add_arrows(func):
    def wrapper(name):
        return f" ==> {func(name)} <== "

    return wrapper


def add_stars(func):
    def wrapper(name):
        return f" * {func(name)} * "

    return wrapper


def make_hawaii(func):
    def wrapper(name):
        return f"{func(name).replace('Hello', 'Aloha')}"

    return wrapper


@make_hawaii
@add_stars
@add_arrows
@add_brackets
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))

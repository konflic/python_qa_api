def make_cool(func):
    def wrapper(name):
        return f"[ * ==> {func(name).replace('Hello', 'Hey')} <== *]"

    return wrapper


@make_cool
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy!"))

def hello_function(name):
    return f"Hello, {name}"


def make_cool(func):
    def wrapper(name):
        return f"[ * ==> {func(name).replace('Hello', 'Hey')} <== *]"

    return wrapper


cool_hello = make_cool(hello_function)

print(hello_function("Vasiliy!"))
print(cool_hello("Vasiliy"))

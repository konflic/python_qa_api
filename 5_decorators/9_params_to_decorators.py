def localization(region):
    if region == "Italy":
        ln_hello = "Ciao"
    elif region == "Russia":
        ln_hello = "Privet"
    elif region == "Hawaii":
        ln_hello = "Aloha"
    else:
        raise Exception("Region is not supported!")

    def decorator(func):
        def wrapper(name):
            return f"{func(name).replace('Hello', ln_hello)}"

        return wrapper

    return decorator


@localization("Italy")
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))


@localization("Russia")
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))


@localization("Hawaii")
def hello_function(name):
    return f"Hello, {name}"


print(hello_function("Vasiliy"))


# Второй пример, почти как в pytest

def numbers(*args, **kwargs):
    def decorator(func):
        for item in args:
            func(item)
        # for key, value in enumerate(kwargs):
        #     print(key, value)

    return decorator


@numbers(1, 2, 3, 4, 5, 6, 7)
def equality_test(n, target=3):
    try:
        assert n > target
        print(f"Correct: {n} is greater than {target}")
    except AssertionError:
        print(f"Wrong: {n} is less than {target}")

def cool_hello(name: str):
    def make_hello(some_name):
        return f'Hello, {some_name}'

    return f"[ * ===> {make_hello(name)} <=== * ]"


# Смотрим что получилось
print(cool_hello('Vasiliy'))

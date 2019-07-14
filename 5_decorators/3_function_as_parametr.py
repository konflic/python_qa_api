def make_hello(name: str):
    return f'Hello, {name}'


def make_bye_bye(name: str):
    return f'Bye Bye, {name}'


# Делаем функцию, которая вызывает внутри себя функцию
def vasiliy_passer(func):
    name = "Vasiliy"
    return func(name)


print(vasiliy_passer(make_hello))
print(vasiliy_passer(make_bye_bye))

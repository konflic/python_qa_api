def make_hello(name: str):
    return f'Hello, {name}'


# Записали функцию в переменную
some_variable = make_hello

# Вызвали функцию из переменной
print(some_variable('Vasiliy'))

def function_return_function():
    def inner_function():
        print("Hi, I'm inner function!")

    return inner_function


# Сохраняем функцию в переменную
some_variable = function_return_function()

print(some_variable())

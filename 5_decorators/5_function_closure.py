def comp_great_function(name):
    def inner_function():
        return f"Hello, {name}"

    return inner_function


great_vasiliy = comp_great_function("Vasiliy")

print(great_vasiliy())

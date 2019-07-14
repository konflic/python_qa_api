def foo(variable):
    return 4 + variable


for el in dir(foo):
    print(el)

# import  dis
# print(foo.__name__)
# print(foo.__code__.co_varnames)
# print(foo.__code__.co_filename)
# print(dis.dis(foo.__code__.co_code))


# def foo_with_args(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return "--------------"
#
# print(foo_with_args())
# print(foo_with_args(1, 2, "Booo", {}))
# print(foo_with_args(one=1, two=2, string="Booo", dicctionary={}))
# print(foo_with_args(1, 2, "Booo", {}, one=1, two=2, string="Booo", dicctionary={}))

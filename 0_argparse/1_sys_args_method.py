import sys

print(sys.argv)

args = sys.argv


def calculate(num1, num2):
    return num1 + num2


print(calculate(args[1], args[2]))

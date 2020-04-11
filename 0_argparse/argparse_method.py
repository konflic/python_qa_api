import argparse

parser = argparse.ArgumentParser()

"""
    Все параметры для add_argument
    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().

"""

parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET',
                    choices=['GET', 'POST'])

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

# Если параметр передан то Ture, иначе False
parser.add_argument('--true', '-t',
                    action='store_true',
                    help='True or false param',
                    required=False)

# Парсим всё что положили
args = parser.parse_args()

# Это словарь из которого аргументы можно доставать
print(args)

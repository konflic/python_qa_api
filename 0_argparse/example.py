import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--schema',
                    help='schema',
                    type=str,
                    default='https',
                    choices=['http', 'https'])

parser.add_argument('--host',
                    help='host',
                    type=str,
                    default="localhost")

# Если параметр передан то Ture, иначе False
parser.add_argument('--path',
                    default='/',
                    type=str,
                    help='True or false param',
                    required=False)

def url_maker(schema, host, path):
    return schema + "://" + host + path


args = parser.parse_args()

print(url_maker(args.schema, args.host, args.path))

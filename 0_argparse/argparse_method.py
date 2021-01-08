import argparse

# First, create parser object
parser = argparse.ArgumentParser()

# Second, define arguments
parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET',
                    choices=['GET', 'POST'])

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request',
                    required=True)

parser.add_argument('--secure', '-s',
                    action='store_true',
                    help='True or False param',
                    required=False)

# Parse passer arguments to args variable
args = parser.parse_args()

# Lets see the content
print("All params available:", args)

print(f"""
Arguments passed to script:
-m (--method) = {args.method}
-u (--url) = {args.url}
-s (--secure) = {args.secure}
""")
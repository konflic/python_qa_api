"""Script for creating url based on script parameters"""
import argparse
import requests

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

parser.add_argument('--path',
                    default='/',
                    type=str,
                    help='Path to make request on host',
                    required=False)


def url_maker(schema, host, path):
    url = schema + "://" + host + path
    print(f"Created url: {url}")
    return url


args = parser.parse_args()

response = requests.get(url=url_maker(args.schema, args.host, args.path))

print("Got response status code:", response.status_code)

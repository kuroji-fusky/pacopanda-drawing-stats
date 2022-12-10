import argparse
import json

parser = argparse.ArgumentParser(
    description="Generate Redis environment stuff")

parser.add_argument(
    "-pswd",
    "--password",
    help="Redis password",
    required=True
)
parser.add_argument("-U",
                    "--username",
                    help="username to the redis database",
                    required=True)

parser.add_argument("-H",
                    "--host",
                    help="host of the redis database",
                    required=True)

parser.add_argument("-P",
                    "--port",
                    help="port of the redis database",
                    required=True)

args = parser.parse_args()
username: str = args.username
password: str = args.password
host: str = args.host
port: str = args.port


def redis_parser():
    url_base = "redis://"

    if password is None:
        return f"{url_base}{username}@{host}:{port}"

    return f"{url_base}{username}:{password}@{host}:{port}"


redis_config_json = {
    "username": username,
    "password": password,
    "host": host,
    "port": port,
}

with open("redis_config.json", "w") as f:
    json.dump(redis_config_json, f)

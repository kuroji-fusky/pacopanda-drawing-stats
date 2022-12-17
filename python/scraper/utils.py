from colorama import Back, Fore, Style
import redis
import json

"""For adding fancy colors to the console"""
clear = Style.RESET_ALL
b_red, b_green, b_yellow = Back.LIGHTRED_EX, Back.LIGHTGREEN_EX, Back.LIGHTYELLOW_EX
f_red, f_green, f_yellow = Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX


def success_msg(msg: str):
    print(f"{f_green}{msg}{clear}")


def warn_msg(msg: str):
    print(f"{f_yellow}{msg}{clear}")


def error_msg(msg: str):
    print(f"{f_red}{msg}{clear}")

def connect_redis(filepath: str):
    print("Connecting to redis...")
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
    
        cfg_host: str = config["host"]
        cfg_port: int = int(config["port"])
        cfg_username: str = config["username"]
        cfg_password: str = config["password"]

        if cfg_password is None:
            cfg_password = ''

        RedisDB = redis.StrictRedis(
            host=cfg_host,
            port=cfg_port,
            username=cfg_username,
            password=cfg_password,
            decode_responses=True
        )
    # i'm gonna go take a tea break, brb kuro :3
    # k lol
    except FileNotFoundError:
        print("file not found")
    return RedisDB

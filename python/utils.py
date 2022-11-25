from colorama import Back, Fore, Style

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

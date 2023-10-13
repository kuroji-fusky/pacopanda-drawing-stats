from typing import Any
import argparse
from parinton.logger import PacoLogger
from utils import load_file, save_file, is_empty_string
from exceptions import CharacterParseError

logger = PacoLogger(time=True)

parser = argparse.ArgumentParser(
    description="Generate list of characters to parse")

parser.add_argument("-A", "--add",
                    type=str,
                    nargs="+",
                    help="Adds a character")

parser.add_argument("-D", "--delete",
                    type=str,
                    help="Deletes a character")

parser.add_argument("-R", "--reset",
                    action="store_true",
                    help="Removes all applied character data")

args = parser.parse_args()


filename = "characters.json"


def set_char_data(data: list[str | Any]) -> None:
    msg = "This file is auto-generated using `characters.py`, do not modify it directly!"

    output = {
        "$$msg": msg,
        "data": data
    }

    save_file(output, filename, indent=True)


def main():
    char_data = []

    # -------------------------
    # Initial load
    # -------------------------
    try:
        _data = load_file(filename)
        char_data.extend(_data["data"])

    except FileNotFoundError:
        logger.log("info", "File not found, creating file")
        set_char_data([])

    # Exception to prevent from argument collsion
    add_args: list[str] = args.add
    reset_arg: bool = args.reset

    if reset_arg and add_args:
        raise Exception("Can't use both flags for reseting and adding data.")

    # -------------------------
    # Reset items
    # -------------------------
    if reset_arg:
        set_char_data([])

        logger.log("info", "All data wiped!")
        return

    # -------------------------
    # Parse items
    # -------------------------
    if not add_args:
        raise Exception(
            "--add flag required. Pass the --add or -A to add a character")

    if add_args and len(add_args) < 1:
        raise Exception("Provide at least one item")

    for arg_item in add_args:
        try:
            name, species = arg_item.split(":")
        except ValueError:
            raise CharacterParseError("Unable to parse arguments specified")

        if is_empty_string(species):
            raise CharacterParseError(
                f"Character \"{name}\" has no species specified.")

        # Add an exception here if there's a matching character name from `char_data`
        existing_names = [character["name"] for character in char_data]
        if name in existing_names:
            raise CharacterParseError(
                f"Character with name '{name}' already exists")

        out = {
            "name": name,
            "species": species,
        }

        char_data.append(out)
        logger.log(
            "info", f"Saved character \"{name}\", with species \"{species}\"")

    set_char_data(char_data)


if __name__ == "__main__":
    main()

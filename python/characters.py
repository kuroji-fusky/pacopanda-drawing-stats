import sys
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
                    help="adds a character")

parser.add_argument("-D", "--delete",
                    action="store_true",
                    help="deletes a character")

parser.add_argument("-R", "--reset",
                    action="store_true",
                    help="removes all applied character data")

parser.add_argument("--stats",
                    action="store_true",
                    help="shows a break down of all the characters")


args = parser.parse_args()


filename = "characters.json"


def set_char_data(data: list[str, Any]) -> None:
    output = {
        "$msg": "This file is auto-generated, do not modify it directly!",
        "data": data
    }

    save_file(output, filename, indent=True)


def main():
    char_data = []

    # -------------------------
    # Initial load
    # -------------------------
    try:
        char_data.extend(load_file(filename)["data"])

    except FileNotFoundError:
        logger.log("info", "File not found, creating file")
        set_char_data([])

    if args.stats:
        unique_values = {}

        for cd in char_data:
            for k, v in cd.items():
                unique_values.setdefault(k, set()).add(v)

        total_count = len(char_data)
        unique_species_count = len(unique_values.get("species"))

        print(total_count, unique_species_count)

    # Exception to prevent from argument collsion
    add_args: list[str] = args.add
    reset_arg: bool = args.reset

    if reset_arg and add_args:
        raise Exception(
            "Can't use both 'add' and 'reset' flags for reseting and adding data.")

    # Reset items
    if reset_arg:
        set_char_data([])

        logger.log("info", "All data wiped!")
        return

    if not add_args:
        return

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
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()

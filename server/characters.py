import argparse
from pydantic import BaseModel
from parinton.logger import PacoLogger
from utils import load_file, save_file

logger = PacoLogger(time=True)

parser = argparse.ArgumentParser(
    description="Generate list of characters to parse")

parser.add_argument("-A", "--add",
                    required=True,
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


class Character(BaseModel):
    name: str
    species: str
    is_hybrid: bool


def main():
    char_filename = "characters.json"
    char_data = []
    initial_data = {
        "$$msg": "This file is auto-generated using `characters.py`, do not modify it directly!",
        "data": []
    }

    try:
        _data = load_file(char_filename)
        char_data.extend(_data["data"])

        print(char_data)

    except FileNotFoundError:
        logger.log("info", "File not found, creating file")
        save_file(initial_data, char_filename, indent=True)

    print(args.add)


if __name__ == "__main__":
    main()

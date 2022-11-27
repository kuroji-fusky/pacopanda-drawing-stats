import json
import re

from utils import error_msg


def main():
  """
  + Parse all the characters listed from characters.json
    This had to be hard-coded for testing purposes
  """
  try:
    with open("characters.json", "r") as c, open("data.json", "r") as d:
      character_json = json.load(c)
      artworks_json = json.load(d)
      
  except Exception as e:
      error_msg(e)

if __name__ == "__main__":
  main()

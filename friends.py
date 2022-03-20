import argparse
import json
import sys
from dataclasses import dataclass


@dataclass
class Config:
    excludes: str


def main(argv):
    parser = argparse.ArgumentParser(prog="friends")
    parser.add_argument('-n', '--nickname', required=True, type=str, help="Nickname of player to delete friends")
    parser.add_argument('-c', '--config', required=True, type=str, help="Path to config file")
    args = parser.parse_args(argv[1:])

    print(f"args={args}")

    with open(args.config, "rt") as config_file:
        text = config_file.read()
        config_data = json.loads(text)

    config = Config(**config_data)

    print(config.excludes)

    # for friend in faceit.requiest_friends(args.nickname):
    #     if friend not in config.excludes:
    #         faceit.delete_friend(args.nickname, friend)


    # excludes = input("Input excludes: ")
    # excludes = [it.strip() for it in excludes.split(",")]
    # print(excludes)


if __name__ == '__main__':
    main(sys.argv)

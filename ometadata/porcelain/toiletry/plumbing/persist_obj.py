
from argparse import ArgumentParser
from importlib import import_module
from types import ModuleType
from typing import Callable, Optional
from shlex import quote, split

from .sewer.utils.types import CLIargs


def parse_args(received_args: Optional[CLIargs]):
    parser = ArgumentParser(description=".")
    parser.add_argument(
        "--database", help="Database name."
    )
    parser.add_argument(
        "--obj", action="store", type=str, help="Image object in JSON."
    )
    parser.add_argument(
        "-J", "--jobs", type=int, default=0, help="Number of threads."
    )

    if received_args is not None:
        args = parser.parse_args(received_args)
    else:
        args = parser.parse_args()
    return args


def import_relevant_module(db: str) -> Callable[[CLIargs], str]:
    sewer_package_python_path = "ometadata.porcelain.toiletry.plumbing.sewer"
    module_name = f"persist_obj_{db}"
    chosen_module: ModuleType = import_module(f".{module_name}", sewer_package_python_path)
    database_connection = chosen_module.get_database()
    return database_connection


def generate_key(received_args: Optional[CLIargs] = None) -> str:
    args = parse_args(received_args)
    database_conn = import_relevant_module(args.database)
    key = database_conn.save(split(f"--image_path {quote(args.image_path)}"))
    return key


def main():
    output = generate_key()
    print(output)


if __name__ == "__main__":
    main()
 

from argparse import ArgumentParser
from importlib import import_module
from json import dumps
from pathlib import Path
from types import ModuleType
from typing import Callable, Optional

from .plumbing.sewer.utils.types import CLIargs


def parse_args(received_args: Optional[CLIargs]):
    parser = ArgumentParser(description=".")
    parser.add_argument(
        "--backend", action="store", type=str, help="."
    )
    parser.add_argument(
        "--hash_function", action="store", type=str, help="."
    )
    parser.add_argument(
        "--image_path", action="store", type=Path, help="Image file path."
    )
    parser.add_argument(
        "-J", "--jobs", type=int, default=0, help="Number of threads."
    )

    if received_args is not None:
        args = parser.parse_args(received_args)
    else:
        args = parser.parse_args()
    return args


def import_key_backend() -> Callable[[CLIargs], str]:
    plumbing_package_python_path = "ometadata.porcelain.toiletry.plumbing"
    module_name = f"get_image_hash"
    backend = import_module(f".{module_name}", plumbing_package_python_path)
    generate_key_function = backend.generate_key
    return generate_key_function


def create_image_obj(received_args: Optional[CLIargs] = None) -> str:
    args = parse_args(received_args)
    generate_key = import_key_backend()
    image_key = generate_key(received_args)
    metadata = {"original-filename": args.image_path.name}
    return dumps({image_key: metadata})


def main():
    output = create_image_obj()
    print(output)


if __name__ == "__main__":
    main()
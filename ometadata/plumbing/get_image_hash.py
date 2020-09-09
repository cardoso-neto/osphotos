
from argparse import ArgumentParser
from importlib import import_module
from types import ModuleType
from typing import Callable, Optional
from shlex import quote, split

from .sewer.utils.types import CLIargs


def parse_args(received_args: Optional[CLIargs]):
    parser = ArgumentParser(description=".")
    parser.add_argument(
        "--backend", action="store", type=str, help="."
    )
    parser.add_argument(
        "--hash_function", action="store", type=str, help="."
    )
    parser.add_argument(
        "--image_path", action="store", type=str, help="Image file path."
    )
    parser.add_argument(
        "-J", "--jobs", type=int, default=0, help="Number of threads."
    )

    if received_args is not None:
        args = parser.parse_args(received_args)
    else:
        args = parser.parse_args()
    return args


def import_backend(backend: str, hash_function: str) -> Callable[[CLIargs], str]:
    sewer_package_python_path = "ometadata.porcelain.toiletry.plumbing.sewer"
    module_name = f"get_image_hash_{backend}_{hash_function}"
    chosen_backend: ModuleType = import_module(f".{module_name}", sewer_package_python_path)
    generate_key_function = chosen_backend.generate_key
    return generate_key_function


def generate_key(received_args: Optional[CLIargs] = None) -> str:
    args = parse_args(received_args)
    chosen_generate_key = import_backend(args.backend, args.hash_function)
    key = chosen_generate_key(split(f"--image_path {quote(args.image_path)}"))
    return key


def main():
    output = generate_key()
    print(output)


if __name__ == "__main__":
    main()
 
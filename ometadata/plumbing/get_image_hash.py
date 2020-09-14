
from argparse import ArgumentParser
from importlib import import_module
from types import ModuleType
from typing import Callable, Dict, Optional
from sys import argv as command_line_arguments

from ometadata.utils.custom_types import CLIargs
from ometadata.utils.external_program_interface import is_on_path, kwargs_to_cli_args, run_command


def parse_args(received_args: CLIargs):
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
    args = parser.parse_args(received_args)
    return args


def import_backend(backend: str, hash_function: str) -> Callable[[CLIargs], str]:
    sewer_package_python_path = "ometadata.sewer"
    module_name = f"get_image_hash_{backend}_{hash_function}"
    chosen_backend: ModuleType = import_module(f".{module_name}", sewer_package_python_path)
    generate_key_function = chosen_backend.generate_key
    return generate_key_function


class FileHasher:
    base_command = "get_image_hash_{backend}_{hash_function}"
    def __init__(self, args_dict: Dict[str, str]):
        super().__init__()
        self.command = self.base_command.format(**args_dict)
        if not is_on_path(self.command):
            raise ValueError("It seems you don't undestand how $PATH works, huh?! Or maybe you just can't spell for shit...")

    def hash_image(self, **kwargs) -> str:
        args = kwargs_to_cli_args(**kwargs)
        return run_command([self.command, *args])


def generate_key(received_args: Optional[CLIargs] = None) -> str:
    if received_args is None:
        received_args = command_line_arguments[1:]
    args = parse_args(received_args)
    file_hasher = FileHasher(vars(args))
    key = file_hasher.hash_image(image_path=args.image_path)
    return key


def main():
    output = generate_key()
    print(output.strip())


if __name__ == "__main__":
    main()
 
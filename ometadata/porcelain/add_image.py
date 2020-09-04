
from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
from typing import Callable, Optional

from .toiletry.plumbing.sewer.utils.types import CLIargs


def parse_args(received_args: Optional[CLIargs] = None):
    parser = ArgumentParser(description="Add image to metadata control.")
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


def import_image_obj_creator() -> Callable[[CLIargs], str]:
    toiletry_package_python_path = "ometadata.porcelain.toiletry"
    module_name = "create_image_obj"
    create_image_obj_module = import_module(f".{module_name}", toiletry_package_python_path)
    create_image_obj_function = create_image_obj_module.create_image_obj
    return create_image_obj_function


def add_image_to_metadata_control(received_args: Optional[CLIargs] = None) -> str:
    args = parse_args(received_args)
    create_image_obj = import_image_obj_creator()
    image_obj = create_image_obj(received_args)
    
    return f"{args.image_path}: OK"


def main():
    output = add_image_to_metadata_control()
    print(output)


if __name__ == "__main__":
    main()

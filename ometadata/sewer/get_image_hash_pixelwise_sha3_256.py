
from argparse import ArgumentParser
from hashlib import sha3_256
from pathlib import Path
from typing import Optional
from sys import argv as command_line_arguments

from imageio import imread
from imageio.core.util import Array
from multibase import encode

from ometadata.utils.custom_types import CLIargs, HashlibHash


def parse_args(received_args: CLIargs):
    parser = ArgumentParser(
        description="Hash image using only its pixels with sha3 256bits."
    )
    parser.add_argument(
        "--image_path", action="store", type=Path, help="Image file path."
    )
    args = parser.parse_args(received_args)
    return args


def check_path(path: Path) -> bool:
    # avoid nasty FileNotFoundError
    path = path.resolve()
    if not path.is_file():
        raise ValueError(f"File could not be found at {str(path)!r}.")
    # TODO: check filetype? path.suffix


def hash_image_pixels(image: Array, hash_function: HashlibHash) -> bytes:
    pixel_bytes_stream = image.tobytes()
    digest = hash_function(pixel_bytes_stream).digest()
    return digest


def generate_key(received_args: Optional[CLIargs] = None) -> str:
    if received_args is None:
        received_args = command_line_arguments[1:]
    args = parse_args(received_args)
    check_path(args.image_path)
    image: Array = imread(args.image_path)
    digest = hash_image_pixels(image, sha3_256)
    b58digest: bytes = encode("base58btc", digest)
    # TODO: rotated images are generating different keys. Is that ok?
    h, w, c = image.shape
    # TODO: use multihash
    return f"pixelwise-{h}-{w}-{c}--sha3_256--{b58digest.decode('utf-8')}"


def main():
    output = generate_key()
    print(output)


if __name__ == "__main__":
    main()

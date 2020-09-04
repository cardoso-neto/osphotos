
from argparse import ArgumentParser
from hashlib import sha3_256
from pathlib import Path
from typing import Optional

from imageio import imread
from imageio.core.util import Array
from multibase import encode

from .utils.types import CLIargs, HashlibHash


def parse_args(received_args: Optional[CLIargs]):
    parser = ArgumentParser(description=".")
    parser.add_argument(
        "--image_path", action="store", type=Path, help="Image file path."
    )

    if received_args is not None:
        args = parser.parse_args(received_args)
    else:
        args = parser.parse_args()
    return args


def hash_image_pixels(image: Array, hash_function: HashlibHash) -> bytes:
    pixel_bytes_stream = image.tobytes()
    digest = hash_function(pixel_bytes_stream).digest()
    return digest


def generate_key(received_args: Optional[CLIargs] = None) -> str:
    args = parse_args(received_args)
    image: Array = imread(args.image_path)
    digest = hash_image_pixels(image, sha3_256)
    b58digest: bytes = encode("base58btc", digest)
    h, w, c = image.shape
    # TODO: use multihash
    return f"pixelwise-{h}-{w}-{c}--sha3_256--{b58digest.decode('utf-8')}"


def main():
    output = generate_key()
    print(output)


if __name__ == "__main__":
    main()

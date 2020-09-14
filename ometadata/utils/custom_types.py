
from typing import List, Union


CLIargs = List[str]


# hashlib type stubs, slightly-modified excerpt
BytesStream = Union[bytes, bytearray, memoryview]


class HashlibHash(object):
    block_size: int
    digest_size: int
    name: str
    def __init__(self, data: BytesStream = ...) -> None: ...
    def copy(self) -> "HashlibHash": ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def update(self, arg: BytesStream) -> None: ...

import setuptools
from typing import List


def read_multiline_as_list(file_path: str) -> List[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = read_multiline_as_list("requirements.txt")
# classifiers = read_multiline_as_list("classifiers.txt")

packages = setuptools.find_packages()  # ['ometadata']

setuptools.setup(
    name="ometadata",
    version="0.0.1",
    author="Nei Cardoso de Oliveira Neto",
    author_email="nei.neto@hotmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cardoso-neto/osphotos",
    packages=packages,
    # classifiers=classifiers,
    keywords='git annex external remote manyzips zip',
    entry_points = {
        'console_scripts': [
            'get_image_hash_pixelwise_sha3_256=ometadata.sewer.get_image_hash_pixelwise_sha3_256:main',
            'get_image_hash=ometadata.plumbing.get_image_hash:main',
            'create_image_obj=ometadata.toiletry.create_image_obj:main'
        ],
    },
    python_requires=">=3.8",
    install_requires=requirements,
)

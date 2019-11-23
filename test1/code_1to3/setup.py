import setuptools
from code_1to3 import program

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codesignal 1to4-srikanth gummadi", # Replace with your own username
    version="0.0.1",
    author="srikanthgummadi",
    author_email="srikanth0466@gmail.com",
    description="codesignal 1_4_prog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gummadi-srikanth/code",
    packages=setuptools.find_packages(program),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
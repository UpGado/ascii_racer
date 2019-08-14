import setuptools
import pypandoc

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='asciiracer',
    version='0.1',
    author='Ahmed Gado',
    author_email='ahmedehabg@gmail.com',
    description='A racing game that runs in terminal',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/UpGado/ascii_racer',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

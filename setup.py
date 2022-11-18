from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

about = {}
exec(open(path.join(here, '__init__.py')).read(), about)

with open(path.join(here, 'README.md')) as file:
    long_description = file.read()

setup(
    name='steg',
    version=about['__version__'],
    description='steg 🐕 is an easy to use python 🐍 library for requests',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    package_dir={"steg": "steg"},
    entry_points={"console_scripts": ["steg=steg._steg:run"]},
    author='Rayan25062011',
    url='https://github.com/Rayan25062011/Steg',
    packages=find_packages(),
    license='Apache-2.0 License',
    install_requires=[
        None
    ],
)

from setuptools import setup
import os

VERSION = "0.4"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="steggy",
    description="Steggy is a python library for requests",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Rayan Haddad",
    url="https://github.com/Rayan25062011/steggy",
    project_urls={
        "Issues": "https://github.com/Rayan25062011/steggy/issues",
        "CI": "https://github.com/Rayan25062011/steggy/actions",
        "Changelog": "https://github.com/Rayan25062011/steggy/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["steg"],
    entry_points="""
        [console_scripts]
        steggy=steg
    """,
    install_requires=["os", "requests", "sys"],
    extras_require={"test": ["os", "requests", "sys"]},
    python_requires=">=3.6",
)

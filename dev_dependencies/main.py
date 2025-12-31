import sys

from . import __version__


def run() -> None:
    print("In run...", __version__)
    print(sys.argv)

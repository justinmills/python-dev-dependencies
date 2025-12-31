import sys

from . import __version__


def run() -> None:
    print("In run...", __version__)
    print(sys.argv)


if __name__ == "__main__":
    print(f"Python dev dependencies, version {__version__}")

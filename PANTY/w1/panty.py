from rich.traceback import install
from src.utils.ban import bann1, bann2
from src.tut.p1 import func1

install(show_locals=True)


def main():
    bann1("p1.py - func1")
    func1()


if __name__ == "__main__":
    main()

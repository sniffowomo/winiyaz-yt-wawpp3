from rich.traceback import install
from src.utils.ban import banner
from src.tut.p6 import func6


install(show_locals=True)


def main():
    banner("Running p4.py - func4")
    func6()


if __name__ == "__main__":
    main()

from rich.traceback import install
from src.utils.ban import banner
from src.tut.p5 import func5


install(show_locals=True)


def main():
    banner("Running p4.py - func4")
    func5()


if __name__ == "__main__":
    main()

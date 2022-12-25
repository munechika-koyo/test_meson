"""Main module for test library to try meson build
"""
import sys
from pathlib import Path
from lib1 import test_mod1 as tm
from lib2.test_mod2 import TestClass2

sys.path.append(Path(__file__).parent)

__all__ = ["main"]


def main() -> None:
    tm.hello_cython()

    test = TestClass2(1, 2, 3)
    test.print_result()


if __name__ == "__main__":
    main()

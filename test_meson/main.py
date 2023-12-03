"""Main module for test built module by meson."""
import sys
from pathlib import Path

from .lib1 import module as mod
from .lib2.module import TestClass2

sys.path.append(Path(__file__).parent)

__all__ = ["main"]


def main() -> None:
    mod.hello_cython()

    test = TestClass2(1, 2, 3)
    test.print_result()


if __name__ == "__main__":
    main()

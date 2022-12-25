"""main module for cython
"""
from libc.stdio cimport printf

from .lib1 cimport test_mod1 as tm1

__all__ = ["main"]


cpdef void main():
    tm1.hello_cython()
    printf("test_mod1.hello_cython was called!")

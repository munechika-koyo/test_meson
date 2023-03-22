"""main module for cython
"""
from libc.stdio cimport printf

from .lib1 cimport module as mod

__all__ = ["main"]


cpdef void main():
    mod.hello_cython()
    printf("test_mod1.hello_cython was called!")

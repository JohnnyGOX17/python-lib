#!/usr/bin/env python3
#
# Runs tests for pytest usage (matches test_* format)
#
from . import binary_search


def test_key_in_list():
    sorted_list = [0, 1, 4, 5, 41, 42, 43, 55]
    key = 42
    index = binary_search.binary_search(key, sorted_list)
    assert key == sorted_list[index], "Key does not match expected!"


def test_key_not_in_list():
    sorted_list = [0, 1, 4, 5, 41, 42, 43, 55]
    key = 47
    index = binary_search.binary_search(key, sorted_list)
    assert index == -1, "Key does not match expected!"


if __name__ == "__main__":
    test_key_in_list()
    test_key_not_in_list()

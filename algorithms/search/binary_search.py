#!/usr/bin/env python3

# Using Python type hints (ver. >=3.5): https://docs.python.org/3/library/typing.html
def binary_search(key: int, sorted_collection: "list[int]") -> int:
	""" Traditional Binary Search algorithm in pure Python

	**Note:** `sorted_collection` must be in ascending order.

	:param key: integer value to search for
	:param sorted_collection: pre-sorted list of integers
	:return: index of key in list, or -1 if not found
	"""
	lo = 0
	hi = len(sorted_collection) - 1

	while lo <= hi:
		# NOTE: remember, /2 -> floating pt. return, //2 -> integer return
		mid = lo + (hi - lo) // 2
		if key < sorted_collection[mid]:
			hi = mid - 1
		elif key > sorted_collection[mid]:
			lo = mid + 1
		else:
			return mid
	# key not found (for Python >3.10, return type can be None here to be
	# "more Pythonic", and return type alias woulc be "-> int | None:"
	return -1


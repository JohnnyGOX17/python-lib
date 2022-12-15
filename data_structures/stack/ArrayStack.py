#!/usr/bin/env python3


class ArrayStack:
    """
    Last-In First-Out (LIFO) Stack implementation which uses native python list
    as the underlying storage
    """

    def __init__(self):
        """Creates an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements currently in the stack"""
        return len(self._data)

    def is_empty(self):
        """Returns True if stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Adds element 'e' to the top of the stack"""
        self._data.append(e)  # NOTE: new item stored at the end of list

    def top(self):
        """
        Returns- but does not remove- the element currently at the top of the
        stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data[-1]  # give last item in list (top of the stack)

    def pop(self):
        """
        Remove and return the element from the top of the stack

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data.pop()  # give last item in list and remove it

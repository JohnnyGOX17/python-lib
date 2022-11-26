#!/usr/bin/env python3

class Vector:
    """Represent a multidimensional vector"""

    def __init__(self, d):
        """Create a vector of zeros in d dimensions"""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimensionality of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the j-th dimension coordinate of the vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set j-th dimension coordinate of vector to val"""
        self._coords[j] = val

    def __add__(self, other):
        """Return the sum of two Vectors"""
        if len(self) != len(other):  # relies on __len__ method above
            raise ValueError('Vector dimensions must agree!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result


    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector is not the same as other vector"""
        return not self == other # relies on existing __eq__definition

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry

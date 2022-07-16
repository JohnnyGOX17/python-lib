def mean(values: list) -> float:
    """
    Returns the mean (average) of a given input list values.
    Wiki: https://en.wikipedia.org/wiki/Mean

    >>> mean([3, 6, 9, 12, 15, 18, 21])
    12.0
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([2.5, 4.5])
    3.5
    """
    if not values:
        raise ValueError("Input list 'values' is empty")
    return sum(values) / len(values)


if __name__ == "__main__":
    import doctest

    # Runs tests present in function docstring
    print(doctest.testmod())

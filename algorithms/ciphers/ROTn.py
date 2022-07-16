def ROTn(s: str, n: int = 13) -> str:
    """
    Implements a generic "rotate by n places" substitution cipher.

    For instance when n = 13, the ROT13 cipher is used which replaces each
    character in the string 's' with the 13th letter after it in the alphabet.
    [ROT13 - Wikipedia](https://en.wikipedia.org/wiki/ROT13)

    >>> msg = "The cat in the hat has 14.5 fedoras!"
    >>> s = ROTn(msg, 13)
    >>> s
    'Gur png va gur ung unf 14.5 srqbenf!'
    >>> ROTn(s, 13) == msg
    True
    """
    # Similar solution to 'import this' in "The Zen of Python"
    # Also could be done with:
    #  import codecs
    #  print(codecs.encode(this.s, 'rot13'))
    # Naive solution for loops over the input string and does the same modulo
    #  character substitution
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + n) % 26 + c)
    return "".join([d.get(c, c) for c in s])


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    pt = input("Enter Plain Text message to ROTn: ")
    ct = ROTn(pt, 13)
    print(f"Cipher Text: {ct}")
    assert pt == ROTn(ct, 13)

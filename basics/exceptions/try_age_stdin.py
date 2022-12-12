#!/usr/bin/env python3

age = -1
while age <= 0:
    try:
        age = int(input('Enter your age (years): '))
        if age <= 0:
            print('Your age must be positive')
    except ValueError:
        print('Invalid age')
        # could also use `pass` statement to do nothing and continue while loop
    except EOFError:
        print('Unexpected error reading input')
        raise # re-raise exception to propagate exception upward

#!/usr/bin/env python3
#
# Shows recursion to print out a standard english ruler
#
# For  each inch, we place a tick with a numeric label. We denote the length of
# the tick  designating a whole inch as the major tick length. Between the
# marks for whole  inches, the ruler contains a series of minor ticks, placed
# at intervals of 1/2 inch,  1/4 inch, and so on. As the size of the interval
# decreases by half, the tick length  decreases by one.
#


def draw_minor_tick(tick_length):
    if tick_length > 1:
        # We're not the smallest tick length so bracket the minor tick_length w/2x
        # smaller ticks/recursive-series
        draw_minor_tick(tick_length - 1)
        print("-" * tick_length)
        draw_minor_tick(tick_length - 1)
    else:
        # We hit the smallest minor tick, print and return back up to last call
        print("-")


def draw_ruler(num_inches, major_tick_length):
    for i in range(num_inches):
        print(("-" * major_tick_length) + f" {i}")
        draw_minor_tick(major_tick_length - 1)
    # Last line to show ending line number
    print(("-" * major_tick_length) + f" {num_inches}\n")


if __name__ == "__main__":
    print("2-inch ruler w/major tick length = 4")
    draw_ruler(2, 4)

    print("1-inch ruler w/major tick length = 5")
    draw_ruler(1, 5)

    print("3-inch ruler w/major tick length = 3")
    draw_ruler(3, 3)

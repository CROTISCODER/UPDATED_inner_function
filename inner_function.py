"""
program: inner_functions_assignment.py
author: Angel Castro
date: 3/3/2021
description:
    Measurement function with inner functions to calculate area and perimeter. Returns an array value, which is then
    printed as results in main().
"""


def measurements(length_width_list):
    length = float(length_width_list[0])
    width = float(length_width_list[1])

    def area(length, width):
        return length * width

    def perimeter(length, width):
        return (length * width) * 2

    return area(length, width), perimeter(length, width)


if __name__ == '__main__':
    rectangle = [2, 5]
    results = measurements(rectangle)
    print('Perimeter = ' + str(results[0]) + ' Area = ' + str(results[1]))

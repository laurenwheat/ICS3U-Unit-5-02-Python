#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better

import math


def triangle_area(base, height):

    area = (base * height) / 2

    return area


def main():

    while True:
        try:
            base_input = input("Enter the base length (cm): ")
            base_int = int(base_input)
            height_input = input("Enter the height (cm): ")
            height_int = int(height_input)
            print("")

            if base_int > 0 and height_int > 0:
                triangle = triangle_area(base_int, height_int)

                print("The area of the triangle is {0} cm²!!".format(triangle))

                break
            else:
                print("Input must be a positive number!!!")
        except Exception:
            print("That is not even a number!!")
        finally:
            print("Wanna try again :)?")


if __name__ == "__main__":
    main()

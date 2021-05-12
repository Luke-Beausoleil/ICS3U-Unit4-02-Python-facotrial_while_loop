#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program uses a while loop to find factorial


def main():
    # this function finds the factorial

    # variables
    loop_counter = 1
    factorial = 1

    # input
    number_as_string = input("Enter a positive integer or zero: ")

    # process & output
    try:
        number = float(number_as_string)
        if number == 0:
            print("\n0 factorial is 1.")
        else:
            try:
                integer = int(number_as_string)
                if integer > 0:
                    while loop_counter < integer:
                        loop_counter = loop_counter + 1
                        factorial = factorial * loop_counter
                    print("\n{0} factorial is {1}".format(integer, factorial))
                else:
                    print("\nInvalid. Enter a positive integer or zero.")
            except (Exception):
                print("\nInvalid. Enter a positive integer or zero.")
    except (Exception):
        print("\nInvalid. Enter a positive integer or zero.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()

# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/13/20
# This program calculates the area and perimeter of a rectangle
# The user enters in the dimensions


def main():
    # this function calculates the answer

    # input
    varX = int(
        input("Enter the first number you would like to add (integer): ")
    )
    varY = int(
        input("Enter the second number you would like to add (integer): ")
    )

    # process
    answer = varX + varY

    # output
    print("")
    print("{0} + {1} = {2}".format(varX, varY, answer))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
#
# title: CracklePop - a FizzBuzz clone
# date:  2023-10-04 18:00 EDT
# author: Jon Boone ipmonger@delamancha.org
#

# we will print a range of numbers (1 - 100, inclusive) using a set of four substitution rules.
# 1. If the number is divisible by 3 and 5, substitute "CracklePop"
# 2. If it is divisibule by 3 and not 5, substitute the work "Crackle"
# 3. If it is not divisible by 3 but is by 5, substitute the work "Pop"
# 4. Otherwise, print the number.

MAXRANGE = 100
targetRange= range(1,MAXRANGE+1)
threes = { x for x in targetRange if x % 3 == 0}
fives = { x for x in targetRange if x % 5 == 0}
both = threes.intersection(fives)


def substitution(value):
    if value in both:
        return "CracklePop"
    elif value in threes:
        return "Crackle"
    elif value in fives:
        return "Pop"
    else:
        return value


def main():
    for value in targetRange:
        if value < MAXRANGE:
            print(f"{substitution(value)}, ",end="")
        else:
            print(f"{substitution(value)}\n",end="")


if __name__ == "__main__":
    main();

"""
given a number, reverse it's digit and add to the original number. now check whether the number is formed by performing
the above mentioned operations is a palindromic or not. If not then repeat the above process again. return the number
og steps required to reach a palindromic number
"""


def is_palindromic(number):
    reversed_ = number[::-1]
    print(reversed_)
    print(number)
    if number == reversed_:
        return True
    return False


def main(number, steps=0):
    str_number = str(number)
    if is_palindromic(str_number):
        return steps
    number += int(str_number[::-1])
    steps += 1
    return main(number, steps)


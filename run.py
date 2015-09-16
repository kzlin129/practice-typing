#!/usr/bin/env python
from __future__ import print_function
from Getch import _Getch
from time import sleep
from profilehooks import profile
import random
import os

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER = "1234567890"
SYMBOL = "~!@#$%^&*()_+{}|:\"<>?-=[]\;',./`"


def clear():
    os.system('clear') #Currently, only linux

def getch():
    _getch = _Getch()
    return _getch()

def test(string):
    clear()
    print(string)
    cha = getch()
    header = 0
    string_len = len(string)
    while True:
        if header == string_len - 1 and cha == string[-1]: #Pass
            break
        elif cha == string[header]:
            print(cha, end="")
            header += 1
        else:
            clear()
            print(string)
            header = 0
        cha = getch()

def test_by_sequence():
    test(ALPHABET)
    test(ALPHABET.upper())
    test(ALPHABET[::-1])
    test(ALPHABET[::-1].upper())
    test(NUMBER)
    test(NUMBER[::-1])
    test(SYMBOL)
    test(SYMBOL[::-1])

def test_by_random():
    alpha = ALPHABET+ALPHABET.upper()
    num = NUMBER+SYMBOL
    test(''.join(random.sample(alpha, 26)))
    test(''.join(random.sample(num, 26)))
    test(''.join(random.sample(alpha + num, 26)))

@profile
def main():
    test_by_sequence()
    test_by_random()
    clear()
    print("Pass")
    sleep(1)


if __name__ == "__main__":
    try:
        main()
	print_prof_data()
	clear_prof_data()
    except KeyboardInterrupt:
        print("Forced to exit by Ctrl-C")
        sleep(1)
        exit(0)

#!/usr/bin/env python
from __future__ import print_function
from time import sleep
from profile import * 
import random
import os
if os.name == "nt":
    import msvcrt
else:
    from Getch import _Getch

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER = "0123456789"
SYMBOL = "~!@#$%^&*()_+{}|:\"<>?-=[]\;',./`"


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def getch():
    if os.name == "nt":
        return msvcrt.getche()
    else:
        _getch = _Getch()
        return _getch()

def test(string):
    clear()
    print(string)
    cha = getch()
    if os.name == "nt":
        cha = cha.decode("utf-8")
    header = 0
    string_len = len(string)
    while True:
        if cha == '\x03': #Ctrl-C
            print("Ctrl-C: Forced exit")
            exit()
        elif header == string_len - 1 and cha == string[-1]: #Pass
            break
        elif cha == string[header]:
            if os.name != "nt":
                print(cha, end="")
            header += 1
        else:
            clear()
            print(string)
            header = 0
        cha = getch()
        if os.name == "nt":
            cha  = cha.decode("utf-8")

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
        sleep(3)
        clear_prof_data()
    except KeyboardInterrupt:
        print("Forced to exit by Ctrl-C")
        sleep(1)
        exit(0)

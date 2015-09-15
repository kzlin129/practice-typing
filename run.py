#!/usr/bin/env python
from time import sleep
import curses
import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER = "1234567890"
SYMBOL = "~!@#$%^&*()_+{}|:\"<>?-=[]\;',./`"

STDSCR = curses.initscr()

def clear():
    STDSCR.clear()

def println(string):
    STDSCR.addstr(0, 0, string+'\n')
    STDSCR.refresh()

def getch():
    return STDSCR.getch()

def test(string):
    clear()
    println(string)
    cha = getch()
    header = 0
    string_len = len(string)
    while True:
        if header == string_len - 1 and cha == ord(string[-1]): #Pass
            break
        elif cha == ord(string[header]):
            STDSCR.addch(1, header, cha)
            STDSCR.refresh()
            header += 1
        else:
            clear()
            println(string)
            header = 0
        cha = getch()

def init_screen():
    curses.cbreak()
    STDSCR.keypad(1)

def deinit_screen():
    curses.nocbreak()
    STDSCR.keypad(0)
    curses.echo()
    curses.endwin()

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


def main():
    init_screen()
    test_by_sequence()
    test_by_random()
    clear()
    println("Pass")
    sleep(1)
    deinit_screen()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        println("Forced to exit by Ctrl-C")
        sleep(1)
        deinit_screen()
        exit(0)

#!/usr/bin/env python
from time import sleep
from sys import exit
import os
import curses
import pdb
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "~!@#$%^&*()_+{}|:\"<>?-=[]\;',./`"

stdscr = curses.initscr()

def clear():
  stdscr.clear()

def println(string):
  stdscr.addstr(0,0,string+'\n');
  stdscr.refresh()

def getch():
  return stdscr.getch()

def test(string):
  clear()
  println(string)
  ch = getch()
  h = 0
  string_len = len(string)
  while True:
    if h == string_len - 1 and ch == ord(string[-1]): #Pass
      break
    elif ch == ord(string[h]):
      stdscr.addch(1,h,ch)
      stdscr.refresh()
      h += 1
    else:
      clear()
      println(string)
      h = 0 
    ch = getch()

def init_screen():
  curses.cbreak()
  stdscr.keypad(1)
    
def deinit_screen():
  curses.nocbreak()
  stdscr.keypad(0)
  curses.echo()
  curses.endwin()

def test_by_sequence():
  test(alphabet)
  test(alphabet.upper())
  test(alphabet[::-1])
  test(alphabet[::-1].upper())
  test(number)
  test(number[::-1])
  test(symbol)
  test(symbol[::-1])

def test_by_random():
  a = alphabet+alphabet.upper()
  n = number+symbol
  test(''.join(random.sample(a,26)))
  test(''.join(random.sample(n,26)))
  test(''.join(random.sample(a+n, 26)))


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

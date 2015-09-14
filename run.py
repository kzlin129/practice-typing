#!/usr/bin/env python
from __future__ import print_function
from Getch import _Getch
from time import sleep
from sys import exit
import os


alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "~!@#$%^&*()_+{}|:\"<>?-=[]\;',./`"

def clear():
  os.system('clear') #Currently, only linux

def getch():
  _getch = _Getch()
  return _getch()

def test(string):
  clear()
  print(string)
  ch = getch()
  h = 0
  string_len = len(string)

  while True:
    if ch == '\x03': # Ctrl+C
      print("Ctrl-C: Forced exit")
      exit()
    if h == string_len - 1 and ch == string[-1]: #Pass
      break
    elif ch == string[h]:
      print(ch,end="")
      h += 1
    else:
      clear()
      print(string)
      h = 0 
    ch = getch()

if __name__ == "__main__":
  test(alphabet)
  test(alphabet.upper())
  test(alphabet[::-1])
  test(alphabet[::-1].upper())
  test(number)
  test(number[::-1])
  test(symbol)
  test(symbol[::-1])
  clear()
  print("\nPass")
  sleep(1)

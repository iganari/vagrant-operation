#!/usr/bin/env python
# coding: utf-8

import sys

def yes_no_input():
    while True:
        choice = raw_input("Plz respond with 'yes' or 'no' [y/N]:").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


if __name__ == '__main__':
    if yes_no_input():
      print('OK!')

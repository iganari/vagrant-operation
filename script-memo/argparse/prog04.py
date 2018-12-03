#!/usr/bin/env python
# coding='utf-8'

import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("square", 
#                     help="display a squre of a given number", 
#                     type=int)
parser.add_argument("square", 
                    help="display a squre of a given number", 
                    type=int)
args = parser.parse_args()
print(args.square**2)
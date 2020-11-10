#!/usr/bin/env python

import sys


def args(args):
  if(len(args) != 3):
    sys.exit("\nUsage: ./monosat.py [# of monopoles] [# of rooms]\n")
  return int(args[1]), int(args[2])

def main():
  args(sys.argv)
  
if __name__ = '__main__':
  main()

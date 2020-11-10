#!/usr/bin/env python3

import sys


# Parses and checks sys.argv arguments to check for correct number and valid
# inputs
# Returns two integers:
#   1) # of monopoles
#   2) # of rooms
def checkSysArgs():

  # Check for correct number of args
  if(len(sys.argv) != 3):
    sys.exit("\nERROR: Incorrect number of arguments\n\nUsage: ./monosat.py <# "
             "of monopoles> <# of rooms>\n")

  # Check that args are valid for monopoles problem
  if(sys.argv[1] <= sys.argv[2]):
    sys.exit("\nERROR: <# of monopoles> must be greater than <# of rooms>\n\nUs"
             "age: ./monosat.py <# of monopoles> <# of rooms>\n")

  return int(sys.argv[1]), int(sys.argv[2])


# Create a CNF of monopole problem
def buildCNF(monos, rooms):
  cnf = []

  # Each monopole is placed
  # No monopole is in two places
  # Sums exclude monopoles s.t. X + Y = Z



def main():

  # Parse args and return integers if input is correct
  monos, rooms = checkSysArgs()

  cnf_vars = monos * rooms

  
if __name__ == '__main__':
  main()

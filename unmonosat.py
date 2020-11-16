#!/usr/bin/env python3

import sys
from monosat import checkSysArgs, additiveProperty


def checkSoln(monos, rooms, solution):

  # 1) Each monopole is placed
  fullList = []
  for room in solution:
    fullList += solution[room]
  if(set(fullList) != set(range(1, monos+1))):
    print("Arguments don't match solution: each monopole is not placed\n")
    return False

  # 2) No monopole is in two places
  fullList = set([])
  for room in solution:
    fullList = fullList.intersection(set(solution[room]))
  if(len(fullList) != 0):
    print(f"Arguments don't match solution: {fullList} in more than one room\n")
    return False

  # 3) Sums exclude monopoles s.t. X + Y = Z
  for room in solution:
    for i, x in enumerate(solution[room][:-2]):
      for y in solution[room][i+1:-1]:
        for z in solution[room][i+2:]:
          if(additiveProperty(x,y,z)):
            return False
  return True
  
  
  


def main():

  rawInput = []
  atoms = []

  # Parse args and return integers if input is correct
  monos, rooms = checkSysArgs()

  # Initialize
  solution = {x: [] for x in range(1,rooms+1)}

  # Read input file
  for line in  sys.stdin:
    rawInput.append(line.rstrip('\n'))

  # Check for SAT or UNSAT
  print(rawInput[0])
  if(rawInput[0] == 'UNSAT'):
    return 0;

  # Decode minisat output
  atoms = rawInput[1].rstrip('\n').split(' ');
 
  for x in atoms:
    if(x == '0'):   # ignore trailing 0
      break
    if(x[0] == '-'):  # ignore negated variable
      continue

    # Reverse the atomic variable encoding
    # See: monosat.py, L(monos, rooms, monopole)
    room = ((int(x)-1) // monos) + 1
    monopole = ((int(x) - 1) % monos) + 1

    # Add to solution dictionary
    solution[room].append(monopole)

  # Check that solution works for args provided
  if(checkSoln(monos, rooms, solution)):

    # Print Solution
    for room in solution.keys():
      print("Room " + str(room) + ": ", end='')
      print(*solution[room], sep=', ')



if __name__ == '__main__':
  main()

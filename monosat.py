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
    sys.exit(f"\nERROR: Incorrect number of arguments\n\nUsage: {sys.argv[0]} <num "
             "of monopoles> <num of rooms>\n")
    
  # Check that args are valid for monopoles problem
  if(int(sys.argv[1]) <= int(sys.argv[2])):
    sys.exit(f"\nERROR: num of monopoles must be greater than num of rooms\n\nUs"
             "age: {sys.argv[0]} <num of monopoles> <num of rooms>\n")

  return int(sys.argv[1]), int(sys.argv[2])



# Check if X + Y = Z for integers x, y, z
# Returns true if property exists
# Returns false if it does not
def additiveProperty(x, y, z):
  if(x + y == z):
    return True
  else:
    return False


# Create atom variable
def L(monos, room, monopole):
  return (monos * room) + monopole


# Create a CNF of monopole problem
def buildCNF(monos, rooms):
  cnf = []

  # 1) Each monopole is placed
  for m in range(1, monos+1):
    clause = ''
    for r in range(rooms):
      # Creates atom variable
      clause += str(L(monos, r, m)) + ' '
    clause += '0'
    cnf.append(clause)

  # 2) No monopole is in two places
  for m in range(1, monos+1):
    clause = ''
    for r in range(rooms):
      # Creates negated atom variable
      clause += '-' + str(L(monos, r, m)) + ' '
    clause += '0'
    cnf.append(clause)

  # 3) Sums exclude monopoles s.t. X + Y = Z
  for r in range(rooms):
    for x in range(1, monos-1):
      for y in range(x + 1, monos):
        for z in range(y + 1, monos+1):
          if(additiveProperty(x,y,z)):
            cnf.append('-' + str(L(monos, r, x)) + ' -' + 
                             str(L(monos, r, y)) + ' -' + 
                             str(L(monos, r, z)) + ' 0')
  return cnf



def main():

  dimacs = []

  # Parse args and return integers if input is correct
  monos, rooms = checkSysArgs()

  # Create DIMACS form from CNF SAT formula
  dimacs = buildCNF(monos, rooms)

  # Add problem clause for minisat program
  probStatement = "p cnf " + str(monos * rooms) + " " + str(len(dimacs))

  # Output the DIMACS format to standard output
  print(probStatement)
  for line in dimacs:
    print(line)

  
if __name__ == '__main__':
  main()


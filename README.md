# SAT_Monopoles
    John Lewis
    Portland State University
    CS441
    HW 2

Solving monopoles problem using CNF DIMACS encoding for `minisat`

## To Run:
1. **./monosat [num of monopoles] [num of rooms] >[monosat output file]**
2. **minisat [monosat output file] [minisat output file]**
3. **./unmonosat [num of monopoles] [num of rooms] <[minisat output]**

## Monopoles: Problem Statement
Given: n rooms, set 1..m of monopoles to place.

Find: a list S of n sets with the following properties:

1. Each monopole is placed:
```
  forall i in {1..m} .
      exists j in {1..n} .
          i in S[j]
```
2. No monopole is in two places:
```
  forall i in {1..m}
      exists unique j in {1..n} .
          i in S[j]
```
3. Sums exclude monopoles:
```
forall i in {1..n} .
   for all j, k in S[i] .
       j ≠ k and j in S[i] and k in S[i] → j + k not in S[i]
```

## Description
This set of programs seeks to solve the monopoles problem described above by converting the
problem into **Conjunctive Normal Form (CNF)** and encoding that into **DIMACS** format for
the `minsat` program to check for satisfiability.

The `monosat` program encoder takes the number of monopoles and number of rooms as arguments
and creates **DIMACS** clauses to reflect the three properties of the monopoles problem stated
above. To make these clauses, the combination of room and monopole are turned into an atomic
variable with the equation `(total_monopoles * room) + monopole` meant to reflect the location
**L[m][n]**. For a problem with eight
monopoles and two rooms this results in 16 variables (`total_rooms * total_monopoles`). As an
example, monopole **1** of **8** monopoles placed in **room 0** would be `(8 * 0) + 1 = 1` and
the same monopole placed in **room 1** would be `(8 * 1) + 1 = 9`
 
For `1. Each monopole is placed` the **DIMACS** clauses are just an enumeration of the possible
combinations of monopoles and rooms i.e `1 is in room 0`, `1 is in room 1`, `2 is in room 0`,
`2 is in room 1`...

For `2. No monopole is in two places` the **DIMACS** clauses are an enumeration of the negation
of the possible combinations of monopoles and rooms. Since the first clauses covered the poosible
locations, these clauses simply state that they can't also be somewhere else. `1 is in room 1`
**AND** `~(1 is in room 1)` can't be true.

Finally, for `3. Sums exclude monopoles` the **DIMACS** clauses reflect that for any three
elements such that `X + Y = Z`, you can't have **X AND Y AND Z** at that location. This gives
clauses that say `~(X in room #) ~(Y in room #) ~(Z in room #)`.

Once the `monosat` program has encoded the **CNF** into **DIMACS**, it can be passed into the
`minsat` program to check if it is satisfiable given the provided clauses. The output is
saved to an output file to be passed into the `unmonosat` program.

The `unmonosat` program takes the result `SAT` or `UNSAT` and the **DIMACS** encoded **CNF**
that satisfies the problem from the `minisat` output and decodes it back into rooms and
monopoles. This is done by reverse engineering the location encodeing we used earlier and
ignoring the negated atomic variables. **16** for input **8** **2** would decode to
**Room 2** =>`((16 - 1) // 8) + 1` and **Monopole 8** =>`((16 - 1) % 8) + 1)`.

There is additional testing in the `unmonosat` program to make sure that even if the `minisat`
program returns `SAT` that the user provided arguments match the arguments provided to the
`monosat` program that encoded the **DIMACS** input. This is done by decoding and checking
that the solution meets properties 1-3 of the problem statement.

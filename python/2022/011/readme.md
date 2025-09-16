Monkey in the Middle
====================

https://adventofcode.com/2022/day/11

A brute force solution for part one but part two becomes impossible to run by brute force unless we divide by much
more than 3.

Because the rules of the problem are set, we can do a modulus by the product of all our divisibility tests to ensure
that we will never have large enough numbers to either overflow or make our program run too slow (as it does in 
Python). For the example input that number is

```
23*19*13*17 = 96577
```

The value for the real input will vary according to your input but this is being calculated by the program when the
input is being parsed.
Lobby
=====

https://adventofcode.com/2025/day/3

Here is the algorithm implemented for creating the joltage codes:

    1 - while the length of generated code (L) is smaller than desired size (S)
    2 - find the maximum value on the array (A) and its index (I)
    3 - if this added to already generated code is S, break
    4 - is I + (S-1) <= length of array?
        4.1 - if yes, add it to the generated code
        4.2 - if no, find a new maximum value and index I and go back to 2 excluding this value/index combination 
    5 - remove everything up to I from A

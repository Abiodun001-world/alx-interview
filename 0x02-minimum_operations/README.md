# 0x02. Minimum Operations

## Introduction
This project is focused on solving the "Minimum Operations" problem using Python. The goal is to implement an algorithm that calculates the minimum number of operations needed to obtain a specific number of characters by copying and pasting.

## Problem Description
Given a string containing only the letter 'H', we want to obtain a target string of a certain length by performing the minimum number of operations. The only two operations allowed are:
- Copy All: This operation copies the entire existing string.
- Paste: This operation pastes the copied string to the end of the existing string.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Code documentation is required.
- Code should follow the PEP 8 style guidelines (version 1.7.x).
- All files must be executable.

## File Structure
The project should have the following files:

1. `0-main.py`: This is the main file that contains the algorithm to solve the problem.
2. `README.md`: This file contains the project description, instructions, and any other relevant information.

## Execution
To execute the algorithm, run the following command:
```
$ ./0-main.py
```

## Example
Let's consider an example where the target string is "HHHHH". The minimum number of operations required to obtain this target string is 5: Copy All, Paste, Paste, Paste, Paste.

## Author
Carrie Ybay, Software Engineer at Holberton School

# 0x08. Making Change

## Description
This project is part of the Holberton School curriculum and focuses on developing an algorithm in Python to solve the "Making Change" problem. The goal is to design a function that calculates the minimum number of coins needed to make change for a given amount using a set of coin denominations.

## Author
Carrie Ybay
* Software Engineer at Holberton School

## Project Timeline
- Start: August 21, 2023, 6:00 AM
- End: August 25, 2023, 6:00 AM
- Checker Release: August 22, 2023, 6:00 AM
- Auto Review Deadline: August 25, 2023, 6:00 AM

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- PEP 8 style (version 1.7.x) should be followed
- All files must be executable

## Files
The project consists of the following files:

| File Name          | Description                      |
|--------------------|----------------------------------|
| `0-making_change.py` | Python script with the algorithm to solve the problem |
| `README.md`        | This file (project documentation) |

## Problem Statement
You are given an amount of money `n` and a list of coin denominations. Your task is to implement a function `makeChange(coins, total)` that calculates the minimum number of coins required to make change for the given amount using the provided coin denominations. Your function should return the minimum number of coins needed or `-1` if it's not possible to make the change.

### Example
```python
>>> makeChange([1, 2, 5], 11)
3  # 11 = 5 + 5 + 1
>>> makeChange([2], 3)
-1  # It's not possible to make change for 3 cents using only 2-cent coins


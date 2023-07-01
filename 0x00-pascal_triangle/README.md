# 0x00. Pascal's Triangle

This project is part of the Holberton School curriculum and focuses on implementing Pascal's Triangle algorithm in Python. The goal is to generate Pascal's Triangle up to a given number of rows and understand its construction.

## Concepts

The main concept to focus on for this project is **Technical Interview**. You will have an opportunity to practice technical interview skills by implementing Pascal's Triangle algorithm in Python.

## About the Author

This project was created by Alexa Orrico, a Software Engineer at Holberton School. 

## Pascal's Triangle

Pascal's Triangle is a triangular array of numbers named after the French mathematician Blaise Pascal. It starts with a row containing a single value of 1, and each subsequent row is constructed by adding the adjacent values from the previous row. The resulting triangle has various applications in mathematics and computer science, including combinatorics, probability theory, and number theory.

The triangle is constructed in the following way:

- The first row consists of the number 1.
- Each subsequent row starts and ends with the number 1.
- Each value in the triangle (except for the first and last value in each row) is the sum of the two values directly above it in the previous row.

Here's an example of Pascal's Triangle with 5 rows:

```
             1
          1     1
       1     2     1
    1     3     3     1
 1     4     6     4     1
```

## Getting Started

To get started with this project, follow the steps below:

1. Clone the project repository from the provided URL.
2. Familiarize yourself with the project structure and files.
3. Implement the `pascal_triangle` function in Python according to the given requirements.
4. Test your implementation thoroughly to ensure correctness.
5. Submit your solution before the deadline for the automated review.

## Requirements

Your implementation of Pascal's Triangle should meet the following requirements:

- The function should be named `pascal_triangle`.
- It should take an integer `n` as input.
- The function should return a list of lists representing Pascal's Triangle up to the `n`th row.
- Each inner list should contain the values of a row in the triangle.
- The triangle should be constructed using the Pascal's Triangle algorithm.

## Example

Here's an example usage of the `pascal_triangle` function:

```python
>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

This example generates the first five rows of Pascal's Triangle.

## Testing

It is important to test your implementation to ensure it works correctly. You can create additional test cases to verify the accuracy of your solution.

## Good luck!

I Take this opportunity to practice my technical interview skills and deepen my understanding of Pascal's Triangle. Feel free to reach out for help if you encounter any issues during the project. Good luck, and enjoy the learning process!

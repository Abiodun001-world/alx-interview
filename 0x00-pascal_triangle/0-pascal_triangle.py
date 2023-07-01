def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the result list with the first row [1]
    result = [[1]]

    for i in range(1, n):
        # Initialize the current row with [1]
        current_row = [1]

        # Calculate the values for the current row
        for j in range(1, i):
            current_row.append(result[i-1][j-1] + result[i-1][j])

        # Add the last value 1 to the current row
        current_row.append(1)

        # Append the current row to the result list
        result.append(current_row)

    return result

def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to the perimeter
                
                # Check adjacent cells (up, down, left, right) and subtract 1 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1
    
    return perimeter

# Test the function
#grid = [
 #   [0, 0, 0, 0, 0, 0],
 #   [0, 1, 0, 0, 0, 0],
  #  [0, 1, 0, 0, 0, 0],
   # [0, 1, 1, 1, 0, 0],
    #[0, 0, 0, 0, 0, 0]
]
# print(island_perimeter(grid))  # Output should be 12


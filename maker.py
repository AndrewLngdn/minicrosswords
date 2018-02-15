
def print_grid(grid):
  for row in grid:
    for val in row:
      print '{:4}'.format(val),
    print

length = 4
grid = [ [None for x in range(length)] for x in range(length)]

grid[2] = ["S", "P", "U", "D"]

print_grid(grid);



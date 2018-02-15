import csv;

def print_grid(grid):
  for row in grid:
    for val in row:
      print '{:4}'.format(val),
    print

length = 4
grid = [ [None for x in range(length)] for x in range(length)]

grid[2] = ["S", "P", "U", "D"]

print_grid(grid);


with open("clues.csv") as clues_csv:
  csv_reader = csv.reader(clues_csv)
  for row in csv_reader:
    print(row)
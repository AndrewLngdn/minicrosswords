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

word_clue_pairs = {}

with open("clues.csv") as clues_csv:
  csv_reader = csv.reader(clues_csv)
  for row in csv_reader:
    word, clue  = row[-1], row[-2]
    if word not in word_clue_pairs:
      word_clue_pairs[word] = [clue]
    else:
      word_clue_pairs[word].append(clue)

for word, clues in word_clue_pairs.iteritems():
  if len(clues) > 1:
    print "word: " + word
    print "clue: " + str(clues)
    print


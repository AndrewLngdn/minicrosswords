import csv
from trie import Trie

class CrosswordMaker:
  def __init__(self, grid_size):
    self.grid = [ [None for x in range(grid_size)] for x in range(grid_size)]

  def print_grid(self):
    for row in self.grid:
      for val in row:
        print '{:4}'.format(val),
      print

if __name__ == "__main__":

  crossword = CrosswordMaker(4)
  crossword.grid[2] = ["S", "P", "U", "D"]
  crossword.print_grid();

  word_clue_pairs = {}

  with open("clues.csv") as clues_csv:
    csv_reader = csv.reader(clues_csv)
    for row in csv_reader:
      word, clue  = row[-1], row[-2]
      if word not in word_clue_pairs:
        word_clue_pairs[word] = [clue]
      else:
        word_clue_pairs[word].append(clue)

  # for word, clues in word_clue_pairs.iteritems():
  #   if len(clues) > 1:
  #     print "word: " + word
  #     print "clue: " + str(clues)
  #     print

words = word_clue_pairs.keys()

trie = Trie(words)


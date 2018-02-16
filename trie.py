class Trie:
  root = None
  def __init__(self, word_list):
    self.root = TrieNode()
    for word in word_list:
      self.root.add_word(word);


class TrieNode:
  def __init__(self, character=""):
    print character
    self.character = character;
    self.children = {}

  def add_word(self, word):
    if word is '':
      print "word added"
      return;

    first_char, rest = word[:1], word[1:]
    # print "first char " + first_char
    # print "rest       " + str(rest)

    if first_char not in self.children:
      self.children[first_char] = TrieNode(first_char)

    self.children[first_char].add_word(rest)


if __name__ == "__main__":
  trie = Trie(["hi", "hello", "howareyou", "helloworld"])
  # import pdb; pdb.set_trace()


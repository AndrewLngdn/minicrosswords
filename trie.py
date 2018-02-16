class Trie:
  root = None
  def __init__(self, word_list):
    self.root = TrieNode()

class TrieNode:
  def __init__(self, character=""):
    print character


if __name__ == "__main__":
  trie = Trie()

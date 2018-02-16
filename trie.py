class Trie:
  root = None
  def __init__(self, word_list):
    self.root = TrieNode()
    for word in word_list:
      self.root.add_word(word, original_word=word);

  def words_with_prefix(self, prefix, length=None):
    prefix_node = self.root
    for char in prefix: 
      prefix_node = prefix_node.children[char]
    return prefix_node.words_from_node()

class TrieNode:
  def __init__(self, character="", parent=None):
    self.character = character;
    self.children = {}
    self.parent = parent
    self.is_word = False
    self.words_under_node = set([])

  def add_word(self, word, original_word):
    self.words_under_node.add(original_word)
    if word is '':
      self.is_word = True;
      return;

    first_char, rest = word[:1], word[1:]

    if first_char not in self.children:
      self.children[first_char] = TrieNode(first_char, self)

    self.children[first_char].add_word(rest, original_word=original_word)

  def prefix(self, suffix=""):
    if self.character is '':
      return suffix
    else:
      last_char = self.character
      return self.parent.prefix(last_char + suffix)

  def words_from_node(self):
    words = []
    nodes = [self]

    while nodes:
      node = nodes.pop()
      if not any(node.children) or node.is_word:
        words.append(node.prefix())
      nodes = nodes + node.children.values()

    return words


# h -> i -> 
#   -> e -> l


if __name__ == "__main__":
  words = ["hi", "hello", "howareyou", "helloworld"]
  trie = Trie(words)
  assert trie.root.children['h'].children['e'].children['l'].prefix() == "hel"

  assert set(trie.root.words_from_node()) == set(words)
  assert set(trie.root.children['h'].children['e'].words_from_node()) == set(["hello", "helloworld"])
  assert set(trie.words_with_prefix("hel")) == set(["hello", "helloworld"])
  assert set(trie.root.children['h'].words_under_node) == set(words)

  import pdb; pdb.set_trace();





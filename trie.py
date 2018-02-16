class Trie:
  root = None
  def __init__(self, word_list):
    self.root = TrieNode()
    for word in word_list:
      self.root.add_word(word);

  def words_with_prefix(self, prefix, length=None):
    prefix_node = self.root
    for chars in prefix: 
      prefix_node = node.children[char]



class TrieNode:
  def __init__(self, character="", parent=None):
    print character
    self.character = character;
    self.children = {}
    self.parent = parent
    # self.is_word = True

  def add_word(self, word):
    if word is '':
      print "word added"
      return;

    first_char, rest = word[:1], word[1:]

    if first_char not in self.children:
      self.children[first_char] = TrieNode(first_char, self)

    self.children[first_char].add_word(rest)

  def prefix(self, suffix=""):
    if self.character is '':
      return suffix
    else:
      last_char = self.character
      return self.parent.prefix(last_char + suffix)

  def words_from_node(self, word=""):
    if len(self.children) is 0:
      print word + self.character
      return word
    
    word = word + self.character
    for char, node in self.children.iteritems():
      node.words_from_node(word)



if __name__ == "__main__":
  trie = Trie(["hi", "hello", "howareyou", "helloworld"])
  assert trie.root.children['h'].children['e'].children['l'].prefix() == "hel"
  # print trie.root.words_from_node()
  import pdb; pdb.set_trace();





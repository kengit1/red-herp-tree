class Dictionary:
    def __init__(self):
        self.tree = RedBlackTree()

    def load_dictionary(self, filename):
        with open(filename, "r") as file:
            for line in file:
                word = line.strip()
                self.tree.insert(word)

    def insert_word(self, word):
        self.tree.insert(word)

    def lookup_word(self, word):
        result = self.tree.search(word)
        if result != self.tree.NIL:
            print("YES")
        else:
            print("NO")
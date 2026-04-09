from tree import RBTree

class Dictionary:
    def __init__(self):
        
        self.tree = RBTree()

    def load_dictionary(self, filename):
        with open(filename, "r") as file:
            for line in file:
                word = line.strip()
                self.tree.insert(word)

    def insert_word(self, word):
        self.tree.insert(word)

    def lookup_word(self, word):
        # Done merging the utility
        result = self.tree.SearchTree(self.tree.root, word)
        
        # NIL == None
        if result is not None:
            print("YES")
        else:
            print("NO")
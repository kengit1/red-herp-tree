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
        if not word.isalpha():
            print("Invalid input! Enter letters only.")
            return
        word = word.upper()
        result = self.tree.SearchTree(self.tree.root, word)

        if result is not None:
            print("Word already exists!")
            return

        self.tree.insert(word)

        with open("dictionary.txt", "a") as file:
            file.write(word + "\n")

    def lookup_word(self, word):
        # Done merging the utility
        word = word.upper()
        result = self.tree.SearchTree(self.tree.root, word)
        
        # NIL == None
        if result is not None:
            print("YES")
        else:
            print("NO")
from dict import Dictionary
from height import height, blackHeight
from size import size


def main():
    dictionary = Dictionary()

    dictionary.load_dictionary("dictionary.txt")

    x = "100"
    while x != "0":
        print("\n1. Search")
        print("2. Insert")
        print("3. Print Tree Height")
        print("4. Print Black Height")
        print("5. Print Tree Size")
        print("0. Exit")

        x = input("Enter your choice: ").strip()

        match x:
            case "1":
                word = input("Enter your search word: ").strip()
                print("Searching for", word)
                dictionary.lookup_word(word)

            case "2":
                word = input("Enter your word: ").strip()
                print("Inserting:", word)
                dictionary.insert_word(word)

                s = size(dictionary.tree.root)
                h = height(dictionary.tree.root)
                bh = blackHeight(dictionary.tree.root)

                print("Tree Size =", s)
                print("Tree Height =", h)
                print("Black Height =", bh)

            case "3":
                h = height(dictionary.tree.root)
                print("Tree Height =", h)

            case "4":
                bh = blackHeight(dictionary.tree.root)
                print("Black Height =", bh)

            case "5":
                s = size(dictionary.tree.root)
                print("Tree Size =", s)

            case "0":
                print("Exit")

            case _:
                print("Invalid Input")


if __name__ == "__main__":
    main()
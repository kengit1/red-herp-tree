x="100"
while x!="0":
    print("1. Search")
    print("2. Insert")
    print("3. Print Tree Height")
    print("4. Print Black Height")
    print("5. Print Tree Size")
    print("0. Exit")
    x = input("Enter your choice: ").strip()

    match x:
        case "1":
            word=input("Enter your search word: ").strip()
            print("Searching for",word)
        case "2":
            word=input("Enter your word: ").strip()
            print("Inserting:", word)
        case "3":
            print("Print height")
        case "4":
            print("Black Height")
        case "5":
            print("Tree Size")
        case "0":
            print("Exit")
        case _:
            print("Invalid Input")


from tree import RBTree
import dict
# using the BFS concept using queue
def print_level_order(root):
    if root is None:
        print("Empty Tree")
        return

    queue = [root]
    level = 0
    print("\n=== Tree Level Print ===")
    while queue:
        level_size = len(queue)
        print(f"Level {level}: ", end="")
        for _ in range(level_size):
            current_node = queue.pop(0)
            color = "⚫(BLK)" if current_node.color == "black" else "🔴(RED)"
            print(f"[{current_node.key} {color} ]   ", end="")
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        print() 
        level += 1
    print("=========================================\n")


if __name__ == "__main__":
    my_tree = RBTree()

    test_words = ['a', 'b', 'c', 'd', 'e']
    
    print(" Our Test Words: ", test_words)
    
    for word in test_words:
        my_tree.insert(word)

    print_level_order(my_tree.root)
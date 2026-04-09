class Node:
    def __init__(self, key):
        self.key = key
        #self.value = value 
        # Default Settings
        self.color = "red"  
        self.left = None
        self.right = None
        self.parent = None

    # Functions
    def display_node(self):
        print(f"{self.key}:[{self.color.upper()}]")

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # auto insert
        new_node = Node(key)

        # if empty , then it is the root 
        if self.root is None:
            self.root = new_node
            return new_node # some sort of basic log system

        current = self.root
        parent = None

        # the placement if not empty
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # if it exist 
                return current

        # attach the new with its parent
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # basic log system for the usage of RB 
        return new_node

    # search & DFS & Height Calculations(your turn 😀)


class RBTree(BST):
    def __init__(self):
        # constructing as basic bst
        super().__init__()

    def insert(self, key):
        # using the basic log system provided by the parent to test the new node & its parent
        new_node = super().insert(key)

        # the test
        if new_node.color == "red":
            self.fixup_insert(new_node)

    def fixup_insert(self, node):

        pass

       # at the end 
        self.root.color = "black" 

    # utilities for the fix up
    def left_rotate(self, node):
        pass

    def right_rotate(self, node):
        pass
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

    # search & DFS & Height Calculations
    def height(self,root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left),self.height(root.right))
    
    def SearchTree(self,node,key):
        if node==None:
            return None
        if node.key == key:
            return node
        else:
            if node.key > key:
                return self.SearchTree(node.left,key)
            else:
                return self.SearchTree(node.right,key)
    
    def size(self,root):
        if root is None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)
        



class RBTree(BST):
    def __init__(self):
        super().__init__()

    def _get_color(self, node):
        # if there is no node , consider it NIL
        if node is None:
            return "black"
        return node.color

    def insert(self, key):
        new_node = super().insert(key)
        
        if new_node.color == "red":
            self.fixup_insert(new_node)

    def fixup_insert(self, z):
        # getting the grand parent
        while z.parent is not None and z.parent.color == "red":
            grandparent = z.parent.parent
            
            # case of parent is the left child
            if z.parent == grandparent.left:
                y = grandparent.right  # y is the uncle
                
                # Case 1
                if self._get_color(y) == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    grandparent.color = "red"
                    z = grandparent  # propageting up 
                
                else:
                    # Case 2
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    
                    # Case 3
                    # if case 2 , it will auotmatic enter here
                    z.parent.color = "black"
                    grandparent.color = "red"
                    self.right_rotate(grandparent)
            
            # if the parent is the right child
            else:
                y = grandparent.left  # y is the Uncle
                
                # Case 1
                if self._get_color(y) == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    grandparent.color = "red"
                    z = grandparent
                
                else:
                    # Case 2
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    
                    # Case 3
                    z.parent.color = "black"
                    grandparent.color = "red"
                    self.left_rotate(grandparent)
        self.root.color = "black"
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        
        if y.left is not None:
            y.left.parent = x
            
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        
        x = y.left
        y.left = x.right
        
        if x.right is not None:
            x.right.parent = y
            
        x.parent = y.parent
        
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
            
        x.right = y
        y.parent = x
        
    def blackHeight(self ,root):
        if root is None:
            return 0

        elif root.color == 'black':
            return 1+max(self.blackHeight(root.left),self.blackHeight(root.right))
        else:
            return max(self.blackHeight(root.left),self.blackHeight(root.right))

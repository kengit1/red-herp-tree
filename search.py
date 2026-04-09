def SearchTree(node,key):
    if node.key == key:
        return node
    else:
        if node.key < key:
            return SearchTree(node.left,key)
        else:
            return SearchTree(node.right,key)






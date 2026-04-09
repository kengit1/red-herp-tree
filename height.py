def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left),height(root.right))


def blackHeight(root):
    if root is None:
        return 0

    elif root.color == 'black':
        return 1+max(blackHeight(root.left),blackHeight(root.right))
    else:
        return max(blackHeight(root.left),blackHeight(root.right))

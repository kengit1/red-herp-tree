def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left),height(root.right))


def blackHeight(root):
    if root is None:
        return 0
    leftbh=blackHeight(root.left)
    rightbh=blackHeight(root.right)
    if leftbh!=rightbh or leftbh==-1 or rightbh==-1:
        print("Invalid Tree!!!")
        return -1

    elif root.color == 'black':
        return 1+leftbh
    else:
        return leftbh


# this class hold the property of node that to be added in tree
class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

"""
types of traversal:
inorder  = left_node -> root -> right_node
preorder = root -> left_node -> right_node
postorder = left_node -> right_node -> root
"""

def inorder(root):
    if root.left:  #checking it left node is None or not
        inorder(root.left)  # if it is not None, calling inorder function recursively
    print(root.val, end=" ")  # print val values from node
    if root.right:
        inorder(root.right)

def preorder(root):
    print(root.val, end=" ")
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)

def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.val, end=" ")


#binary tree can be in anyorder,but bst left subtree contains lower val and right subtree conatins greater val
#binary search tree(bst)
#left part of node have lower val
#right part of node have greater val
def inserting_node(root, data):
    if root: #checking if root not is empty or not
        if data > root.val:  #if data is greate than root.val, it is added to right subtree
            if root.right:
                inserting_node(root.right, data)
            else:
                root.right = node(data)   # ******remember to use node(data) not just data*******,we should add left ,right property to all nodes
        elif data < root.val:
            if root.left:
                inserting_node(root.left, data)
            else:
                root.left = node(data)
    else:
        root = node(data)



def searching_node(root, data):
    # if root:
    #     if data > root.val:
    #         if root.right is None:
    #             print("notfound")
    #         elif root.right.val == data:
    #             print("found")
    #         searching_node(root.right, data)
    #     elif data < root.val:
    #         if root.left is None:
    #             print("notfound")
    #         elif root.left.val == data:
    #             print("found")
    #         searching_node(root.left, data)

    if data > root.val:
        if root.right:
            searching_node(root.right, data)
        else:
            print("notfound")
    elif data < root.val:
        if root.left:
            searching_node(root.left, data)
        else:
            print("notfound")
    else:
        print("found")
        



root = node(20)

#we can manually data values in tree
# root.left = node(100)
# root.right = node(19)

inserting_node(root, 90)
inserting_node(root, 100)
inserting_node(root, 120)
inserting_node(root, 12)
inserting_node(root, 4)

# inorder(root)
# print("\n")
# preorder(root)
# print("\n")
# postorder(root)

searching_node(root, 104)

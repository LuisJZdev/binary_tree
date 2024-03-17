from binary_tree import BinaryTree

tree = BinaryTree(root_value=5)
tree.add(value=3)
tree.add(value=6)
tree.add(value=7)
tree.add(value=4)
tree.add(value=1)

print("     ", tree.root_value)
print(" ",tree.left.root_value,"    ",tree.right.root_value)
print(tree.left.left.root_value," ",tree.left.right.root_value,"      ", tree.right.right.root_value)

assert tree.search(value=6) == True
assert tree.search(value=3) == True
assert tree.search(value=4) == True
assert tree.search(value=7) == True
assert tree.search(value=8) == False
assert tree.length == 6

print("Blues!!!")
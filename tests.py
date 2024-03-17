from binary_tree import BinaryTree

tree = BinaryTree(root_value=5)
tree.add(value=3)
tree.add(value=6)
tree.add(value=7)
tree.add(value=4)
tree.add(value=1)
tree.add(value=6.5)
tree.add(value=7.5)
tree.add(value=8.5)
tree.add(value=2)
tree.add(value=5)

# print("     ", tree.root_value)
# print(" ",tree.left.root_value,"    ",tree.right.root_value)
# print(tree.left.left.root_value," ",tree.left.right.root_value,"      ", tree.right.right.root_value)

assert tree.search(value=6) == True
assert tree.search(value=3) == True
assert tree.search(value=4) == True
assert tree.search(value=7) == True
assert tree.search(value=8) == False
print("")
tree.show()

print("")
print(50*"*")
print("")

tree_2 = BinaryTree(root_value=3)
tree_2.add(4)
tree_2.add(6)
tree_2.add(7)
tree_2.add(5)
tree_2.add(4.5)

tree_2.show()

print("")
print(50*"*")
print("")

tree_2.remove(value=6)

tree_2.show()

tree_2.remove(value=7)

print("")
print(50*"*")

tree_2.show()

tree_2.remove(value=4.5)

print("")
print(50*"*")

tree_2.show()

print("")
print(50*"*")

tree.remove(value=3)

tree.show()

print("")
print(50*"*")

tree.remove(value=7)

tree.show()

print("")
print(50*"*")

tree.remove(value=15)

tree.show()


print("Blues!!!")
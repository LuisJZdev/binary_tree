class BinaryTree:
    def __init__(self, root_value=None):
        self.root_value = root_value
        self.left = None
        self.right = None

    def add(self, value) -> None:

        def recursion(node: BinaryTree, value) -> None:
            if not node.root_value:
                node.root_value = value
            elif value < node.root_value:
                if node.left == None:
                    node.left = BinaryTree(root_value=value)
                else:
                    recursion(node=node.left, value=value)
            elif value >= node.root_value:
                if node.right == None:
                    node.right = BinaryTree(root_value=value)
                else:
                    recursion(node=node.right, value=value)

        recursion(node=self, value=value)

    def __add_node(self, node):

        def recursion(node: BinaryTree, value) -> None:

            if node.root_value == None:
                node.root_value = value.root_value
                node.left = value.left
                node.right = value.right
            elif value.root_value < node.root_value:
                if node.left == None:
                    node.left = value
                else:
                    recursion(node=node.left, value=value)
            elif value.root_value >= node.root_value:
                if node.right == None:
                    node.right = value
                else:
                    recursion(node=node.right, value=value)

        recursion(node=self, value=node)

    def search(self, value) -> bool:

        def recursion(node: BinaryTree, value) -> bool:
            if node == None:
                return False
            elif node.root_value == value:
                return True
            elif value < node.root_value:
                return recursion(node=node.left, value=value)
            elif value >= node.root_value:
                return recursion(node=node.right, value=value)

        return recursion(node=self, value=value)

    def show(self) -> None:

        def recursion(node: BinaryTree, space=0) -> None:
            
            if node.left:
                recursion(node=node.left, space=space+1)

            print("   "*space, node.root_value)

            if node.right:
                recursion(node=node.right, space=space+1)
        
        recursion(node=self)

    def remove(self, value) -> None:

        def recursion(node: BinaryTree, value) -> None:
            if node.root_value == value:

                left = node.left
                right = node.right

                node.root_value = None
                node.left = None
                node.right = None

                if left:
                    self.__add_node(node=left)
                if right:
                    self.__add_node(node=right)

            elif value < node.root_value:

                if node.left == None:
                    return None

                if (node.left.root_value == value) and (node.left.left == None and node.left.right == None):
                    node.left = None
                else:
                    return recursion(node=node.left, value=value)
            elif value >= node.root_value:

                if node.right == None:
                    return None

                if (node.right.root_value == value) and (node.right.left == None and node.right.right == None):
                    node.right = None
                else:
                    return recursion(node=node.right, value=value)
        
        recursion(node=self, value=value)
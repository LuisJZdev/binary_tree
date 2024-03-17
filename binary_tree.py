class BinaryTree:
    def __init__(self, root_value=None):
        self.root_value = root_value
        self.left = None
        self.right = None

    def add(self, value) -> None:

        def recursion(node: BinaryTree, value) -> None:
            if not node.root_value:
                node.root_value = value
                node.length = 1
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

    def search(self, value) -> bool:

        def recursion(node: BinaryTree, value) -> bool:
            if node.root_value == value:
                return True
            elif node.right == None and node.left == None:
                return False
            elif value < node.root_value:
                return recursion(node=node.left, value=value)
            elif value >= node.root_value:
                return recursion(node=node.right, value=value)

        return recursion(node=self, value=value)
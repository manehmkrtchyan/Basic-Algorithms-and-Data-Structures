class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self) -> None:
        self.root = None
        
    def search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def search_iterative(self, root, key):
        current = root
        while current is not None:
            if current.value == key:
                return current
            elif current.value < key:
                current = current.right
            else:
                current = current.left
        return None
    
    def insert_recursive(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self._insert_recursive(root.left, value)
        elif value > root.value:
            root.right = self._insert_recursive(root.right, value)

        return root
    
    def insert_iterative(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
    
    def get_height_recursive(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)
        return max(left_height, right_height) + 1
        
    def get_height_iterative(self):
        if self.root is None:
            return 0
        max_height = 0
        stack = [(self.root, 1)]
        while stack:
            node, height = stack.pop()
            max_height = max(max_height, height)
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
        return max_height

    def is_empty_recursive(self):
        return True if self.get_height_recursive() == 0 else False
    
    def is_empty_iterative(self):
        return True if self.get_height_iterative() == 0 else False
        
    def get_number_of_nodes_iterative(self):
        if self.root is None:
            return 0
        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

    def get_number_of_nodes_recursive(self):
        return self._get_number_of_nodes_recursive(self.root)

    def _get_number_of_nodes_recursive(self, node):
        if node is None:
            return 0
        left_count = self._get_number_of_nodes_recursive(node.left)
        right_count = self._get_number_of_nodes_recursive(node.right)
        return left_count + right_count + 1    
        
    def get_root_data(self):
        return self.root.value if self.root else None    
        
    def remove_recursive(self, data):
        self.root = self._remove_recursive(self.root, data)

    def _remove_recursive(self, node, data):
        if node is None:
            return node
        if data < node.value:
            node.left = self._remove_recursive(node.left, data)
        elif data > node.value:
            node.right = self._remove_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor_parent = node.right
                successor = successor_parent
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left
                if successor_parent != node.right:
                    successor_parent.left = successor.right
                    successor.right = node.right
                successor.left = node.left
                return successor
        return node

    def remove_iterative(self, data):
        if self.root is None:
            return
        parent = None
        current = self.root
        while current is not None:
            if data < current.value:
                parent = current
                current = current.left
            elif data > current.value:
                parent = current
                current = current.right
            else:
                if current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor_parent = current
                    successor = current.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    if successor_parent != current:
                        successor_parent.left = successor.right
                        successor.right = current.right
                    successor.left = current.left
                    if parent is None:
                        self.root = successor
                    elif parent.left == current:
                        parent.left = successor
                    else:
                        parent.right = successor
                break
            parent = current
    
    def clear_iterative(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left = None
            node.right = None
        self.root = None

    def clear_recursive(self):
        self._clear_recursive(self.root)
        self.root = None

    def _clear_recursive(self, node):
        if node is None:
            return
        self._clear_recursive(node.left)
        self._clear_recursive(node.right)
        node.left = None
        node.right = None
                
    def contains_recursive(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)
                
    def contains_iterative(self, value):
        if self.root is None:
            return False
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif current.value < value:
                current = current.right
            else:
                current = current.left
        return False            
                
    def preorder_iterative(self):
        if self.root is None: return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value, end = ' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
    def preorder_recursive(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is None: return
        print(node.value, end=" ")
        self._preorder_recursive(node.left) 
        self._preorder_recursive(node.right)
        
    def inorder_iterative(self):
        if self.root is None:
            return
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.value, end=" ")  # Process the node
            current = current.right 
        
    def inorder_recursive(self):
        self._inorder_recursive(self.root)    
        
    def _inorder_recursive(self, node):
        if node is None: return
        self._inorder_recursive(node.left) 
        print(node.value, end=" ")
        self._inorder_recursive(node.right) 
        
    def postorder_iterative(self):
        if self.root is None:
            return
        stack = [self.root]
        result = []
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        for value in reversed(result):
            print(value, end=" ")
        
    def postorder_recursive(self):
        self._postorder_recursive(self.root)    
        
    def _postorder_recursive(self, node):
        if node is None: return
        self._postorder_recursive(node.left) 
        self._postorder_recursive(node.right)    
        print(node.value, end=" ")
        
    def print(self):
        self._print_tree_recursive(self.root, "")

    def _print_tree_recursive(self, node, prefix):
        if node is None:
            return
        self._print_tree_recursive(node.right, prefix + "    |")
        if prefix == "":
            print(node.value)
        else:
            print(prefix[:-3] + "    |--", node.value)
        self._print_tree_recursive(node.left, prefix + "    |")
    

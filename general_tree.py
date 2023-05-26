class Node:
    def __init__(self, value: 'function' = None) -> None:
        self.value = value
        self.children = []
        
    def add_child(self, value: 'function' = None):
        new = Node(value)
        self.children.append(new)
        
    def set_func(self, func):
        self.value = func

    def remove_func(self):
        self.value = None
        
class GeneralTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        
    def execute(self, number):
        return self._execute_recursive(self.root, number)
    
    def _execute_recursive(self, node, number):
        if node.value is not None:
            number = node.value(number)
        for child in node.children:
            number = self._execute_recursive(child, number)
        return number
    
 
func1 = lambda x: x * 100
func2 = lambda x: x + 50
func3 = lambda x: x - 20
func4 = lambda x: x // 10
  
            
tree = GeneralTree(func1)
tree.root.add_child(func2)
tree.root.add_child(func4)
tree.root.children[0].add_child(func3)


result = tree.execute(5)
print(result)  #53

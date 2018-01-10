#pseudo code
'''
node_count = size of queue
if node count is 0, return height
else increase height

while node count > 0
pop node from front 
push children to queue
decrease node count
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_height(root):
    if root is None:
        return 0
    
    queue = []
    queue.append(root)
    height = 0
    while(True):
        node_count = len(queue)
        if node_count == 0:
            return height
        height += 1
        
        while(node_count > 0):
            node = queue[0]
            queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node_count -= 1
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print "Height of tree is", find_height(root)
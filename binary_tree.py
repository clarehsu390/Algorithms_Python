class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(head, result):
    if head is not None:
        inorder_traversal(head.left, result)
        result.append(head.val)
        inorder_traversal(head.right, result)


head = Node(5)

head.left = Node(3)
head.left.left = Node(1)
head.left.right = Node(4)
head.left.left.left = Node(0)
head.left.left.right = Node(2)

head.right = Node(6)
head.right.right = Node(8)
head.right.right.left = Node(7)
head.right.right.right = Node(9)

    # result will store the output
result = []
inorder_traversal(head, result)

print("Extracted Double Linked list is")
print(' '.join(str(res) for res in result))


#Time Complexity: O(n), does a single traversal of given Binary Tree
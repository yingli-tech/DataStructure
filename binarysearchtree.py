class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value=val
        self.leftChild=left
        self.rightChild=right

    def insert(self, value, node):
        if value < node.value:
            # If the left child node does not exist, set the new value as the left child node.
            if node.leftChild is None:
                node.leftChild=TreeNode(value)
            else:
                self.insert(value, node.leftChild)

        elif value > node.value:
            # If the right child node does not exist, set the new value as the right child node.
            if node.rightChild is None:
                node.rightChild=TreeNode(value)
            else:
                self.insert(value, node.rightChild)

    def traverse(self, node):
        if node is None:
            self.traverse(node.leftChild)
            # When you set end='', it means that after printing the content, 
            # it will not move to the next line, but will continue to print the subsequent content directly.
            print(node.value)
            self.traverse(node.rightChild)

    def search(self, value, node):
            # base case: if the node does not exist
            # or the value of the node meets the condition
            if node is None or node.value==value:
                return node

            # If the value is less than the current node, search from the left child node.
            elif value < node.value:
                return self.search(value, node.leftChild)

            # If the value is greater than the current node, search from the right child node.
            else: # value > node.value
                return self.search(value, node.rightChild)
            
    def delete(self, valueToDelete, node):
        # There are no child nodes in the level above the current position, and we have reached the bottom layer of the tree (the base case)
        if node is None:
            return None
        # If the value to be deleted is less than (or greater than) the current node
        # recursively call this method with the left subtree (or right subtree) as the parameter
        # and then point the left link (or right link) of the current node to the returned node.

        elif valueToDelete < node.value:
            node.leftChild = self.delete(valueToDelete, node.leftChild)
            # Return the current node (and its subtree, if it exists)
            # As the new left child node (or new right child node) of its parent node
            return node
        elif valueToDelete > node.value:
            node.rightChild = self.delete(valueToDelete, node.rightChild)
            return node
        # If the node to be deleted is exactly the current node
        elif valueToDelete == node.value:
            # if the current node has no left child node, replace the current node with its right child node (and its subtree, if it exists) to become the new child node of the current node’s parent node.
		if node.leftChild is None:
                return node.rightChild
            # If the current node doesn't have left child node or right child node, then return None from here
            elif node.rightChild is None:
                return node.leftChild
            # if the current node has two child nodes, then delete the current node with lift function
            # It will change the value of the current node to the value of its successor node.
            else:
                node.rightChild = self.lift(node.rightChild, node)
                return node

    def lift(self,node, nodeToDelete):
        # If the current node has a left child node
        # Then recursively call this function to find the successor node from the left subtree
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        # If the current node of this function has no left child node
        # it means the current node is the successor node; 
        # therefore, set its value as the new value of the deleted node.
        else:
            nodeToDelete.value = node.value
        # Replace the left child node of the successor node's parent node with the right child node of the successor node.
            return node.rightChild

root = TreeNode(25)
"""
node3 = TreeNode(14)
node2 = TreeNode(10)
root1 = TreeNode(20, node, node2)
root2 = TreeNode(225, node3, root1)
root3 = TreeNode(120, root2, node3)
root = TreeNode(1962, root2, root3)
"""
array = [98, 20, 10, 15, 33,11,98,2,6,75,48]

for i in range (len(array)-1):
    root.insert(array[i],root)
root.traverse(root)
a = root.search(20,root)
print("the following number exists in the BTS, and its value is ")
print(a.value)
root.delete(20, root)
print("the new tree is ")
root.traverse(root)

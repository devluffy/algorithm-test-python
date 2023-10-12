class Node:
    def __init__(self, number, left_node, right_node) -> None:
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node):
    if(node.left_node != -1):
        in_order(tree[node.left_node])
    
    
    if(node.rigth_node != -1):
        in_order(tree[node.right_node])
        

n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1


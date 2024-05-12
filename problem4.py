class Node:
    def __init__(self, name, count, is_girl):
        self.name = name
        self.count = count
        self.is_girl = is_girl
        self.parent = None
        self.children = []
        self.message = 0

root = Node("Teacher", 1, False)
child1 = Node("Hansel", 1, False)
child2 = Node("Gretel", 1, True)
child3 = Node("Alice", 1, True)
child4 = Node("Bob", 1, False)

root.children = [child1, child2, child3, child4]
child1.parent = root
child2.parent = root
child3.parent = root
child4.parent = root

def count_children(node):   
    if is_leaf(node):
        node.message = node.count
        send_message(node.parent, node.message)
    else:
        for child in node.children:
            message = receive_message(child)
            node.message += message
        node.message += node.count
        if is_root(node):
            broadcast_message(node.children, node.message)
        else:
            send_message(node.parent, node.message)
            total_count = receive_message(node.parent)
            node.message = total_count
            broadcast_message(node.children, total_count)


count_children(root)

print("Total count:", root.message)
print("Hansel:", child1.message)
print("Gretel:", child2.message)
print("Alice:", child3.message)
print("Bob:", child4.message)

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "A node with value {} ".format(self.value)

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_after(self, after, new_value):
        new_node = Node(new_value)
        current_node = self.get_head_node()
        while current_node:
            next_node = current_node.get_next_node()
            if current_node.get_value() == after:
                new_node.set_next_node(next_node)
                current_node.set_next_node(new_node)

                current_node = None
            else:
                current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != 111:
                if current_node.get_next_node() != None:
                    string_list += str(current_node.get_value()) + " -> "
                else:
                    string_list += str(current_node.get_value())
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            try:
                while current_node:
                    next_node = current_node.get_next_node()
                    if next_node.get_value() == value_to_remove:
                        current_node.set_next_node(next_node.get_next_node())
                        current_node = None
                    else:
                        current_node = next_node
            except AttributeError:
                print("There is no Node with the value to remove.")

a = Node(-1)
ll = LinkedList(0)
a = [1,2,3,4,5,"a","b","c"]
for x in a:
    ll.insert_beginning(x)
print(ll.stringify_list())
ll.remove_node("a")
print(ll.stringify_list())
ll.insert_after(0,"A")
print(ll.stringify_list())
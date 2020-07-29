class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def __repr__(self):
        return "A node with value {} ".format(self.value)

    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

    def get_value(self):
        return self.value

class DoubleLinkedList:
    def __init__(self,value=None):
        self.head_node = Node(value)
        self.tail_node = self.head_node

    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node.set_previous_node(new_node)
        self.head_node = new_node

    def insert_ending(self, new_value):
        new_node = Node(new_value)
        new_node.set_previous_node(self.tail_node)
        self.tail_node.set_next_node(new_node)
        self.tail_node = new_node

    def insert_after_value(self, after, new_value):
        new_node = Node(new_value)
        current_node = self.head_node
        while current_node:
            if current_node.get_value() == after:
                if current_node == self.get_tail_node():
                    self.insert_ending(new_value)
                    break
                new_node.set_previous_node(current_node)
                new_node.set_next_node(current_node.get_next_node())
                current_node.get_next_node().set_previous_node(new_node)
                current_node.set_next_node(new_node)
                current_node = None
            else:
                current_node = current_node.get_next_node()

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:

            if current_node.get_next_node() != None:
                string_list += str(current_node.get_value()) + " <=> "
            else:
                string_list += str(current_node.get_value())
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, direction, value_to_remove):
        if direction.lower() == 'h':
            current_node = self.head_node
            if current_node.get_value() == value_to_remove:
                self.head_node = current_node.get_next_node()
                self.head_node.set_previous_node(None)
            else:
                while current_node:
                    if current_node.get_value() == value_to_remove:
                        current_node.get_previous_node().set_next_node(current_node.get_next_node())
                        current_node.get_next_node().set_previous_node(current_node.get_previous_node())
                        current_node = None
                    else:
                        current_node = current_node.get_next_node()
        elif direction.lower() == 't':
            current_node = self.tail_node
            if current_node.get_value() == value_to_remove:
                self.tail_node = current_node.get_previous_node()
                self.tail_node.set_next_node(None)
            else:
                while current_node:
                    if current_node.get_value() == value_to_remove:
                        current_node.get_previous_node().set_next_node(current_node.get_next_node())
                        current_node.get_next_node().set_previous_node(current_node.get_previous_node())
                        current_node = None
                    else:
                        current_node = current_node.get_previous_node()



dbll = DoubleLinkedList()
for i in range(5):
    dbll.insert_beginning(i)
    dbll.insert_ending(i+5)
print(dbll.stringify_list())
dbll.remove_node('h', 3)
print(dbll.stringify_list())

dbll.remove_node('t', 8)
print(dbll.stringify_list())

dbll.insert_after_value(9,10)
print(dbll.stringify_list())
print(dbll.get_head_node())
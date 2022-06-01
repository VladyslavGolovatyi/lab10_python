class Node:
    def __init__(self, model: str, resistance: float, power: float, precision: float):
        self.model = model
        self.resistance = resistance
        self.power = power
        self.precision = precision
        self.next = None
        self.prev = None

    def __str__(self):
        return "Resistor {}\nResistance = {} Ohms\nPower = {} W\nPrecision = {} %\n".\
            format(self.model, self.resistance, self.power, self.precision)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_info(self, min_precision: int):
        current_node = self.head
        if current_node.precision > min_precision:
            print(current_node)
        current_node = current_node.next
        while current_node != self.head:
            if current_node.precision > min_precision:
                print(current_node)
            current_node = current_node.next
        print("\n")

    def insert(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            node.prev = node
        else:
            if node.resistance < self.head.resistance or \
                    (node.resistance == self.head.resistance and node.model <= self.head.model):
                node.next = self.head
                node.prev = self.head.prev
                self.head.prev.next = node
                self.head.prev = node
                self.head = node
            else:
                current_node = self.head.next
                while current_node != self.head:
                    if node.resistance < current_node.resistance or \
                             (node.resistance == current_node.resistance and node.model <= current_node.model):
                        node.next = current_node
                        node.prev = current_node.prev
                        current_node.prev.next = node
                        current_node.prev = node
                        break
                    elif current_node.next == self.head:
                        current_node.next = node
                        self.head.prev = node
                        node.next = self.head
                        node.prev = current_node
                        break
                    current_node = current_node.next

#!/usr/bin/python3
"""
class of Node that defines a node of a singly linked list
"""


class Node:
    """
    represent a node in a single linked list
    """
    def __init__(self, data, next_node=None):
        """initialize a new Node.

        Args:
            data (int): the data of the new node
            next_node (Node): next node of the node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ get/set the data of the node.

        Returns:
            int: self.__data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ the setter part

        Args:
            value : the value passed as a tuple

        Raises:
            TypeError: checks if the value is integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ initializing a getter and a setter

        Returns:
            _type_: self.__next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ the setter part

        Args:
            value : the value passed

        Raises:
            TypeError: checks if it is a Node or NOne
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""
class of SinglyLinkedList that defines a singly linked list
"""
class SinglyLinkedList:
    """
    implementing the singlyLinkedList
    """
    def __init__(self):
        """
        initializer
        """
        self.__head = None

    def sorted_insert(self, value):
        """ sortes the list in increasing order

        Args:
            value (int): the value that is passed
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

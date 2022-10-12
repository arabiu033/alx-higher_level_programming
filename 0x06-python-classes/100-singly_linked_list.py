#!/usr/bin/python3
""" No Modules Imported """


class Node:
    """ Singly linked list will be built base on this Node """
    __data = 0
    __next_node = None

    def __init__(self, data=0, next_node=None):
        """ Initialize the node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Return class __data value """
        return self.__data

    @property
    def next_node(self):
        """ Reurn class __next_node__ value """
        return self.__next_node

    @data.setter
    def data(self, data):
        """ Set class __data value """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @next_node.setter
    def next_node(self, next_node):
        """ Set class __next_node value """
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """ A Singly Linked list """
    __head = None

    def __init__(self):
        """ Initialize class varaibles """
        self.__head = None

    def sorted_insert(self, value):
        """ Sort and add the new node at the appropriate place """
        if self.__head is None:
            self.__head = Node(value, None)
            return

        temp = self.__head
        hold = None
        while temp and value > temp.data:
            hold = temp
            temp = temp.next_node

        if hold is not None:
            new = Node(value, temp)
            self.__head = new
            return

        new = Node(value, temp)
        hold.next_node = new

    def __repr__(self):
        """ Serve as a string """
        temp = self.__head
        while temp and temp.next_node:
            print(temp.data)
            temp = temp.next_node
        if temp:
            print(temp.data, end="")
        return ""

import DoublyLinkedList
from LinkedList import *
from DoublyLinkedList import *

class QueuePythonList:
    def __init__(self, LIST = []):
        self.__list = LIST
    def enqueue(self, item):
        '''
        adds item to end of list
        :param item: any
        :return: new list
        '''
        return self.__list.append(item)
    def dequeue(self):
        '''
        removes the item at index[0]
        :return: the item that was deleted from list
        '''
        return self.__list.pop(0)
    def is_empty(self):
        '''
        checks to see if list is empty
        :return: True if yes False if No
        '''
        if len(self.__list) == 0:
            return True
        else:
            return False
    def size(self):
        '''
        takes len(self.__list)
        :return: length
        '''
        return len(self.__list)
class QueueLinkedList:
    def __init__(self):
        self.list = LinkedList()
    def size(self):
        '''
        Call LinkedList.size()
        :return: self.length
        '''
        self.list.size()
    def is_empty(self):
        '''
        Call LinkedList.is_empty
        :return: True or False
        '''
        return self.list.is_empty()
    def enqueue(self, data):
        '''
        Call LinkedList.append
        :param data: and data
        :return:
        '''
        self.list.append(data)
    def dequeue(self):
        '''
        Pop the last element in the linked list
        :return:
        '''
        self.list.pop(0)
class QueueDoublyLinkedList:
    def __init__(self):
        self.list = DoublyLinkedList()
    def size(self):
        '''
        Call size method in DLL
        :return: self.length
        '''
        self.list.size()
    def is_empty(self):
        '''
        Call is_empty method in DLL
        :return: True or False
        '''
        return self.list.is_empty()
    def enqueue(self, data):
        '''
        Append to the DLL
        :param data: Any data
        :return:
        '''
        self.list.append(data)
    def dequeue(self):
        '''
        Pop first element in DLL
        :param self:
        :return: the element
        '''
        self.list.pop(0)

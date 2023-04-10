#Jackson Snyder
#CSC-232
#03-20-2022
#LinkedList
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self, length = 0):
        self.head = None
        self.length = length
    def is_empty(self):
        '''
        Checks to see if self.head = None
        :return:True:if self.head = None, False if self.head != None
        '''
        if self.length <= 0:
            return True
        else:
            return False
    def add(self, data):
        '''
        Checks to see if the LL is empty, if yes, set self.head = data, if not,
        set self.head.next = self.head and set self.head = data
        :param data: any data type
        :return: N/A
        '''
        self.length += 1
        newNode = Node(data)
        if self.head != None:
            newNode.next = self.head
        else:
            current = self.head
            newNode.next = current
        self.head = newNode
    def append(self, data):
        '''
        Checks to see if the list id empty, if yes, set self.head = data, if not,
        iterate over the list till the end(when current.next = None) then set current.next = data,
        and current.next.next = None
        :param data: any data type
        :return: N/A
        '''
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.length += 1
    def size(self):
        '''
        Throughout the class, self.length increases and decreases based on the amount
        that append, add, remove and pop are called
        :return: total nodes in LL
        '''
        return self.length
    def pop(self, pos = None):
        '''
        First, "index" to pop, if None, set pos = len(LL)-1, then check if the input was correct
        if pos == 0, set self.head = self.head.next,
        if not, iterate through the LL keeping track of the current and previous nodes, returning the
        current node once current == data for one of the node's data
        :param pos: "index" of the pop
        :return:data at the popped node
        '''
        if pos == None:
            pos = self.size()-1
        if not isinstance(pos, int) or pos < 0 or pos > self.size()-1:
            return None
        if pos == 0:
            current = self.head
            if current.next == None:
                current = None
            else:
                self.head = current.next
        else:
            counter = 0
            current = self.head
            previous = self.head
            while counter != pos:
                previous = current
                current = current.next
                counter += 1
            previous.next = current.next
        self.length -= 1
        return current
    def __iter__(self):
        '''
        iterates through the LL
        :return: N/A
        '''
        current = self.head
        while current is not None:
            yield current
            current = current.next
    def search(self, data):
        '''
        iterates through the LL till a Node's data == data, return True of
        data ever == data, False if not
        :param data:
        :return: Boolean
        '''
        current = self.head
        for i in range(self.size()):
            if str(current) == str(data):
                return True
            else:
                current = current.next
        return False
    def remove(self, data=None):
        '''
        Searchs through the LL to find what Node data is located,
        removing that node from the list by setting its previous next to its current next
        :param data: any data type
        :return: N/A
        '''
        if data == None:
            print('TypeError: Must enter a piece of data to remove, Please try again.')
            return None
        else:
            if self.head == None:
                return None
            else:
                current = self.head
                previous = current
                while str(current) != data:
                    previous = current
                    current = current.next
                    if current == None:
                        print(data, ' is not in the list')
                        return None
                if current.next == None:
                    previous.next = None
                    self.length -= 1
                elif current.next == self.head.next:
                    self.head = self.head.next
                    self.length -= 1
                else:
                    previous.next = current.next
                    self.length -= 1

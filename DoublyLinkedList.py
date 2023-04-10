class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
    def __str__(self):
        return str(self.data)
class DoublyLinkedList:
    def __init__(self, length = 0):
        self.head = None
        self.length = length
        self.tail = None
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
        if self.head == None:
            newNode.next = self.head
            self.tail = newNode
        elif self.head == self.tail:
            self.head = newNode
            newNode.next = self.tail
            self.tail.previous = newNode
        else:
            current = self.head
            newNode.next = current
            current.previous = newNode
        self.head = newNode
    def append(self, data):
        '''
        Checks to see if the list is empty, if yes, set self.head = data, if not,
        iterate over the list till the end(when current.next = None) then set current.next = data,
        and current.next.next = None also setting self.tail.previous = self.tail and self.tail to data
        :param data: any data type
        :return: N/A
        '''
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif self.head == self.tail:
            self.tail = newNode
            newNode.previous = self.head
            self.head.next = newNode
        else:
            current = self.tail
            previous = self.tail.previous
            previous.next = current
            current = previous
            current.next = newNode
            self.tail = newNode
            newNode.previous = current
        self.length += 1
    def size(self):
        '''
        print self.length
        :return: length of LL
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
            pos = self.length-1
        if not isinstance(pos, int) or pos < 0 or pos > self.length-1:
            return None
        if pos == 0:
            if self.head == self.tail:
                current = self.head
                self.head, self.tail = None, None
            else:
                current = self.head
                self.head = current.next
        elif pos == self.length - 1:
            current = self.tail
            self.tail = current.previous
            self.tail.next = None
        else:
            mid = self.length // 2
            if pos <= mid:
                counter = 0
                current = self.head
                previous = self.head
                while counter != pos:
                    previous = current
                    current = current.next
                    counter += 1
                previous.next = current.next
                current.next.previous = previous
            else:
                counter = self.length - 1
                nxt = self.tail
                current = self.tail
                while counter != pos:
                    nxt = current
                    current = current.previous
                    counter -= 1
                nxt.previous = current.previous
                current.previous.next = nxt
        self.length -= 1
        return current
    def __iter__(self):
        '''
        iterate through the list
        :return: N/A
        '''
        current = self.head
        while current is not None:
            yield current
            current = current.next
    def search(self, data):
        '''
        iterates through the LL and returns True or False depending on if
        data is in a Node
        :param data:any data type
        :return: Boolean
        '''
        current = self.head
        for i in range(self.size()):
            if str(current) == str(data):
                return True
            else:
                current = current.next
        return False
    def remove(self, data):
        '''
        Searchs through the LL to find what Node data is located,
        removing that node from the list by setting its previous next to its current next
        if data = self.tail
        set self.tail = self.tail.previous
        self.tail.next = None
        :param data: any data type
        :return: N/A
        '''
        if self.head == None:
            return None
        else:
            current = self.head
            previous = self.head
            while str(current) != data:
                previous = current
                current = current.next
                if current == None:
                    print(data, 'is not in the list')
                    return None
            if current.next == None:
                self.tail = previous
                self.tail.next = None
                self.length -= 1
            elif current.next == self.head.next:
                self.head = self.head.next
                self.length -= 1
            else:
                previous.next = current.next
                current.next.previous = previous
                self.length -= 1
    def reverse(self):
        previous = None
        current = self.head
        while current != None:
            previous = current.previous
            current.previous = current.next
            current.next = previous
            current = current.previous
        if previous != None:
            self.head = previous.previous
myDLL = DoublyLinkedList()
myDLL.append(1)
myDLL.append(2)
myDLL.append(3)
print(myDLL.head,myDLL.tail)
myDLL.reverse()
print(myDLL.head,myDLL.tail)

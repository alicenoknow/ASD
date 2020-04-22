class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.sentinel = Node(data=0)
        self.sentinel.next = None
        self.last = None

    def pop(self):
        if not self.is_empty():
            tmp = self.sentinel.next
            self.sentinel.next = tmp.next
            self.sentinel.data -= 1
            return tmp


    def add_node(self, node):
        if not self.is_empty():
            self.last.next = node
            self.last.next.next = None
            self.last = self.last.next
        else:
            self.sentinel.next = node
            self.last = node
            self.last.next = None
        self.sentinel.data += 1


    def add(self, data):
        newnode = Node(data=data)
        self.add_node(newnode)


    def is_empty(self):
        return self.sentinel.next == None


    def list_size(self):
        if not self.is_empty():
            return self.sentinel.data
        return 0


    def find_max(self):
        if not self.is_empty():
            tmp = self.sentinel.next
            max_v = tmp.data
            while tmp is not None:
                if tmp.data > max_v:
                    max_v = tmp.data
                tmp = tmp.next
            return max_v


    def insertion_sort(self):
        if self.is_empty():
            return
        curr = self.sentinel.next
        sorted = LinkedList()
        while curr is not None:
            next = curr.next
            sorted.sorted_add(curr)
            curr = next
        self.sentinel.next = sorted
        self.last = sorted.last

    def sorted_add(self, node):
        curr = self.sentinel.next
        if curr is None:
            self.sentinel.next = node
            self.sentinel.next.next = None
            self.last = node
        else:
            while curr.next is not None and curr.next.data < node.data:
                curr = curr.next
            if curr.next is None:
                self.last = node
            node.next = curr.next
            curr.next = node
        self.sentinel.data += 1


    def print_list(self):
        curr = self.sentinel.next
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def append_list(self, newlist):
        self.last.next = newlist.sentinel.next
        self.last = newlist.last
        self.sentinel.data += newlist.sentinel.data

    def bucket_sort_on_lists(self):
        max_v = self.find_max()
        len = self.list_size()
        if self.is_empty():
            return
        buckets = [None for _ in range(len)]
        while not self.is_empty():
            curr = self.pop()
            index = int(curr.data/max_v * (len-1))
            print("idx: ", index, "\n")
            if buckets[index] is None:
                buckets[index] = LinkedList()
                buckets[index].sorted_add(curr)
            else:
                buckets[index].sorted_add(curr)
        for bucket in buckets:
            if bucket is not None:
                bucket.print_list()
                self.append_list(bucket)


head = LinkedList()
head.add(5)
head.add(19)
head.add(65)
head.add(76)
head.add(31)
head.add(12)
head.add(7)
head.bucket_sort_on_lists()
head.print_list()

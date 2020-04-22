class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def insertionSort(head_ref):
    sorted = None                                   # Initialize sorted linked list
    current = head_ref                              # Traverse the given linked list and insert every
    while current is not None:                        # node to sorted
        next = current.next                         # Store next for next iteration
        sorted = sortedInsert(sorted, current)      # insert current in sorted linked list
        current = next                              # Update current
    head_ref = sorted                               # Update head_ref to point to sorted linked list
    return head_ref

# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
def sortedInsert(head_ref, new_node):
    current = None
    if (head_ref == None or (head_ref).data >= new_node.data):  # Special case for the head end */
        new_node.next = head_ref
        head_ref = new_node
    else:
        current = head_ref                                      # Locate the node before the point of insertion
        while current.next != None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
    return head_ref

def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next

def push(head_ref, new_data):
    new_node = Node(new_data,head_ref)
    head_ref = new_node
    return head_ref


a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 4)
a = push(a, 3)
a = push(a, 30)

print("Linked List before sorting ")
printList(a)

a = insertionSort(a)

print("\nLinked List after sorting ")
printList(a) 
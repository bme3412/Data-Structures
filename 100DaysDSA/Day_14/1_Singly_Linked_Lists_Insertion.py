#############################################
####  Single Linked Lists - Insertion    ####
#############################################

## In a singly linked list, each node contains a value and a reference (or pointer) to the next node in the list. 
    ## The last node points to None to indicate the end of the list. 
    ## Insertion in a singly linked list can be performed at different positions: at the beginning, at the end, or at a specific position.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

## 1. Insertion at the Beginning: 
    ## To insert a new node at the beginning of the list, we need to update the head of the list to point to the new node, and the new node should point to the previous head.

def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

# Create a linked list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Insert a new node with value 0 at the beginning
head = insert_at_beginning(head, 0)
# Updated list: 0 -> 1 -> 2 -> 3 -> None

## 2. Insertion at the End: 
    ### To insert a new node at the end of the list, we need to traverse the list until we reach the last node and then update its next pointer to the new node.

def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    return head

# Create a linked list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Insert a new node with value 4 at the end
head = insert_at_end(head, 4)
# Updated list: 1 -> 2 -> 3 -> 4 -> None

## 3. Insertion at a Specific Position: 
    ## To insert a new node at a specific position, we need to traverse the list until we reach the desired position and then update the pointers accordingly.

def insert_at_position(head, value, position):
    if position == 0:
        return insert_at_beginning(head, value)
    
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of range")
        current = current.next
    
    new_node = Node(value)
    new_node.next = current.next
    current.next = new_node
    return head

# Create a linked list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Insert a new node with value 4 at position 2
head = insert_at_position(head, 4, 2)
# Updated list: 1 -> 2 -> 4 -> 3 -> None
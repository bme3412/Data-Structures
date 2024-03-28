#####################################
####   Intro to Linked Lists     ####
#####################################

## A linked list is a linear data structure that consists of a sequence of nodes. 
    ## Each node contains two parts: data and a reference (or pointer) to the next node in the sequence. 
    ## Unlike arrays, linked lists do not store elements in contiguous memory locations. 
    ## Instead, the elements are linked using pointers, allowing for efficient insertion and deletion operations.

## Advantages of Linked Lists over Arrays
    ## Dynamic Size: Linked lists can grow or shrink in size during runtime. They do not have a fixed size like arrays, making them more flexible.

    ## Efficient Insertion and Deletion: Inserting or deleting elements in the middle of a linked list is efficient, as it only requires updating the pointers of the adjacent nodes. In contrast, arrays require shifting elements for insertion or deletion in the middle.

    ## No Memory Wastage: Linked lists allocate memory dynamically for each node, so there is no need to pre-allocate memory like in arrays. This prevents memory wastage.

## Node Structure
    ## In a singly linked list, each node consists of two parts:

    ## Data: Stores the actual value or information.
    ## Next: A reference or pointer to the next node in the sequence.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    ## data: Stores the value or information.
    ## next: Stores a reference to the next node. It is initially set to None to indicate the end of the list.

## Singly Linked List
    ## A singly linked list is a type of linked list where each node contains only a reference to the next node in the sequence. 
    ## The last node in the list points to None to mark the end of the list.

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    ## is_empty(): Checks if the linked list is empty.
    ## append(data): Appends a new node with the given data to the end of the list.
    ## display(): Displays the elements of the linked list.

    # Create a singly linked list
linked_list = SinglyLinkedList()

# Append elements to the list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Display the linked list
linked_list.display()  # Output: 1 2 3
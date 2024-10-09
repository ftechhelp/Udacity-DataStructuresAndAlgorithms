import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
def linked_list_to_set(llist: LinkedList) -> set:
    set_llist = set()
    current_node = llist.head

    while current_node != None:
        set_llist.add(current_node.value)
        current_node = current_node.next

    return set_llist

def set_to_linked_list(set: set) -> LinkedList:
    llist = LinkedList()

    for item in set:
        llist.append(item)

    return llist

def union(llist_1, llist_2):
    set_llist_1 = linked_list_to_set(llist_1)
    set_llist_2 = linked_list_to_set(llist_2)

    unionized_set = set_llist_1.union(set_llist_2)
    unionized_llist = set_to_linked_list(unionized_set)

    return unionized_llist

def intersection(llist_1, llist_2):
    set_llist_1 = linked_list_to_set(llist_1)
    set_llist_2 = linked_list_to_set(llist_2)

    intersected_set = set_llist_1.intersection(set_llist_2)
    intersected_llist = set_to_linked_list(intersected_set)

    return intersected_llist


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("----- Test Case 1 -----")
print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("----- Test Case 2 -----")
print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 3: Empty Linked Lists

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print("----- Test Case 3 -----")
print(union(linked_list_5, linked_list_6)) 
print(intersection(linked_list_5, linked_list_6))

## Test Case 4: Duplicate Values in Both Linked Lists

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1, 1, 1, 2, 2, 3]
element_2 = [1, 1, 2, 2, 3, 3]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("----- Test Case 4 -----")
print(union(linked_list_7, linked_list_8)) 
print(intersection(linked_list_7, linked_list_8))

## Test Case 5: Very Large Linked Lists

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

for _ in range(1000):
    linked_list_9.append(random.randint(1, 100))
    linked_list_10.append(random.randint(1, 100))

print("----- Test Case 5 -----")
print(union(linked_list_9, linked_list_10))
print(intersection(linked_list_9, linked_list_10))
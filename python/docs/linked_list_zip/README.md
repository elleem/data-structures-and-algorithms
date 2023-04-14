## Linked List: Zip Two Lists

Write a method to zip two linked lists and return the new linked list.

argument: 2 linked lists, return: new linked list
Return the node’s value that is k places from the tail of the linked list.
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the zipped list.
~~Try and keep additional space down to O(1)~~
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

### Whiteboard Process

![Linked List Zip Two Lists whiteboard](Whiteboard%20Code%20Challenge%2008.jpg)

### Approach and Efficiency

Creates a new copy of the two lists that I am zipping together.
Initializes current1 and current2, at the head, to move through the linked list
and adds each values to the zipped_list return variable.

O(n) for time and space. The time will be constant based on the input. The space will be constant based on storing the lists.

### Solution

[Code Challenge Linked List Zip Two Lists](Whiteboard%20Code%20Challenge%2008.jpg)

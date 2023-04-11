## Linked List: kth value from the end

Write a method to find kth from the end in the Linked List class.

argument: a number, k, as a parameter.
Return the node’s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

### Whiteboard Process

![Linked List kth whiteboard](Whiteboard%20Code%20Challenge%2007.jpg)

### Approach and Efficiency

Using two pointers, collect the count of the linked list, and then use the second point to move to the kth value after the count is determined.
O(n) time complexity, O(l) space complexity

### Solution

[Code Challenge Linked List](Whiteboard%20Code%20Challenge%2007.jpg)

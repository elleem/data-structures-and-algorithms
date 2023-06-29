## Hashtable Repeated Word

Write a function called repeated_word

- Find the first word to occur more than once in a string

Arguments: string
Return: string

### Whiteboard Process

![Hashtable Repeated Word](hashtable_repeated_word_whiteboard.jpg)

### Approach and Efficiency

Using recursion, iterate through the input tree. Convert the root, then convert each child and re-append to the new_tree value.

The time is O(n) because of the potential length of the string, you may have to iterate through the whole string in order to find a match, or the match may not be present.

The space is O(n) because of the potential length of the string, you may have to store the whole string in the dictionary before finding a match, or the match may not be present.


### Solution

[Hashtable Repeated Word](hashtable_repeated_word_whiteboard.jpg)

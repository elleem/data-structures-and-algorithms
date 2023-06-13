# Blog Notes: Insertion Sort

### Insertion Sort

Insertion sort is a sorting algorithm that traverses a list, in order to sort it.
As it traverses it compares each element to the element before it and inserts it into the correct position.


### Problem Domain
![Problem Domain](images/problem_domain.png)

### Input Output
![Input Output](images/input_output.png)

### Pseudocode
![Pseudocode](images/pseudocode.png)

### Visualization
![Visualization](images/visualization_1.png)
![Visualization](images/visualization_2.png)
![Visualization](images/visualization_3.png)
![Visualization](images/visualization_4.png)
![Visualization](images/visualization_5.png)
![Visualization](images/visualization_6.png)

### Algorithm
![Algorithm](images/algorithm.png)

### Code
![Code](images/code.png)

### Step Through
![Step Through 1](images/step_through_1.png)
![Step Through 2](images/step_through_2.png)

### Big O
Insert:
time: O(n)where the whole input list has to be traversed to be compared
space: O(n) I am not creating an additional list, I am only sorting through it using the temp value

InsertionSort:
time:  I am using def insert within InsertionSort, so at least O(n^2), due to the function being called internally
and the potential input of the input list
space: O(n) if I have to store and sort the whole list

### Tests
![Tests](images/tests.png)


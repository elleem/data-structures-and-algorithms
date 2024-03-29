# Data Structures and Algorithms

## Language: `Python`

### Table of Contents

-[Code Challenge 1](/docs/list_reverse/Code-Challenge-01.jpg)

-[Code Challenge 2](/docs/list_insert_shift/Code-Challenge-02.jpg)

-[Code Challenge 3](/docs/list_binary_search/Code-Challenge-03.jpg)

-[Code Challenge 5,6](/data_structures/linked_list.py)

-[Code Challenge 7](/docs/linked_list_kth/Whiteboard-Code-Challenge-07.jpg)

-[Code Challenge 8](/docs/linked_list_zip/Whiteboard-Code-Challenge-08.jpg)

-[Code Challenge 9](/data_structures/queue.py)

-[Code Challenge 9](/data_structures/stack.py)

-[Code Challenge 11](/docs/stack_queue_pseudo/stack-queue-pseduo.jpg)

-[Code Challenge 12](/docs/stack_queue_animal_shelter/Stack-Queue-Animal-Shelter.jpg)

-[Code Challenge 13](/docs/stack_queue_brackets/stacks-queues-brackets.jpg)

-[Code Challenge 15 Binary Tree](/data_structures/binary_tree.py)

-[Code Challenge 15 Binary Search Tree](/data_structures/binary_search_tree.py)

-[Code Challenge 16 Tree Max](/docs/tree_max/Binary_Tree_Max_Value.jpg)

-[Code Challenge 17 Breadth First](/docs/tree_breadth_first/Tree_Breadth_First.jpg)

-[Code Challenge 18 Fizz Buzz Tree](/docs/tree_fizz_buzz/tree-fizz-buzz.jpg)

-[Code Challenge 30 Hashtable Implementation](/data_structures/hashtable.py)

-[Code Challenge 31 Hashable Repeated Word](docs/hashtable_repeated_word/hashmap_repeated_word_whiteboard.jpg)

-[Code Challenge 32 Tree Intersection](docs/tree_intersection/tree_intersection_whiteboard.jpg)

-[Code Challenge 33 Two Arrays](docs/hashtable_left_join/two_arrays_whiteboard.jpg)

-[Code Challenge 34 Graph Implementation](data_structures/graph.py)

-[Code Challenge 36 DSA Practice](docs/three_odds/three_odds_whiteboard.jpg)

-[Lab 36 part 1](docs/computational_thinking/lab_36_whiteboard_1.jpg)

-[Lab 36 part 2](docs/computational_thinking/lab_36_whiteboard_2.jpg)

-[Code Challenge 37 Peak Index](docs/peak_index/peak_index_in_a_mountain_list_whiteboard.jpg)

-[Code Challenge 38 Construct a BST](docs/construct_BST/construct_BST_whiteboard.jpg)


### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`

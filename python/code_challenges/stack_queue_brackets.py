from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    bracket_mapping = {
        "(":")",
        "{": "}",
        "[":"]"
    }

    for x in string:
        if x in bracket_mapping:
            stack.push(x)
        elif stack.is_empty():
            return False
        elif bracket_mapping[stack.pop()] != x:
            return False

    return True



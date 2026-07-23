'''
Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.

Brackets can be any of the three types: (), [], and {}.
The input will always have a single deepest group.
For example, given "(hello (world))", return "world".
'''

def get_deepest_brackets(s):

    prefix_stack =[]
    bracket_stack = []
    current = ""
    max_depth = 0
    deepest_content = ""

    for ch in s:
        if ch in '([{':
            prefix_stack.append(current)
            bracket_stack.append(ch)
            current = ""
        elif ch in ')]}':
            depth = len(prefix_stack)
            if depth > max_depth:
                max_depth =  depth
                deepest_content = current
            prefix = prefix_stack.pop()
            left = bracket_stack.pop()
            current = prefix + left + current + ch

        else:
            current += ch
        print(current)
    print(deepest_content)
    s = deepest_content
    return s

t = get_deepest_brackets("(hello (world))")
print(t)
'''
Frontmatter Parser
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.

Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:

---
title: My Post
draft: false
views: 100
---
Should return:

{
  title: "My Post",
  draft: false,
  views: 100
}
Numbers, Booleans, and Strings should all be returned as their respective type.
The given string will have new lines separated with the newline character ("\n"). The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".
'''


def parse_frontmatter(s):
    lines = s.strip().split('\n')
    print(lines)

    if lines and lines[0].strip() == '---':
        lines = lines[1:]
    print(lines)

    if lines and lines[-1].strip() == '---':
        lines = lines[:-1]
    print(lines)

    result = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ': ' not in line:
            continue
        key, value_str = line.split(': ', 1)
        key = key.strip()
        value_str = value_str.strip()

        if value_str == 'true':
            value = True
        elif value_str == 'false':
            value = False
        elif value_str.isdigit():
            value = int(value_str)
        else:
            try:
                value = float(value_str)
                if value.is_integer():
                    value = int(value)
            except ValueError:
                value = value_str

        result[key] = value

    print(result)
    s = result

    return s


t = parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---")
print(t)

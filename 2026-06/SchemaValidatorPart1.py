'''
Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string
}
Extra keys are allowed
'''


def is_valid_schema(obj):
    if not isinstance(obj, dict):
        return False
    result = "username" in obj and isinstance(obj["username"], str)
    obj = result

    return obj


t = is_valid_schema({"username": "bob"})
print(t)

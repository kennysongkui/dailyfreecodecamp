'''
Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string,
  posts: number,
  verified: boolean
}
Extra keys are allowed

'''


def is_valid_schema(obj):
    if not isinstance(obj, dict):
        return False
    bool_username = "username" in obj and isinstance(obj["username"], str)
    bool_posts = "posts" in obj and isinstance(obj["posts"], int)
    bool_ver = "verified" in obj and isinstance(obj["verified"], bool)

    if bool_username and bool_posts and bool_ver:
        return True
    else:
        return False

    return obj


t = is_valid_schema({"username": "alice", "posts": 10, "verified": False})
print(t)

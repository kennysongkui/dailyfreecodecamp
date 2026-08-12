'''
Schema Validator Part 5
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
The brackets [] after string means that badges should be an array of strings (or empty).
Extra keys are allowed

'''


def is_valid_schema(obj):
    roles = ("user", "creator", "moderator", "staff", "admin")
    # role = obj["role"]

    if not isinstance(obj, dict):
        return False

    if "username" not in obj or not isinstance(obj["username"], str):
        return False

    if "posts" not in obj:
        return False

    posts_val = obj["posts"]
    if not isinstance(posts_val, (int, float)) or isinstance(posts_val, bool):
        return False

    if "verified" not in obj or not isinstance(obj["verified"], bool):
        return False

    if "role" not in obj or not isinstance(obj["role"], str):
        return False

    if obj["role"] not in roles:
        return False

    if "badges" not in obj:
        return False
    badges_val = obj["badges"]
    if not isinstance(badges_val, list):
        return False

    for item in badges_val:
        if not isinstance(item, str):
            return False

    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    obj = True

    return obj


t = is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False,
                     "badges": ["early-adopter", "popular"]})
print(t)

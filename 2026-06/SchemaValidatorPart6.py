'''
Schema Validator Part 6
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
Extra keys are allowed

'''


def is_valid_schema(obj):
    if not isinstance(obj, dict):
        return False

    if "users" not in obj:
        return False

    users_val = obj["users"]
    if not isinstance(users_val, list):
        return False

    for user in users_val:
        if not validate_user_profile(user):
            return False

    obj = True
    return obj


def validate_user_profile(user):
    roles = ("user", "creator", "moderator", "staff", "admin")
    # role = obj["role"]

    if not isinstance(user, dict):
        return False

    if "username" not in user or not isinstance(user["username"], str):
        return False

    if "posts" not in user:
        return False

    posts_val = user["posts"]
    if not isinstance(posts_val, (int, float)) or isinstance(posts_val, bool):
        return False

    if "verified" not in user or not isinstance(user["verified"], bool):
        return False

    if "role" not in user or not isinstance(user["role"], str):
        return False

    if user["role"] not in roles:
        return False

    if "badges" not in user:
        return False
    badges_val = user["badges"]
    if not isinstance(badges_val, list):
        return False

    for item in badges_val:
        if not isinstance(item, str):
            return False

    if "supporter" in user and not isinstance(user["supporter"], bool):
        return False

    return True


t = is_valid_schema({"users": [
    {"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]},
    {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20,
     "badges": ["helper"]}]})
print(t)

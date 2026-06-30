'''
Browser History
Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

"URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
"Back" - moves to the previous page in history, or stays on the current page if there isn't one.
"Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0].
'''


def get_browser_history(commands):
    history = []
    current = -1

    for cmd in commands:
        if cmd == "Back":
            if current > 0:
                current -= 1
        elif cmd == "Forward":
            if current < len(history) - 1:
                current += 1
        else:
            if current < len(history) - 1:
                history = history[:current + 1]
            history.append(cmd)
            current = len(history) - 1
    result = [history, current]
    print(result)

    commands = result
    return commands


t = get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"])
print(t)

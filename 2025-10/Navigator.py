'''
Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
'''

def navigate(commands):
    history = []
    forward_stack = []
    current_page = "Home"

    for command in commands:
        if command.startswith("Visit"):
            page_name = command[6:]

            history.append(current_page)
            forward_stack.clear()
            current_page = page_name
        elif command == "Back":
            if history:
                forward_stack.append(current_page)
                current_page = history.pop()
        elif command == "Forward":
            if forward_stack:
                history.append(current_page)
                current_page = forward_stack.pop()

    commands = current_page

    return commands

t = navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"])
print(t)
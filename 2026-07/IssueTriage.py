'''
Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

If the last message is less than 7 days ago, return "leave it"
If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
Otherwise, return "bump it"

'''

def triage_issue(ms, message):

    day = ((ms/1000)/3600)/24
    print(day)

    if day < 7:
        return "leave it"
    else:
        if "bump" in message.lower():
            return "close it"
        else:
            return "bump it"
    return ms

t = triage_issue(86400000, "Lets fix it")
print(t)
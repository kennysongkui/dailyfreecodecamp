'''
Issue Triage 2
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:

"bug" and "needs triage" if the title contains "error" or "bug"
"enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:

"needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
"discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:

"security", add a "critical" label
'''


def triage_issue(title, labels):
    result = labels.copy() if labels else []
    title_lower = title.lower()

    if not result:
        if "error" in title_lower or "bug" in title_lower:
            result.extend(["bug", "needs triage"])
        elif "feature" in title_lower or "add" in title_lower:
            result.extend(["enhancement", "discussing"])

    else:

        if "needs triage" in result and ("simple" in title_lower or "easy" in title_lower):
            result.remove("needs triage")
            if "good first issue " not in result:
                result.append("good first issue")

        elif "discussing" in result and ("planned" in title_lower or "next" in title_lower):
            result.remove("discussing")
            if "on the roadmap" not in result:
                result.append("on the roadmap")

        else:
            removed = False
            if "needs triage" in result:
                result.remove("needs triage")
                removed = True
            if "discussing" in result:
                result.remove("discussing")
                removed = True
            if removed and "help wanted" not in result:
                result.append("help wanted")

    if "security" in title_lower and "critical" not in result:
        result.append("critical")

    print(result)
    title = result
    return title


t = triage_issue("app crashes with error", [])
print(t)

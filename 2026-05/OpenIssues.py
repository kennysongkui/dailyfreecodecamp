'''
Open Issues
Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain open after all PRs have been merged.

A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or 312.
A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with all the same number can't get closed.
Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201). Similarily, issue 201 would be closed by PR 12.
Return the remaining open issues in the order they were given.
'''


def get_open_issues(issues, prs):
    # prs_list = list(str(prs))
    # print(prs_list)

    def is_closed(issue, pr):
        if issue == pr:
            return False
        s1 = str(issue)
        s2 = str(pr)
        L = max(len(s1), len(s2))
        s1 = s1.zfill(L)
        s2 = s2.zfill(L)
        print(s1, s2)
        for i in range(L):
            if s1[i:] + s1[:i] == s2:
                print(s1[i:], s1[:i])
                return True
        return False

    open_list = []
    for issue in issues:
        closed = False
        for pr in prs:
            if is_closed(issue, pr):
                closed = True
                break
        if not closed:
            open_list.append(issue)

    result = open_list
    print(result)
    issues = result
    return issues


t = get_open_issues([123, 234], [231])
print(t)

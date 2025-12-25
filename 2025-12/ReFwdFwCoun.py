'''
Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers.


'''

def email_chain_count(subject):

    case_list = ['fw', 'fwd', 're']
    new_arr = subject.split(":")
    result = 0
    for i in new_arr:
        i = i.lstrip()
        i = i.lower()
        if i in case_list:
            result += 1

    print(new_arr)
    print(result)
    subject = result
    return subject

t = email_chain_count("Re: Meeting Notes")
print(t)

t1 = email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary")
print(t1)
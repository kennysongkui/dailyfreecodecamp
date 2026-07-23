'''
Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.

Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
All given times will be in "HH:MM" (24-hour) format.
Use the following medication schedule:

Name	Schedule
Deployxitrin	08:00, 16:00
Debuggamanizole	07:00, 13:00, 21:00
Mergeflictamine	every 4 hours
Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".
'''


def medication_reminder(medications, current_time):
    print(medications)
    print(current_time)

    cur = parse_time(current_time)
    best_name = None
    best_wait = float('inf')
    print(cur)
    for name, last in medications:
        last_min = parse_time(last)

        if name == "Deployxitrin":
            times = [8 * 60, 16 * 60]
            next_due = None
            for t in times:
                if t > last_min:
                    next_due = t
                    break
            if next_due is None:
                next_due = times[0] + 24 * 60
            while next_due < cur:
                next_due += 24 * 60
            print(f"str1+{next_due}")

        elif name == "Debuggamanizole":
            times = [7 * 60, 13 * 60, 21 * 60]
            next_due = None
            for t in times:
                if t > last_min:
                    next_due = t
                    break
            if next_due is None:
                next_due = times[0]
            while next_due < cur:
                next_due += 24 * 60

            print(f"str2+{next_due}")
        elif name == "Mergeflictamine":
            interval = 4 * 60
            next_due = last_min + interval
            while next_due < cur:
                next_due += interval
            print(f"str3+{next_due}")
        else:
            continue

        wait = next_due - cur
        if wait < best_wait:
            best_wait = wait
            best_name = name
    print(name)
    result = f"{best_name} in {format_delta(best_wait)}"

    print(result)
    medications = result

    return medications


def parse_time(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m


def format_delta(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h}h {m}m"


# t = medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "07:00"], ["Mergeflictamine", "10:00"]],
#                         "11:00")
# print(t)

t1 = medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "21:00"], ["Mergeflictamine", "03:00"]], "06:55")
print(t1)
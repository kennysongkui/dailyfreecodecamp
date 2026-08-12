'''
Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.

Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".

Compatibility rules:

"AB" can receive from any blood type.
"A" can receive from "A" and "O".
"B" can receive from "B" and "O".
"O" can only receive from "O".
Duplicate entries in the given arrays represent quantity.
'''


def triage_blood(bank, patients):
    inv = {'O': 0, 'A': 0, 'B': 0, 'AB': 0}
    req = {'O': 0, 'A': 0, 'B': 0, 'AB': 0}

    for b in bank:
        inv[b] += 1
    for b in patients:
        req[b] += 1

    total_patients = sum(req.values())
    print(total_patients)
    served = 0

    take = min(inv['O'], req['O'])
    served += take
    inv['O'] -= take
    req['O'] -= take

    take = min(inv['A'], req['A'])
    served += take
    inv['A'] -= take
    req['A'] -= take
    take = min(inv['O'], req['A'])
    served += take
    inv['O'] -= take
    req['A'] -= take

    take = min(inv['B'], req['B'])
    served += take
    inv['B'] -= take
    req['B'] -= take
    take = min(inv['O'], req['B'])
    served += take
    inv['O'] -= take
    req['B'] -= take

    take = min(inv['AB'], req['AB'])
    served += take
    inv['AB'] -= take
    req['AB'] -= take

    take = min(inv['A'], req['AB'])
    served += take
    inv['A'] -= take
    req['AB'] -= take

    take = min(inv['B'], req['AB'])
    served += take
    inv['B'] -= take
    req['AB'] -= take

    take = min(inv['O'], req['AB'])
    served += take
    inv['O'] -= take
    req['AB'] -= take

    result = f"{served} of {total_patients} patients served"
    print(result)
    bank = result
    return bank


t = triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"])
print(t)

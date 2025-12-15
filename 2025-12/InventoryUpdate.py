'''
Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].
'''

def update_inventory(inventory, shipment):

    new_dict={}
    for i in range(len(inventory)):
        # new_list = list(new_dict.keys())
        # print(type(new_list))
        # print(new_list)
        # print(inventory[i][1])
        print(inventory[i][1])
        if inventory[i][1] in new_dict:
            new_dict[inventory[i][1]] += inventory[i][0]
        else:
            new_dict[inventory[i][1]] = inventory[i][0]
    for j in range(len(shipment)):
        if shipment[j][1] in new_dict.keys():
            new_dict[shipment[j][1]] += shipment[j][0]
        else:
            new_dict[shipment[j][1]] = shipment[j][0]

    new_arr = []

    for x in new_dict.items():
        item, quantity = x
        new_arr. append([quantity, item])
    print(new_dict)
    print(new_arr)
    inventory = new_arr[:]
    return inventory

# t = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]])
# print(t)

t1 = update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]])
print(t1)
def addToInventory(inventory, addedItems):
    # inventory is a dictionary
    for i in addedItems:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] = inventory[i] + 1

    return inventory


def displayInventory(stuff):
    item_total = 0
    print("Inventories :")
    for key, val in stuff.items():
        print(str(val) + "->" + key)
        item_total += val

    print('Total items = ' + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby', 'ruby', 'dagger', 'dagger']

inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)

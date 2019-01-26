inventory = {
    'rope':1,
    'torch':6,
    'gold coin':42,
    'dagger':1,
    'arrow':12
}

def displayInventory(stuff):
    item_total = 0
    print("Inventories :")
    for key, val in stuff.items():
        print( str(val) +"->"+ key)
        item_total += val

    print('Total items = '+ str(item_total))

displayInventory(inventory)

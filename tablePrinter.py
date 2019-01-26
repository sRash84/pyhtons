tableData = [
    ['apples','oranges','cherries','banana'],
    [ 'Alice','Bob','Carol','David'],
    ['dogs','cats','moose','goose']
]

def printTable(data):
    colwidths = [0]*len(data)

    for j in colwidths:
        colwidths = max(data[j], key=len)

    y = len(colwidths)

    for i in range(len(data[0])):
        for td in range(len(data)):
            print(data[td][i].rjust(y), end='')
        print()



printTable(tableData)

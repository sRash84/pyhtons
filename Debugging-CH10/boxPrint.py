def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height-2):
        print(symbol+(" " *(width-2))+ symbol)
    print(symbol * width)


for symbol, width, height in (('&',10,5),("@",15,15),("@",3,3),('x', 1, 3),('ZZ', 3, 3),('Z', 3, 1)):
    try:
        boxPrint(symbol,width,height)
    except Exception as err:
        print('An exception happened: '+str(err))
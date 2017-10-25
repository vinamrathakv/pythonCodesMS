#convert binary to hexadecimal

def binaryToHex(binaryValue):
    binary = str(binaryValue)
    length = len(binary)
    
    for i in range(4 - (length % 4)):
        binary = "0" + binary
    print(binary)
    
    binList = []
    
    while len(binary) != 0:
        
        binList.append(binary[:4])
        print(binList)
        binary = binary[4:]
        print(binary)
    print(binList)
    
    hexChar = ''
    hexList = []
    for i in binList:
        hexValue = int(i[0]) * 8 + int(i[1]) * 4 + int(i[2]) * 2 + int(i[3])*1
        print(hexValue)
        if hexValue > 9:
            hexChar = chr(hexValue -10 + ord('A'))
        else:
            hexChar = str(hexValue)
        hexList.append(hexChar)
        
    hex = ''.join(hexList)
    print(hex)

    
    
binaryToHex(101111)
        
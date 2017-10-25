#Recursive function binary to decimal

def binaryToDecimal(bstring):
    if not bstring:
        return 0
    return binaryToDecimal(bstring[:-1]) * 2 + (bstring[-1] == '1')

print(binaryToDecimal('001011'))
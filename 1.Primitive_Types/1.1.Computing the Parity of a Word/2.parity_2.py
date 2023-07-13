def parity(x: int):
    result = 0
    while x:
        print("value of the number: ", x)
        print("binary value of the number: ", bin(x))
        result ^= 1
        print("result: ", result)
        #x &= x - 1 # drops the lowest set bit of x
        #print("value of x: ", x)
        print("value after droping the bit: ", bin(x))
        print("-----------------------------------")
    return result
    
par = parity(13)
print(par)
def parity(x: int):
    result = 0
    while x:
        print("value of number x: ", x)
        print("binary value of the number: ", bin(x))
        result ^= x & 1
        print("after AND operation: ", result)
        x >>= 1
        print("after right shifting the bit: ", x)
        print("result: ", result)
        print("----------------------------------")
    return result

par = parity(13)
print(par)
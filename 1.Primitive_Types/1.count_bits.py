def count_bits(x: int):
    num_bits = 0

    while x:
        print("Value of x: ", x)
        print("Binary value of x: ", bin(x))
        num_bits += x & 1
        print("After Binary AND operation: ", x & 1)
        x >>= 1
        print("Bits after right shift: ", bin(x))
        print("After right shift: ", x)
    return num_bits
    
bits = count_bits(12)
print(bits)
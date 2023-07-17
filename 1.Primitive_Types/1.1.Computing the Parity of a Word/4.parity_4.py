def parity(x: int):
    print("value of the integer: ", bin(x))
    x ^= x >> 32
    print("right shift by 32: ", bin(x))
    x ^= x >> 16
    print("right shift by 16: ", bin(x))
    x ^= x >> 8
    print("right shift by 8: ", bin(x))
    x ^= x >> 4
    print("right shift by 4: ", bin(x))
    x ^= x >> 2
    print("right shift by 2: ", bin(x))
    x ^= x >> 1
    print("right shift by 1: ", bin(x))
    return x & 0x1

par = parity(12)
print(par)

y = 12
print(bin(y))
print(bin(y >> 3))

print(bin(0x1))
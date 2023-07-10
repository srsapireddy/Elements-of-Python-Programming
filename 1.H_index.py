def h_index(citations: list[int]):
    print("original array", citations)
    citations.sort()
    print("sorted array: ", citations)
    
    n = len(citations)
    print("length of array: ", n)
    
    for index, value in enumerate(citations):
        print("index, value: ", index, value)
        
        if (value >= n - index):
            return n - index
    return 0
    
h_index = h_index([100,78,62,32,18,3,2,1,1])
print("h_index value: ", h_index)
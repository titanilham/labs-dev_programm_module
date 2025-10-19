def task1(a):
    summ = 0
    count = 0
    for i, item in enumerate(a):
        if item[i] >= 0:
            summ += item[i]
            count += 1
    return f"{summ}, {count}" 

b = [
    [13, 90, 0],
    [0, 2, 3],
    [323, 23, -1],
    [-1, -12, -213213, 32, -21]
]

def task2(b):
    for i in b:
        minimum_element = i.index(min(i))
        first_element = i[0]
        i[0] = min(i)
        i[minimum_element] = first_element
        
        maximum_element = i.index(max(i))
        last_element = i[-1]
        i[-1] = max(i)
        i[maximum_element] = last_element 
                
    return b

if __name__ == "__main__":
    print(task2(b))
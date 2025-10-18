from array import array

def task1():
    arr = array("i", [])
    n = input(": ")
    
    try:
        for i in n.split(", "):
            arr.append(int(i))
    except (ValueError, OverflowError):
       return "ValueError: Можно вводить только 32-битные целые числа через запятую!"
   
    return f"{max(arr)}\n{arr[::-1]}"

def task2():
    arr = array("d", [])
    n = input(": ")
    
    try:
        for i in n.split(", "):
            arr.append(float(i))
    except (ValueError, OverflowError):
        return "ValueError: Можно вводить только 64-битные целые числа через запятую!"
    
    average = sum(arr) / len(arr)
    print(average)
    
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = average
            
    return arr

if __name__ == "__main__":
   print(task2())
    





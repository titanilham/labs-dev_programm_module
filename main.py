def task1(a):
    summ = 0
    count = 0
    for i, item in enumerate(a):
        if item[i] >= 0:
            summ += item[i]
            count += 1
    return f"{summ}, {count}"

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, -1]]

if __name__ == "__main__":
    print(task1(a))
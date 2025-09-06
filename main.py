def task1(string: str) -> int:  # длина строки
    return len(string)
    

def task2(number: int) -> bool:  # положительное ли число 
    if number > 0:
        return False
    return True

def task3(string: str)-> str:  # последний символ строки
    return string[-1]

def task4(number: int)-> bool:  # четное ли число
    if number % 2 == 0:
        return True
    return False

def task5(string1: str, string2: str) -> bool:  # проверить что первые буквы 2 слов совпадают
    if string1[0] == string2[0]:
        return True
    return False

def task6(string: str) -> str:
    """
    получить последнию букву слова, 
    если заканчивается на мягкий знак то предпоследнию букву
    """

    if string[-1] != 'ь':
        return string[-1]
    return string[-2]

def task7(number: int) -> int:  # первая цифра числа
    return int(str(number)[0])
    
def task8(number: int) -> int: 
    return int(str(number)[-1])  # поседняя цифра числа

def task9(number: int) -> int:  # сумму первой и последней цифры числа
    return int(str(number)[0]) + int(str(number)[-1])

def task10(number: int) -> int:  # количество цифр числа 
    return len(str(number))

def task11(number1: int, number2: int) -> bool:  # совпадают ли первые цифры 2 чисел
    if str(number1)[0] == str(number2)[0]:
        return True
    return False

def task12(array: list) -> list: # получить первые 3 элемента списка
    return array[0:3]

def task13() -> None:  # от 1 до 100, 
    numbers = ''
    for i in range(1, 101):
        numbers = numbers + str(i) + ' '
    return numbers

def task14() -> None:  #  от -100 до 0
    numbers = ''
    for i in range(-100, 1):
        numbers = numbers + str(i) + ' '
    return numbers

def task15() -> None:  # от 100 до 1
    numbers = ''
    for i in range(100, -1, -1):
        numbers = numbers + str(i) + ' '
    return numbers

def task16(array: list) -> int:  # сумма элементов списка
    return sum(array)

def task17(array: list) -> int:  # сумма квадратов списка
    array2 = []
    for i in array:
        array2.append(i**2)
    return sum(array2)

def task18(array: list) -> int:  # сумма элементов квадратных корней
    array2 = []
    for i in array:
        array2.append(i**0.5)
    return int(sum(array2))

def task19(string: str) -> list:  # получить список букв строки
    array = []
    for i in string:
        array.append(i)
    return array

def task20(array: list) -> int:  # сумма положительных элементов списка
    array2 = []
    for i in array:
        if i > 0:
            array2.append(i)
    return sum(array2)


if __name__ == '__main__':
    try: 
        print(task18([25, 100]))
    except TypeError as e:
        print(f"Error{e}")
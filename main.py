from math import pi
from array import array

class Task1:
    """Класс для вычисления площади разных геометрических фигур."""
    
    @classmethod
    def triangle(cls, h, b):
        return 1/2*h*b
    
    @classmethod
    def circumference(cls, r):
        return pi * r**2
    
    @classmethod
    def parallelogram(cls, b, h):
        return b * h
    
    @classmethod
    def rectangle(cls, a, b):
        return a * b
class Task2:
    @classmethod
    def task2(cls, arr1, arr2, arr3):
        if len(arr1) > 15 or len(arr2) > 15 or len(arr3) > 15:
            raise ValueError("Размер каждого массива не должен превышать 15")

        arr1 = array("l", arr1)
        arr2 = array("l", arr2)
        arr3 = array("l", arr3)
        
        average_arr1 = sum(arr1) / len(arr1)
        average_arr2 = sum(arr2) / len(arr2)
        average_arr3 = sum(arr3) / len(arr3)
        
        return f"""sum arr1: {sum(arr1)}, average arr1: {average_arr1}
    sum arr2: {sum(arr2)}, average arr2: {average_arr2}
    sum arr3: {sum(arr3)}, average arr3: {average_arr3}"""

if __name__ == "__main__":
    print(Task2.task2([1, 2], [3, 2], [1, 2, 3, 4]))



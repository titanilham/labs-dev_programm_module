class Main:
    """Лабораторная работа 3"""
    def __init__(self, price):
        self.price = price
    
    def task1(self):
        prices = []
        for i in range(1, 11):
            prices.append(i * (self))
        return prices    

    def task2(self):
        counter = 0
        summ = 0
        while len(self) != counter:
            summ += self[counter]
            counter +=1
        return f"a: {summ}\nb: {counter}"        


if __name__ == "__main__":
    print(Main.task2([1, 2, 3, 4])) 


"""
https://uproger.com/20-prakticheskih-zadanij-s-rekursiej-v-python-python-praktika/
"""
"""
1) Факториал
Напишите рекурсивную функцию factorial(n), которая будет принимать 
положительное целое число n и возвращать факториал от этого 
числа (1 x 2 x 3 x … x n).

ПРИМЕР!!!
factorial(1)   # 1
factorial(2)   # 2
factorial(3)   # 6
factorial(4)   # 24
factorial(5)   # 120
factorial(6)   # 720
factorial(7)   # 5040
factorial(8)   # 40320
"""
if __name__ == "__main__":
    def factorial(n: int) -> int:
        print(n)
        res = 1
        while n > 1:
            res = res * factorial(n - 1)
        return res
        print(res)



print("sadfa")   # 40320


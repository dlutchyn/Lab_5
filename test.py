class First:
    def __init__(self, x):
        self.x = x

    def alpha(self):
        return self.x - 100/self.x
    
    def beta(self):
        return 10**self.x

    def __str__(self):
        return str(self.x + self.alpha())


first = First(5)
print(first)


class Demo:
    def __init__(self):
        # self.a = 1
        # self.__b = 1
        pass

    # def get(self):
    #     return self.__b
    def test(self):
        print(__name__)

obj = Demo()
obj.test()
# obj.a = 45
# print(obj.a)


# class Test:
#     def __init__(self):
#         self.x = 0


# class Der_Test(Test):
#     def __init__(self):
#         self.y = 1
    

# b = Der_Test()
# print(b.x, b.y)
print(str(-2))


class A:
    def __init__(self, x=1):
        self.x = x

    def count(self):
        self.x = self.x + 1


class der(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y
    
    # def count(self):
    #     self.y += 1
    

obj = der()
# obj.count()
print(obj.x, obj.y)


# class A:
#     pass


# class B(A):
#     pass

# obj = B()

# print(isinstance(obj, A))

class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        self.time = '6:30'
        print(time)


# clock = Clock('7:30')
# clock.print_time()


class Demo:
    def __init__(self):
        __a = 1
        self.__b = 1
        self.__c__ = 1
        __d__= 1


# a = Demo()
# # print(__a)
# # print(a.__b)
# print(a.__c__)
# print(__d__)



class A:
    def test(self):
        print("A")

class B(A):
    def test(self):
        print("B")
        super().test()
    
o = B()
print(o.test())
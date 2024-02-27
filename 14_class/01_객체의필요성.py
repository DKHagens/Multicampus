#객체의 필요성

변수와 함수를 함께

#더하기 기능을 위한 계산기 구현


#3 + 4 + 5 + 9

class AddCal:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result
# result1 = 0
# def adder1(num):
#     global result1
#     result1 +=num
#     return result1
# result2 = 0
# def adder2(num):
#     global result2
#     result2 +=num
#     return result2
#
# print(adder1(3))
# print(adder1(7))
# print(adder1(9))
#
# print(adder2(3))
# print(adder2(7))
# print(adder2(9))

class AddCal:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result

myadder = AddCal()
myadder.adder(10)
print(myadder.result)
myadder.adder(20)
print(myadder.result)
myadder.adder(30)
print(myadder.result)
youradd = AddCal()
youradd.adder(100)
print(youradd.result)
print(type(myadder))




# 정적매서드(static method)
#: 인스턴스를 통하지 않고 클래스에서 바로 호출해서 사용하는 매서드

# 매서드 위에 @staticmethod 키워드를 지정하여 정의

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def sub(a, b):
        print(a - b)

myCal = Calc()
myCal.add(10,20)
Calc.add(10,20)

#함수처럼 쓸 수 있음
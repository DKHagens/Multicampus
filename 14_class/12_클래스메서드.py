# 클래스 매서드(class method)
# - 인스턴스를 통하지 않고 클래스에서 바로 호출
# - @classmethod를 지정하여 사용

class Person:
    count = 0 # 클래스 변수

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls): # cls : 클래스 의미
        print(f'{cls.count}명 태어났어요')

    @classmethod
    def create(cls): #생성자와 같은 메서드
        p = cls()  #Person()
        return p

kim = Person()
Person.print_count()

choi = Person()
Person.print_count()

#클래스 전체와 관련된 메소드를 부를 때 사용
#클래스 자체에 바로 접근해서 사용. 특히 클래스 내에서 클래스 변수에 접근할 때 편리

lee = Person.create() #클래스 매서드로 인스턴스 생성
Person.print_count()
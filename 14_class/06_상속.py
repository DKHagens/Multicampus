# 상속 : 부모 클래스로부터 상속받은 필드와 메소드를 이용하거나 추가 변경하여 활용(재사용
# 매서드 재정의


class Car(object):
    def __init__(self, speed = 0, color=''):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}로 주행한다')

class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color) #기존에 있는 것 부터 먼저 적기
        self.load = load

    #메서드 재정의
    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행한다')

    def loading(self):
        print(f'최대 {self.laod}양의 짐을 운반할 수 있는 트력')

car1 = Car()
truck1 = Truck(0,'blue',5)
truck2 = Truck(0,'white',10)
truck3 = Truck(0,'blue',5)
for car in [car1, truck1, truck2, truck3]:
    car.drive()
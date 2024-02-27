# 예제. Dog 클래스

class Dog:
    dog_id=0 #class 변수. class 내에서 전역변수처럼 작용
    def __init__(self, name, breed, size, age, Color):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.color = Color
        Dog.dog_id += Dog.dog_id+1
    def eat(self,food):
        print(f'{self.name}이 {food}를 먹는다')

    def sleep(self):
        print(f'{self.name}이 잠잔다')
    def sit(self):
        print(f'{self.name}이 앉아있다')
    def run(self):
        print(f'{self.name}이 뛴다')
    #def __repr__(self):
    #    return f'{self.name}은 품종: {self.breed}, 나이: {self.age}'

Dog1 = Dog('삐삐', 'Maltese', 'small', 2, 'white')
print(Dog1.dog_id)

Dog2 = Dog('벤', 'Chow Chow', 'medium', 3, 'brown')
print(Dog2.dog_id)

Dog3 = Dog('뭉치', 'Mastiff', 'large', 5, 'black')
print(Dog3.dog_id)


print(f'name = {Dog1.name},'
      f'\nbreed = {Dog1.breed},'
      f'\nsize = {Dog1.size},'
      f'\nage = {Dog1.age},'
      f'\ncolor = {Dog1.color}')
print(f'name = {Dog2.name},'
      f'\nbreed = {Dog2.breed},'
      f'\nsize = {Dog2.size},'
      f'\nage = {Dog2.age},'
      f'\ncolor = {Dog2.color}')
print(f'name = {Dog3.name},'
      f'\nbreed = {Dog3.breed},'
      f'\nsize = {Dog3.size},'
      f'\nage = {Dog3.age},'
      f'\ncolor = {Dog3.color}')

# 인스턴스 변수: 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역 변수와 같이 클래스들의 모든 인스턴스들이 공유하는 변수
# 클레스 이름, 빌드 이믊으로 메서드 내부에서 사용하고
# 인스턴스이름.클래스변수명으로 사용
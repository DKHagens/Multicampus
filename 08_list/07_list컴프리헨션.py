#리스트 컴프리헨션

#새로운 리스트 = [문장 for in range () [if 조건식]]


num_list = []
for num in range(1,6):
    num_list.append(num)
print(num_list)

num_list = [num for num in range(1,6)]
print(num_list)

num_list2 = [num*2 for num in range(1,6)]
print(num_list2)

num_list3 = [num*num for num in range(1,6)]
print(num_list3)

# 문제. 1~20의 정수 중 짝수만으로 구성 된 리스트 생성
even = [num for num in range(2,21,2)]
print(even)

even = [num*2 for num in range(1,11)]
print(even)

even = [num for num in range(1,21) if num %2 ==0]
print(even)

num_list4 = [num for num in range(1,21) if num %3 ==0]
print(num_list3)

list1 = [1,2,3,4,10,11,12]
num_list5 = [num for num in list1 if num %3 == 0]
print(num_list5)

#참고. zip()함수. zip 값은 여러 값을 순차적으로 받는다는 개념

foods = ['떡볶이', '짜장면', '라면', '피자']
sides = ['단무지','김치','피클']

#zip = 각각 변수에 담아줌 zip는 tuple. 동시에 여러 값을 담는다? #strict = True는 반드시 갯수가 맞아야. 기본값은 False
for food, side in zip(foods, sides, strict=True):
    print(food, '--', side)

for item in zip(foods, sides):
    print(item)
print(type(zip(foods, sides)),zip(foods, sides))
print(list(zip(foods, sides)))

name = ['홍길동','강감찬','성춘향','방자']
sex = ['남','남','여','남']
addr = ['서울','한양','독도','부산']

print(list(zip(name,sex,addr)))
print(zip(name,sex,addr))


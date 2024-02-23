#재귀함수(recursive function)
#함수 내부에서 자신의 함수를 다시 호출

#1~n 까지의 합 재귀함수

def my_sum(n):
    if n == 1:
        return 1
    return n+my_sum(n-1)

print(my_sum(10))

# . 1*2*...*n : n! 계산하는 재귀함수

def my_fact1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(my_fact1(5))

def my_fact2(n):
    if n <= 1:
        return 1
    return n * my_fact2(n-1)

print(my_fact2(5))

#내부함수

def outFunc(x,y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc(10,30))

#람다(lambda) 함수
#한 줄짜리 함수, return문을 사용하지 않음
# 변수명 = lambda<인수들>:<반환할 식>
# 람다 함수는 함수 참조를 반환
#변수로 람자 함수라는 객체가 됨
#람다함수도 디폴트 매개 변수 사용 가능
f = lambda:1
print(f())

add = lambda x,y=30:x+y
print(add(2,5))

add = lambda x=10,y=30:x+y
print(add())
print(add(20))
print(add(10,50))
print(add(y=100,x=300))

#람다 표현식 : 함수 이름 명명하지 않고 바로 호출
# (lambda <매개 변수들>:식)(인수들)
print((lambda x : x+10)(10)) #진짜 이름 없는 함수

#람다표현식 안에서는 변수 생성 불가 :SyntaxError
#(lambda x: y=10 ; x+y)(10)

#람다표현식 바깥에서 정의된 변수를 람다 표현식 안에서 사용
y=10
(lambda x:x+y)(10)
(lambda x,y,z : x+y)(10,20,30)

def plus_ten(x):
    return x+10

# [1,2,3,4,5] + 10
new = []
for n in [1,2,3,4,5]:
    new.append(n+10)
print(new)

lambda x:x+10
#map(fuct, 데이터들) 함수에 집합적 데이터를 순차적으로 집어넣음. 반환은 map이라는 type

print(list(map(lambda x:x+10, [1,2,3,4,5])))

print('lambda사용')
print(list(map(plus_ten,  [1,2,3,4,5])))

def add_list(x,y):
    new_list = []
    for i in range(min(len(x),len(y))):
        new_list.append(x[i]+y[i])
    return new_list

a=[1,2,3,4]
b = [10,11,12,13]
print(add_list(a,b))

#map(func, iterable_data) 함수
def add_two(x,y):
    return x+y

print(list(map(add_two,a,b)))
print(list(map(lambda x,y: x+y, a,b)))

print(min(1,2))
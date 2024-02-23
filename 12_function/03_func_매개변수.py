# 함수의 매개변수(parameter)와 인수(인자: argument)
# 매개변수 : 함수를 정의할 때 함수로 전달되는 값을 갖는 변수 (함수정의)
# 인수 : 함수를 호출할 때 전달하는 값

def get_area(width,height):
    result = width * height
    print(f'사각형 가로={width}, 세로 = {height}, 면적은 {result}')
    return result

get_area(10,20)

# 문제. 삭칙연산을 수행하는 함수 정의
#add(a,b): 두 수 더하기
#sub(a,b) : 두 수 빼기
#mul(a,b) : 두 수 곱하기
#div(a,b) : 두 수 나누기

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print('0으로 나눌 수 없음')
    else:
        return a/b

a=2
b=3
print(f'{a}+{b}={add(a,b)}')
print(f'{a}-{b}={sub(a,b)}')
print(f'{a}*{b}={mul(a,b)}')
print(f'{a}/{b}={div(a,b):.2f}')

#2. 디폴트 매개변수
#매개변수의 기본값이 지정되어 있는 경우
#

def greet(name, msg='hello'):
    print(name + ','+msg)

greet('홍길동','hi')
#안넣으면 error가 msg -> msg='hello'로 기본값 설정
#반드시 디폴트 매개변수는 뒤쪽으로!
#print(hi, end='')도 예시임

#3. 위치 매개변수(positional parameter)
#매개변수의 위치가 실 인수로 전달받을 때 동일한 위치의 변수에 저장됨

#함수에 여러개 자료(리스트, 딕셔너리) 전달 가능
def show_names(names):
    for name in names:
        print(name,end= ' ')

show_names(['홍길동','심청이','강감찬'])
print()

def show_info(info):
    print(info)
    for key,value in info.items():
        print(key, value)

info = {'이름':'홍길동','나이':20}
show_info(info)

# 5. 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러개의 값을 전달받을 때 사용
# *args : tuple **kwargs=> key=value

print('hi','ho', end=' ')
print()

def my_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(my_sum(1,2))
print(my_sum(1))
print(my_sum(1,2,3))
print((my_sum(1,3,4,5,6)))

# 2) **kwargs 매개변수

def show_info(**kwargs):
    for key in kwargs.keys():
        print(key, end = ' ')
    print()
    for value in kwargs.values():
        print(value, end = ' ')
    print()
    for item in kwargs.items():
        print(item, end = ' ')

show_info(id='abc')
show_info(id='abcd',name='hong')
show_info(id='abcd',name='hong',age=30)

#6. 키워드 인수(keyword arguments)
#직접 집어 넣으면 순서 바꿔도 상관 없음
def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40)
my_print(a=5, c=10, b=30)

def show_info2(id,name,age=20):
    print(id)
    print(name)
    print(age)

show_info2(name='hong',id=20)

# *args(가변길이 인수이자 위치 인수)는 **kwargs(가변길이 인수, 키워드 인수) 앞에 반드시 와야함
#위치 인수는 키워드 인수 앞에 적기!
def my_func(*args, **kwargs):
    pass

#def my_func(**kwargs, *args): 안됨!

my_func(1,2,3, a=10, b=3)
#my_func(1, a=10, 2,3, b=3)이런 식으로는 못씀!

#함수 호출: 위치 인수와 키워드 인수를 함께 사용하는 경우 키워드 인수가 위치 인수 뒤로
#함수 정의: 위치매개변수, 디폴트매개변수 순
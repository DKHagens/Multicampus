# 지역변수(local variable)와 전역변수(global variable)
# 지역변수 : 함수 내부에서 정의된 변수, 함수 안에서만 사용 가능
#       함수 호출 시 생성, 종료시 소멸해 더 이상 사용 불가

a= 10

def show_info(name):
    age = 10
    print(name,age)

show_info('age')
#print(age)
#print(name)

def show1():
    a=1 #지역변수
    a=a+1
    print(f'a:{a}',id(a))

#전역변수와 같은걸 define할 때는 지역 변수가 우선
'''
def show2():
    a=a+1 #지역변수를 못찾음 : 오류 발생. 전역변수와 같은걸 define할 때는 전역변수로 못받아옴. 지역 변수 우선
    print(f'a:{a}',id(a))
'''
def show3():
    b=a+1 #전역 변수를 찾아옴
    print(f'b:{b}',id(b))


def show4():
    global a #전역 변수를 받아오는게 아니고 전역 변수라고 선언하는 것
    a = a+1
    print(f'지역변수 a: {a}', id(a))

show1()
#show2()
show3()
show4()

print(f'전역변수 a: {a}', id(a))

#range나 dictionary와 list등 변경 가능한 집합적 자료는 변수를 shallow copy해 전역마냥 취급됨
def show_list(my_list):
    cpy_list = my_list.copy()
    cpy_list[-1] = 100
    print(cpy_list, id(cpy_list))

my_list = [1,2,3,4]
show_list(my_list)
print(my_list, id(my_list))

def sub():
    global b
    global z
    a=7
    z=7

sub()
print(z)
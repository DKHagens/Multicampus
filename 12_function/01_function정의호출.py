#함수
#재사용/자주 사용하는 기능들을 위한 코드 집합
#경제적, 관리 용이
#내장함수(built-in function) / 사용자정의함수
#https://docs.python.org/3.12/library/functions.html

#함수 정의 및 호출
#예. 이름, 나이, 연락처 출력하는 함수 show_info()

def show_info():
    print('이름 : 홍길동')
    print('나이 : 20')
    print('연락처 : 010-111-1111')

def show_info1():
    #나이, 이름, 연락처 입력
    name = input('이름 입력: ')
    age = input('나이 입력: ')
    phone = input('연락처 입력: ')
    print('이름 :', name)
    print('나이 :', age)
    print('연락처 :', phone)


show_info()
show_info1()

#문제. 두 정수를 입력받아 더하고 그 결과를 출력하는 함수 add() 정의하기
def add():
    int1 = int(input('첫 번째 정수 입력: '))
    int2 = int(input('두 번째 정수 입력: '))
    print('두 숫자의 합은',int1 + int2, '입니다')

result = add()
print(result)

#반환값이 있는 함수 정의
def add2():
    int1 = int(input('첫 번째 정수 입력: '))
    int2 = int(input('두 번째 정수 입력: '))
    result = int1 + int2
    print('두 숫자의 합은',int1 + int2, '입니다')
    return result

print(f'return value = {add2()}')
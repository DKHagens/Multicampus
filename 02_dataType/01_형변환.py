#Day2
#1. 자료형(Data Type)

# 기본자료형 : 정수, 실수, 부울(bool), 문자열(str)
# iterative / 집합적 자료/ sequence : 리스트, 딕셔너리, 튜플, 세트

# 2진수, 8진수, 16진수, 10진수
# bin(), oct(), hex()

print('bin(123)=', bin(123))
print('bin(0o123)=', bin(0o123))
print('bin(0x123)=', bin(0x123))

print('oct(123)=', oct(123))
print('oct(0b11010111)=', oct(0b11010111))
print('oct(0x123)=', oct(0x123))

print('hex(123)=', hex(123))
print('hex(0b11010111)=', hex(0b11010111))
print('hex(0o123)=', hex(0o123))

# 변수의 자료형 : 실행할 때 결정(동적타이핑)
# id(), type()

# 2) 형변환
# int(string), float(string), str(number)
# int(string, base=10) -> 10진수가 기본
# int(string, 2), int(string, 8), int(string, 16)

print('int("123")=', int('123'))
print('int("1010",2)=', int('1010',2))
print('int("ff",16)=', int('ff',16))
print('int("123",8)=', int('123',8))

#print("int('ff'))=", int('ff'))
#에러 : NameError, TypeError, ValueError(자릿수등이 안맞음)

print('float(\'13.5\')=', float('13.5'))
print('float(\'13\')=', float('13'))

#str(숫자) : 문자열 변환
#print('나이는 = %d' %'20') #TypeError
print('나이는 = %d' %int('20'))
#print('나이는 = ' + 20) #TypeError
print('나이는 = ' + str(20))

#input() 함수 : 키보드로 입력받아서 문자열로 반환
name = input('이름은: ')
year = int(input('출생연도는: '))
print(f' 이름은 {name}, 나이는 {2024-(year)}')

#연산자 : str의 +: 두 문자열을 연결
#연산자 : str의 *: 문자열을 숫자만큼 생성해서 연
'''num = input('실수입력: ')
result = num * 10
print(f' {num}*10 = {result}')'''

num = input('실수입력: ')
result = int(num) * 10
print(f' {num}*10 = {result}')

# SW => data + algorithm

#문제1: 두 개의 정수를 입력받고 합계 출력하기
int1 = int(input('첫 번째 정수를 입력하시오: '))
int2 = int(input('두 번째 정수를 입력하시오: '))
print(f'두 숫자의 합은 {int1 + int2}')

#문제2. 몸무게와 키 값을 입력받아서 BMI 지수 계산

wgh = float(input('당신의 BMI는? \n몸무게(kg)를 입력하세요: '))
hgt = float(input('키(cm)을 입력하세요: '))/100
BMI = wgh/(hgt*hgt)

print(f'당신의 BMI는 {BMI:.2f}입니다')


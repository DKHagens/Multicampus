#Day1: 변수에 대해서 실습

#실습1: 두 변수의 값을 교환(Swap)
'''
a = 10
b = 5
print(a, b)

c=a
a=b
b=c
print(a, b)
'''

#방법2 : 파이썬 방식

a,b = 10,5
print('a=', a, 'b=',b)
a,b = b,a
print('a=',a,'b=',b)

#실습2: 변수 삭제
#del a
#print(a)

#실습3: 변수의 값 출력 print()
age = 30
name = 'HongGilDong'
print(name, age)

addr = '서울시 서초구'
result = name + "은 " + addr + '에 살아요'
print(result)

print(name + ": 나이는 " + str(age) + '입니다.')
# TypeError : 문자열과 숫자는 연결할 수 없다
# 숫자를 문자열로 변환하는 함수 활용 : str(숫자)

#실습4 : 변수를 이용한 계산 결과값 출력
#삼각형의 넓이 계산

w = 10
h = 5

s= w*h/2
print('넓이는 ' + str(s) + '입니다')

# print() 함수의 다양한 출력
# print('문자열', 변수)

#포맷 서식
#방법1: '서식'% 값
# 대표적 format string : %f(실수), %d(정수), %s(문자), %c, %x, %o(8진수), %%(%를 %로 출력시킴)
#%a.b  앞 부분 = 전체 자릿수, 뒷부분 소수점 자릿수
print('넓이=%d'% s)

result = '%s은 %s에 살고 나이는 %d에요' %(name, addr, age)
result2 = '넓이=%.2f' %s
pcnt = 10.5
result3 = '전체면적의 %.3f%%입니다' % pcnt

print(result)
print(result2)
print(result3)

#방법2: format() 함수
#format(숫자, '숫자서식')

result4 = format(s, '.2f')
print(result4)
print(format(100, '5d'))

#연습문제
#다음의 변수 값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기

#총점: 245, 평균: 81.67

kor = 90
eng = 80
math = 75

summ = kor + eng + math
aver = summ/3

print('총점: ' + str(summ) + ', 평균: ' + format(aver, '.2f'))

# 방법3: .'{0:서식}{1:서식}{2:서식}'.format( , , ) 함수
print(format(3.141592, '10.3f'))
print('{0:.3f}'.format(3.1415927))
print('{0:5d} {2:05d} {1:.3f}'.format(kor,math,eng))

#방법4 : f'string -> 3.6버전 부터 제공
print(f' 수학점수는  {math:05d}이고, 국어 점수는 {kor:.3f}, 영어점수는 {eng}이다.')
result5 = f' 수학점수는  {math:05d}이고, 국어 점수는 {kor:.3f}, 영어점수는 {eng}이다.'
print(result5)

balance = 10300.0
print(balance)
print(int(balance))
print(format(int(balance), ','))

#print()함수의 매개변수 활용
print('국어',kor, '수학',math, '영어',eng, end='  ')
print('국어',kor, '수학',math, '영어',eng, sep='*')
print('국어',kor, '수학',math, '영어',eng)

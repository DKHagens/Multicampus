# 연산자
#1. 산술연산자 : +, -, *, /, %, //, **
#divmod(x,y) : x를 y로 나는 몫과 나머지ㅣ 반환

#문제. 10000초는 몇분 몇초인가?
time = 10000
hours = time // 3600
minutes = (time % 3600)//60
seconds = time % 60
print(f'{time}는 {hours}시간 {minutes}분 {seconds}초입니다.')

# 2. 관계 연산자 : > < >= <= == !=
a = 100
b = 5
#result = a == b
print(f'{a}=={b}의 결과는 {a==b}')
print(f'{a}!=={b}의 결과는 {a!=b}')
print(f'{a}>{b}의 결과는 {a>b}')

#3. 논리 연산자 : and or not
print( a>10 and a<300)
print(not(a>200))

#4. 비트 연산자: & | ^ ~ << >>
print(f'~a:{~a}')
print(f'{b}<<1 : {b<<1}')
print(f'{b}<<3 : {b<<3}')
print(f'{b}>>1 : {b>>1}')
print(f'{b}>>2 : {b>>2}')
print(f'{a}>>3 : {a>>3}')

# 대입연산자 : += -= *= /= //= %=
print(f'a={a}, do a+=10')
a+=10
print(f'a={a}')

#실습문제1. 지폐교환기
# 777777원을 지폐로 교환해서 나타내기

money = int(input('지폐로 교환할 돈은 얼마? '))
print(f'50000원짜리 ==> {money // 50000}장')
money %= 50000
print(f'10000원짜리 ==> {money // 10000}장')
money %= 10000
print(f'5000원짜리 ==> {money // 5000}장')
money %= 5000
print(f'1000원짜리 ==> {money // 1000}장')
money %= 1000
print(f'지폐로 바꾸지 못한 돈 ==> {money}원')

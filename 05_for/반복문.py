sumX = 0

for x in range(1,11):
    print(x)
    sumX += x

print('sum =', sumX)

#1부터 10사이의 홀수 더하기
sumX = 0

for x in range(1,11,2):
    sumX += x

print('sum =', sumX)

#값을 시작값, 끝값 입력받아 이 사이에 있는 정수 더하기
start = int(input('덧셈의 시작 값을 입력하시오: '))
end = int(input('덧셈의 끝 값을 입력하시오: '))
sumX=0
for x in range (start+1,end):
    sumX += x

print('숫자 사이의 합은 ', sumX)

#5명의 점수 입력받아 합격>=60, 불합격<60 출력
for _ in range(5):
    jumsu = int(input{'0~100사이 점수입력: '))
    if jumsu >= 60:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu} 불합격')

for num in range(1,101):
    print(num, end=' ')
print()

num = 1
while num <= 100:
    print(num, end=',')
    num += 1
print()
print()

# 1부터 100사이 3의 배수들의 합
total = 0
for num in range(3, 101, 3):
    total += num
print('1~100사이 3의 배수 합', total)

print()

total = 0
num = 3
while num <=100:
    total += num
    num += 3
print('1~100사이 3의 배수 합', total)

num = int(input('숫자 입력: '))
while num != 7:
    num = int(input('다시 입력: '))
print('7 입력! 종료')
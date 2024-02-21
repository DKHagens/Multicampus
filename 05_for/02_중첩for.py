# #다중 for 이용
# for y in range(3):
#     for x in range(4):
#         print(x+4*y+1, end=' ')
#     print()
#
# a=0
#
# for y in range(3):
#     for x in range(4):
#         a += 1
#         print(a, end=' ')
#     print()

#2~9단 구구단 출력
for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan}*{n:3d}={dan*n:<3}')
    print()

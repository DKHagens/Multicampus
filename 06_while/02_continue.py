# x = 0
#
# while x < 10:
#     x+=1
#     if x%2 == 0:
#         continue
#     print(x, end=',')
#
# print('\n----------------')
# x = 0
# while x < 10:
#     x+=1
#     if x%2 == 1:
#         continue
#     print(x, end=',')
#
# print('\n----------------')
# x = 0
# while x < 10:
#     x+=1
#     if x%2 == 0:
#         break
#     print(x, end=',')

neg = pos = zero = 0

for i in range (1,11):
    num = int(input(f'숫자 {i}입력 : '))
    if num < 0:
        neg += 1
    elif num > 0 :
        pos += 1
    elif num == 0:
        zero += 1

print('--------------------------')
print(f'양의 개수 :  {pos}')
print(f'음의 개수 :  {neg}')
print(f'0의 개수 :  {zero}')

neg = pos = zero = 0
i = 1
while i <= 10:
    num = int(input(f'숫자 {i}입력 : '))
    if num < 0:
        neg += 1
    elif num > 0 :
        pos += 1
    elif num == 0:
        zero += 1
    i += 1

print('--------------------------')
print(f'양의 개수 :  {pos}')
print(f'음의 개수 :  {neg}')
print(f'0의 개수 :  {zero}')
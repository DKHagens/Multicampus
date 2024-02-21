# 1) 리스트의 한 값을 삭제

a=[1,10,30,40]
print(f'삭제 전 alist: {a}')
a[1:3] = []
print(f'삭제 후 alist: {a}')
b = [1, 20, 30, 40]
print(f'삭제 전 blist: {b}')
b[1:2] = []
print(f'삭제 후 blist: {b}')

#2) 리스트 자체를 삭제
a.append(50)
b.append(5)
print(f'삭제 전 alist: {a}')
a=[]
print(f'삭제 후 alist: {a}')
print(f'삭제 전 blist: {b}')
b=None
print(f'삭제 후 blist: {b}')

c = ['apple','coconut','melon','hotdog']
print(f'삭제 전 clist: {c}')
del(c) #메모리에서 제거
print(f'삭제 후 clist: {c}')
#name error 발생
#1. append() : 리스트 맨 뒤에 항목을 추가

a = []
a.append('apple')
a.append('hotdog')
a.append(10)
print(f'alist {a}')

#2. pop([index=-1]): 리스트의 맨 마지막 요소를 추출하고 요소를 제거
value = a.pop()
print(f'alist : pop 적용 후 {a}, value={value}')
a.append('melon')
print(f'a.append("melon")')
print(f'alist : a.pop(2)={a.pop(2)}, pop 적용 후 {a}' )

#3. sort() : 리스트의 요소들을 정렬하여 정렬한 리스트로 변경
b = [6,3,5,1,-3]
print(f'blist: {b}')
b.sort()
print(f'sort적용 후 {b}')

#3.1 sort(key=str.lower) 대문자도 소문자마냥 취급
char = ['b','B','A','a','z']
char.sort()
print(f'charlist: sort()적용 후 {char}')
char.sort(key=str.lower)
print(f'charlist: sort(key=str.lower)적용 후 {char}')
char.sort(key=str.lower, reverse=True)
print(f'charlist: sort(key=str.lower, reverse=True)적용 후 {char}')
#문자열은 첫 문자로 정렬

#4. reverse(): 리스트를 역순으로 변경
b.reverse()
print(f'reverse 적용 후 {b}')
a.reverse()
print(f'reverse 적용 후 {a}')

#5. index() : 리스트에서 지정한 값이 위치를 반환
c = ['홍길동','강감찬','성춘향','변학도','강감찬']
idx = c.index('강감찬')
print(f'강감찬의 위치는 {idx}')
#idx = c.index('원빈')
#print(f'{idx}')

#6. insert(): 리스트에 값 삽입
print(f'insert 전 {c}')
c. insert(-1, '원빈')
print(f'insert 후 {c}')
c. insert(2, '피카소')
print(f'insert 후 {c}')

#7. remove(값): 리스트에서 지정한 값을 제거, 첫 번째 값만 제거
#8. count(값): 리스트에서 지정한 값의 개수 반환
print(f'c.remove("강감찬") 전 {c}')
#c.remove('강감찬')
for item in range(c.count('강감찬')):
    c.remove('강감찬')
    print(f'강감찬 삭제 후 {c}')

print(f'c.remove("강감찬") 후 {c}')

#9. extend(): 리스트에 리스트를 추가(확장) => 하나의 리스트로 변경/병합, 리스트안 리스트 x
print(f'blist {b}')
b.extend([10,11,12])
print(f'b.extend([10,11,12]) 적용 후 blist {b}')
new_b = list(b)
#insert, append와 차이
b.append([10,11,12])
print(f'b.append([10,11,12]) 적용 후 blist {b}')
b.insert(3,[10,11,12])
print(f'b.insert(3, [10,11,12]) 적용 후 blist {b}')
#b.extend(100) 값 하나면 error
#print(f'extend(100) 적용 후 blist {b}')

#10 sorted([],reverse=False) 내장 함수 : 리스트를 정렬한 새로운 리스트 반환, 원본 리스트를 건드리지 않고 생성
print(f'new_blist {new_b}')
renewal_b = sorted(new_b, reverse=True)
print(f'sorted() 함수 적용 후 new_blist {new_b}')
print(f'sorted()로 생성된 {renewal_b}')

#11. copy() : 리스트 복사 당연하지만 원본 안 건드림
cpy_b = new_b
print(cpy_b)
cpy_b.sort()
print(cpy_b)

#12. clear() : 리스트 비우기
#cpy_b.clear() #cpy_b[:] = [] 동일한 기능
#print(cpy_b)

#13. del() : 리스트 요소 지우기, 리스트 전체 지우기

del(cpy_b[3:])
#dep cpy_b
print(cpy_b)
#del cpy_b
#print(cpy_b)

#14. len() : 리스트의 길이
print(len(b))
print(b)

#15. max() : 최대값을 반환하는 내장함수
#16. min() : 최소값을 반환하는 내장함수
ex_list = [100,7,-2,99,30]
ex_list = ['hello','Exit','Zoo','hI']
ex_list = ['hello','Exit','Zoo','홍길동','춘향','방자',\
           'hI','100','7'] #숫자를 작은 값으로 따짐

print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')

#17. in, not in 연산자 True나 False 값으로 반환함

num = [1,2,3,4,5]
result = 1 in num
print(result)
result = 10 not in num
print(result)

#18. > < >= <= == != : 리스트 일치 검사
list1 = [1,2,3]
list2 = [5,6,7]
list3 = [1,2,3]

print(list1 < list2)
print('----')
print(list1 == list3)
print('---')
print(list1 > list3)

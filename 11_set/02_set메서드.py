# 메서드
s= {10,1,3,4}
print(s)

# add()메서드 : 집합에 요소 추가
s.add(100)
print(s)

#update()
s.update([5,6])
print(s)

#2 데이터 삭제, 추출
# pop() 일단 앞에 것 지움

result = s.pop()
print(result)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

s.update([10,11,12,13,14])
print(s)

#remove
s.remove(10)
print(s)
#s.remove(15) #삭제하려는 값이 없는 경우 keyError

#discard() 얘는 없으면 그냥 None로 반환
s.discard(6)
print(s)
s.discard(16)
print(s)

# clear()
s.clear()
print(s)

#연산
s1={1,2,3}
s2={3,4,5}

# 합집합 : union() , |
print(s1.union(s2))
print(s1 | s2)

# 교집합 : intersection(), &
print(s1.intersection(s2))
print(s1 & s2)

# 차집합 : difference(), -
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
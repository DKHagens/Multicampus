#복수계 자료 치환 튜플 내 자료 수정이 아니고 변수를 받는 것이기에 가능

a,b = 1, 2
print(a,b,type(a),type(b))

a,b = b,a
print(a,b)

(a,b), (c,d) = (10,11),(12,13)
print(a,b,c,d)

# 패킹(packing)
t = 1,2, 'hello'
print(t)

#언패킹(unpacking) 변수앞 * 는 값을 여러개 받는(보통 list)라는 뜻
x,y,z = t
print(type(t))
print(x,y,z,type(x),type(y),type(z))

t2= (1,2,3,4,5)
a, *b = t2
print(a,b,type(a),type(b))
t2= (1,2,3,4,5)
a, b,*c = t2
print(a,b,c,type(a),type(b),type(c))
*a, b, c = t2
print(a,b,c,type(a),type(b),type(c))
#*a, *b, c = t2 배분 여러 개에 알아서 못함 -> 걍 문법적으로 못함
#print(a,b,c,type(a),type(b),type(c))


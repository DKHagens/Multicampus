#set

#1. 순서 x: 입력되는 순서와 출력 순서는 다를 수 있음
#2. 동일 값 사용 불가
#3. 인덱스 사용 불가
#4. 요소 추가/삭제 가능
#5. 변경 가능한 항목은 세트의 요소가 될 수 없다
# 리스트는 세트 요소로 올 수 없다
# 튜플은 포함 가능
#6. 넣으면 다 들어는 가지만 변형시킴

#키만 모아놓은 딕셔너리의 특수한 형태
#세트(집합) 생성: {}, set()

#세트 생성
s1 = {1,2,3,4,5,1,2,4}
print(s1, type(s1))

s2 = set([10,8,11,20,30,10])
print(s2)

s3 = set((10,2,300))
print(s3)

s4 = set({'one':1, 'two':2})
print(s4)

#s1[0] 인덱스 못씀
#TypeError: 'set' object is not subscriptable

#리스트는 세트에 못옴
#s5 = {1,2,[4,3]}
#TypeError: unhashable type: 'list'

s5 = {1,2,(4,5)}
print(s5)

#hashable type => hasing
#객체를 식별할 수 있는 코드를 부여하여 테이블에 저장:(키,값)
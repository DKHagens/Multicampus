#1. get() 메서드

d= {'one':1, 'two':2, 'three':3}
print(d)
print(f'd["two"]: {d["two"]}')

print(f'd.get("two") : {d["two"]}')

#print(d['four']) #KeyError 발생 : 없는키 접근
print(d.get('four'))#key가 없는 경우 None 반환
print(d.get('four',4))#key가 없는 경우 2번째 인수만 반환

#2. setdefault() 매서드 없으면 가져다 넣음
print(d)
print(d.setdefault('two'))
print(d.setdefault('two',4))
d.setdefault('four',4)
print(d)

#3 . pop(). popitem() 메서드
print(d.popitem())
key, value = d.popitem()
print(f'key={key}, value={value}')
print(d)

d['six']=6
d['ten']=10
print(d)

result = d.pop('two')
print(result)
print(d)

#reversed(d)?

d2 = d.copy()
print(d, id(d))
print(d2, id(d2))

#5.update() 키 값 추가
d3 = {'five' : 5, 'two': 2 , 'seven':7}
print(d3)
d3.update(d2)
print(d3)

#6. clear()
print(d)
d.clear()
print(d)

print(d2, id(d2))
d2 = {}
print(d2, id(d2))
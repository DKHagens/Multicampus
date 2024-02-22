#뷰(view)
d = {'one':1, 'two':2, 'three':3}

# keys() 뷰
keys = d.keys()
print(keys, type(keys))

print(list(keys))

#키들에 대한 값들을 출력
for key in d.keys():
    print(key,d[key])

values = d.values()
print(values, type(values),list(values))
print(len(values))

for value in d.values():
    print(value, end=',')
print()

#items() 뷰 tuple로 반환
items = d.items()
print(items, type(items))
print(list(items))

for item in d.items():
    print(item, type(item))

for key, item in d.items():
    print(key, item)
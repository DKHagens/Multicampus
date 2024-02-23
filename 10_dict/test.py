def create_dict(name, korean, math, english, science):
    return {'name': name, 'korean': korean, 'math': math, 'english': english, 'science': science}

student = [create_dict('홍길동', 87,98, 88, 95),
create_dict('이몽룡',92,98,96,98),
create_dict('성춘향',76,96,94,90),
create_dict('변학도',98,92,96,92),
create_dict('박지성',95,98,98,98),
create_dict('류현진',64,88,92,92)]

print('이름',' ','총점','평균')

for data in student:
    total = data["korean"]+data["math"]+data['english']+data['science']
    avrg = total / ((len(data.keys()))-1)
    print(data['name'],'', total, avrg)





dict = {}

while True:
    eng = input('영어 단어 등록 (종료는 quit) : ')
    if eng == 'quit':
        break
    #elif dict.get(eng) != None:
    elif eng in dict:
        print(f'{eng}는 이미 등록된 단어 입니다\n')
        continue
    mean = input(f"{eng}의 뜻입력 (종료는 quit) : ")
    if mean =='quit':
        break
    dict[eng] = mean
    print()
print()
while True:
    print()
    eng = input('검색할 단어 입력 (종료는 quit) : ')
    if eng == 'quit':
        break
    if dict.get(eng) == None:
        print(f'{eng}는 사전에 없는 단어입니다.')
        continue
    print(f'{eng}의 뜻은  {dict[eng]}입니다')
print()
print('종료합니다')
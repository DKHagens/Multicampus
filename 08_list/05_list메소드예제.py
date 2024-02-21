#1. 리스트 요소 추가 :append(), insert()
'''
name1 = input('회원 입력: ')
name2 = input('회원 입력: ')
name3 = input('회원 입력: ')
name = []
name.append(name1)
name.append(name2)
name.append(name3)
print(name)
'''
name_list = []

for i in range(3):
    name = input('회원 입력: ')
    name_list.append(name)

print(name_list)

#i=0
while True:
    name = input('회원 입력: ')
    if name == 'x':
        break
    else:
        name_list.append(name)

    #i+=1
print(name_list)



name_str = ''
for name in name_list:
    name_str += name + ', '
print(name_str)

#예제 6. 학생 5명 점수를 입력받아 리스트에 추가하고 총점과 평균 계산하고 출력

score_list = []
total = 0
for i in range(5):
    score = int(input(f'학생{i+1} 점수 입력 : '))
    score_list.append(score)

for score in score_list:
    total += score

average = total/len(score_list)

print(f'총점은 {total}, 평균은 {average:.2f}이다')

#예제 7. 예제 6에서 80점 이상의 학생수를 계산하고 출력
over_80 = 0
for score in score_list:
    if score >= 80:
        over_80+=1
print(f'80점 이상 학생 : {over_80}명')

#문제 3. 엔터키를 누를 때까지 상품명들을 리스트에 추가하고, 엔터키를 누르면 입력 종료되고 등록된 상품리스트 출력.

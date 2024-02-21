#2차원 리스트 : [행][열]

table = [[1,2,3,4],[7,8,9,10],[10,11,12,14]]
table2 = [[1,2,3,4],[7,8,10],[10,11,12,14]]
print(table2)
print(len(table2))
print(table2[0])

for item in table:
    print(item, type(item), len(item))

for row in table2:
    for col in row:
        print(col, end=' ')
    print()
#for 문 자체에서 각 행렬을 찾아서 가져오는 느낌

row_n = len(table2)
col_n = len(table2[0])
'''
for r in range(row_n):
    for c in range(col_n):
        print(table2[r][c], end=' ')
    print()
'''
#for 문에서 찾을 index를 찾고 list에 넣어서 긁어오는 느낌, 이건 열 길이가 동일하지가 않음
#가변 길이

#문제5. 학생별 과목별 점수와 총점, 평균 계산하고 출력 / 학생들의 국어, 영어, 수학 점수를 학생별 점수 리스트로 입력


score_list = [[90,85,70],[88,79,92],[100,100,100],[90,60,70]]

print('---성적표 (점수)---')
for score in score_list:
    print(score)

print('---성적표(점수,총점,평균)---')
for score in score_list:
    print(score, end=' , ')
    total = 0
    for row in score:
        total += row
    print(total, end=' , ')
    print(f'{total/len(score):.2f}')
    #or
    print('{0}, {1}, {2:.2f}'.format(score, total,total/len(score)))
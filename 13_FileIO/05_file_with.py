# with문 : close()가 자동을 수행
# with open(파일명, 모드) as 파일객체:
#   수행문장들

# with open('study_data2.txt', 'r') as f:
#     text = f.read()
#     print(text)
#
# with open('data/file1.txt', 'a', encoding='utf-8') as f2:
#     f2.write(text)

#한줄로 요약해서 이런식으로 더 많이 씀

#scores.txt : 탭으로 구분한 데이터파일
with open('data/scores.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    print(data)

#scores2.txt: ,으로 구분한 데이터 파일 -> csv같은 형태로 다루는 형식이 존재. 제일 많이 씅ㅁ
with open('data/scores2.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    print(data)

print(len(data))
# 텍스트 파일 읽기: read(), readline(), redalines(), seek(), 파일 깊게 찾기

# 텍스트 파일 생성: 메모장을 이용해서 생성
# study_data.txt

# 1단계: 파일열기(open)
#f = open('study_data.txt', mode = 'r' #객체 이름이 필요, 일반적으로는 f
f = open('data/study_data.txt', mode ='r', encoding ='utf=8') #한글은 인코딩이 안맞아서 인코딩 필요
# 오류 UnicodeDecodeError: 'cp949' codec 한글 인코딩 못함


#f = open('study_data3.txt', mode = 'r') #study_data3. txt: ANSI 코드로 저장됨
#ANSI 인코딩일시 별개의 인코딩 필요 없음
#정작 pycharm은 잘 못읽음

# 2단계: 파일 처리(읽기)
#text = f.read()
# text = f.readline()
# print(text)
# text2 = f.readline()
# print(text2)

# while True:
#     text = f.readline()
#     if not text: #읽을 내용이 없으면(마지막)
#         break
#     print(text)
# #print(f.readlines())

#print(f.readlines()) #2번은 못읽나? 움직이면서 읽는 것이기 때문에 2번은 당연히 못읽음
#readlines 써서 파일 읽기
for textline in f.readlines(): #readline과 동일한 결과
     print(textline, end = '') #없으면 enter키가 안됨


#3단계 : 파일닫기(close())
f.close()

#영문으로 된 텍스트 파일 읽기
# f1 = open('study_data2.txt', mode = 'r') #객체 이름이 필요, 일반적으로는 f
# text = f1.read()
# print(text)
# f1.close()

# seek() :
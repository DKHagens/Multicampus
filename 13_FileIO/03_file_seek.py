# seek(offset. whence) 함수

print('파일 내에서 검색 : seek() ----')
f = open('data/seek_test_data.txt', 'r', encoding='utf-8')

# f.seek(0,0) #시작위치: 0,0 : 파일 처음
# lines = f.readlines()
# print(lines)

f.seek(0,0) #시작위치: 7,0 : 파일 처음
lines = f.readlines()
print(lines)


f.seek(3,0) #시작위치: 7,0 : 파일 처음
lines = f.readline()
print(lines)


#f.seek(1,0)
f.seek(0,1) #시작위치: 7,0 : 파일 처음
lines = f.read()
print(lines)

f.seek(16,0) #시작위치: 7,0 : 파일 처음 #한글은 utf-8에서 3바이트를 차지해서 숫자가 안맞는 경우가 생김
lines = f.readlines()
print(lines)

f.seek(19,0) #시작위치: 7,0 : 파일 처음 #한글은 utf-8에서 3바이트를 차지해서 숫자가 안맞는 경우가 생김
lines = f.readlines()
print(lines)

f.close()
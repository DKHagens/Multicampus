#파일입출력 3단계

# 1단계: 파일 열기(open)
# 내장함수 open(파일경로, 모드=r)
# r, w, a, r+, w+, a+ : 텍스트파일
# rb, wb, ab, rb+, wb+, ab+: 이진파일(binary 파일)
# 파일객체 = open()

# 2단계: 파일처리 => 읽기 / 쓰기
# 파일객체.read()
# 파일객체.write()

# 3단계: 파일 닫기(close())
# 파일객체.close()
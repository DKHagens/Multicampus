# binary file : 이진파일
# - 글자(text)가 아닌 bit 단위로 의미가 부여되는 파일
# - 텍스트파일을 제외한 파일 : 그림파일, 음악파일, 동영상파일, 엑셀, 실행
# - 텍스트파일과 이진 파일 구분 : 메모장에서 파일열기 시 내용이 보이면 텍스트, 이상하게 보이면 이진 파일

inStr = ''
path1 = 'C:/Windows/notepad.exe' #드라이브부터 시작하면 절대경로임
path2 = 'data/notepad.exe'

inF = open(path1, 'rb')
outF = open(path2, 'wb')

while True:
    inStr = inF.read(1) #1바이트씩 읽기
    if not inStr:
        break
    outF.write(inStr)

inF.close()
outF.close()
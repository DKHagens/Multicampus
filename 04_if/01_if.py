#조건문

#if문

num= int(input('정수입력: '))
if num > 10:
    print('10보다 크네요')


#if~else

if num>10:
    print('10보다 크네요')
else:
    pass

#    print('10보다 작거나 같아요')


idn = input('아이디 입력 : ')
psw = input('비밀번호 입력 : ')

'''
if idn == 'flower' and psw == '1234':
    print('로그인 성공!')
else:
    print('로그인 실패!')
'''

if 'flower' == idn:
    if '1234' == psw:
        print('로그인 성공')
    else:
        print('비밀번호를 확인해주세요')
else:
    print('아이디를 확인해주세요')

#중첩 if : if 조건이 만족하는 경우 또다른 조건에 따라 실행
    # if 아래 if 존재

if 'flower' == idn:
    if '1234' == psw:
        print('로그인 성공')
    else:
        print('비밀번호를 확인해주세요')
else:
    if '1234' == psw:
        print('아이디를 확인해주세요')
    else:
        print('아이디와 비밀번호를 모두 확인해주세요')
        



#점수 입력(0~100)받아서 학점 출력
#90점 이상 A,
#80이상, 90미만 : B
#70이상, 80점 미만 : C
#60이상, 70점 미만 : D
#60미만 : F

score = int(input('당신의 점수는(0~100)? '))
if 100 >= score >= 90:
    print('A')
elif 90 >= score >= 80:
    print('B')
elif 80>= score >= 70:
    print('C')
elif 70>= score >= 60:
    print('D')
elif 0 <= score < 60:
    print('F')
else:
    print('잘못된 점수입니다')

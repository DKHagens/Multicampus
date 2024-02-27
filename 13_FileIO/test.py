#1

with open('data/s.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    data.sort()
    for i in data:
        print(i, end= '')

#2
path = 'yesterday.txt'
with open(path, 'r', encoding = 'utf-8') as f:
    voc = {}
    for data in f.readlines():
        data = data.strip()
        text_list = data.lower().split(' ')
        text_list = [x for x in text_list if x]
        for key in text_list:
            if key in voc:
                voc[key] += 1
            else:
                voc[key] = 1
    keys_list = sorted(voc.keys())
    voc_list = '[출력결과 : 단어별 빈도]\n'
    for keys in keys_list:
        voc_list += f"'{keys}': {voc[keys]}\n"
w = open('voc_list.txt', 'w', encoding='utf-8')
w.write(voc_list)
w.close()


#3
def add(path, name):
    with open(path,'r',encoding='utf-8') as f:
        rst = ''
        for data in f.readlines():
            a = int(data.split(' ')[0])
            b = int(data.split(' ')[1])
            rst += f"{a}+{b}={a+b:.1f}\n"
        w = open(name, 'w', encoding='utf-8')
        w.write(rst)
        w.close()

path = 'data/number.txt'
add(path, 'result.txt')

#4

def input_member(fname):
    name_str = ''
    while True:
        nam = input('멤버를 입력하세요.(종료는 q) : ')
        if nam == 'q':
            break
        else:
            name_str += nam + '\n'
    with open(fname, 'w', encoding='utf-8') as w:
        w.write(name_str)

def output_member(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        print(f.read())

start = input('저장 1, 출력 2, 종료 q : ')
while start != 'q':
    if start == '1':
        fname = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(fname)
        start = input('저장 1, 출력 2, 종료 q : ')
    if start == '2':
        fname = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(fname)
        start = input('저장 1, 출력 2, 종료 q : ')
    else:
        print('다시 입력해주세요.')
        start = input('저장 1, 출력 2, 종료 q : ')

name = 'mem.txt'
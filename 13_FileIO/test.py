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
    # for data in f.readlines():
    #     data = data.strip()
    #     text_list = data.lower().split(' ')
    #     text_list = [x for x in text_list if x]
    text_list = f.read().lower().split()
    print(text_list)
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
def my_sum(input_file, name):
    with open(input_file,'r') as f:
        rst = ''
        for data in f.readlines():
            a = int(data.split(' ')[0])
            b = int(data.split(' ')[1])
            rst += f"{a}+{b}={a+b:.1f}\n"
        with open(name, 'w') as w:
            w.write(rst)

input_file = 'data/number.txt'
my_sum(input_file, 'result.txt')

#4

def input_member(fname):
#이거 안받고 nam을 받는대로 쓰는 것도 방법
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


while True:
    start = input('저장 1, 출력 2, 종료 q : ')
    if start == '1':
        fname = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(fname)
    elif start == '2':
        fname = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(fname)
    elif start == 'q':
        break
    else:
        print('다시 입력해주세요.')

name = 'mem.txt'
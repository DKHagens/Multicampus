# 함수 반환문 return

def get_area():
    w = int(input('가로길이: '))
    h = int(input('세로길이: '))
    result = w*h
    print(f'사각형 가로={w},세로={h},면적은 {result}')
    return result

print(get_area())

def multi_return():
    return 1,2,3

value=multi_return()
print(value, type(value))
a,b,c = value
print(a,b,c)

def get_names():
    names = []
    for i in range(3):
        name = input('이름입력: ')
        names.append(name)
    return names

names = get_names()
print(names)

def get_info():
    name = input('이름입력: ')
    age = input('나이: ')
    info = {'name': name, 'age': age}
    return info

info = get_info()
print(info, type(info))
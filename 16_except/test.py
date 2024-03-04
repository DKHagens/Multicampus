def div(a,b):
    if b == 0:
        raise RuntimeError('0으로 나눌 수 없습니다')
    return a/b

div(1,0)
def toUpper(sentence):
    return sentence.upper()

print(toUpper('abcd'))

def pickup_even(alllist):
    even_list = []
    for i in alllist:
        if i % 2 ==0:
            even_list.append(i)
    return even_list

print(pickup_even([1,2,3,4,5,6,7,8,9]))

# 파이썬 객체를 파일에 저장(dump)하고 읽기(load)
#pickle은 파이썬전용 저장 형식? 느낌

#import pickle
from pickle import dump, load

data_list = [['구','전체','내국인','외국인'],
             ['관악구', 519864, 502089, 17775],
             ['강남구', 547602, 542498, 5014],
             ['송파구', 686181, 679247, 6934],
             ['강동구', 428547, 424235, 4312]]

path = 'data/dataList.pickle'

with open(path, 'wb') as f:
    dump(data_list, f) #가장 기본

with open(path, 'rb') as f:
    data_pickle = load(f)

for item in data_pickle:
    print(item)

data_pickle.append(['종로구', 321673, 300000, 21673])
print(data_pickle)
#csv(comma separated value)파일 읽기
#csv 모듈 임포트

import csv

# csv.reader()
#reader 모듈을 이용한 list 생성
path = 'data/scores2.csv'
with open(path,'r', encoding='utf-8') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

#csv.writer
#obj = csv.writer(csvfile)
#obj.writerows(데이터) : 데이터는 csv파일에 쓸 객체
data_list = [['구','전체','내국인','외국인'],
             ['관악구', 519864, 502089, 17775],
             ['강남구', 547602, 542498, 5014],
             ['송파구', 686181, 679247, 6934],
             ['강동구', 428547, 424235, 4312]]

print(data_list)
with open('data/pop.csv','w',encoding='utf-8', newline='') as f: #newline : 줄바꿈 한칸을 막기 위함
    obj = csv.writer(f,delimiter=',') #행과 ,로 구분
    obj.writerows(data_list)
#실전에선 여러 정의된 함수로 더 많이 씀

def writecsv(filename, datalist, encoding):
    with open(filename, 'w', encoding):
        obj = csv.writer(f, delimiter=',')
        obj.writerows(datalist)

writecsv('data/pop.csv',data_list,'utf-8')

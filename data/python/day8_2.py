'''  11.16 오후수업 '''
'''
    * CSV란? Comma Seperate Value => 콤마(,)로 데이터가 분리된 파일
    
     공공데이타포탈 (국가에서 제공 중인 데이터)
     https://www.data.go.kr/
'''
import os, csv
os.chdir('data')
print('population.csv' in os.listdir(), 'data.csv' in os.listdir())

f = open('data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
print(csv_data) # csv 객체 출력됨  <_csv.reader object at 0x00000177DA7A7400>

# csv의 각 레코드가 리스트로 출력됨
for item in csv_data:
    print(item)
print('-'*50)
f.close()

# 2차원 형태의 리스트 구조로 변환
f = open('data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
data_list = []
for item in csv_data:
    data_list.append(item)
f.close()
print(f'data_list => {data_list}\ndata_list 길이=> {len(data_list)}')

# 2차원 리스트 출력
for row in data_list:
    for col in row:
        print(col, end="\t")
    print()
    
# 'kor' 데이터만 정수형 리스트로 생성
korList = []
for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
print(korList, type(korList[0]))

# 'kor' 테이터의 총점과 평균, 최고점, 최하점 구하기
# 리스트의 모든 합계 sum(리스트명), 최소/최대 min,max(리스트명)
print(f'{"*"*30}\n총점 = {sum(korList)}\n평균 = {sum(korList)/len(korList)}\n'
      f'최소 = {min(korList)}\n최대 = {max(korList)}\n{"*"*30}')



# 국어 점수의 최고점을 받은 학생의 이름은?
# 값에 해당하는 인덱스번호를 출력하는 함수 => 리스트이름.index(값)
# 알고리즘
# 국어점수의 최고점
# 리스트이름.index(국어점수의 최고점 ) => 인덱스번호
# 리스트이름[인덱스번호][이름인덱스번호]
print('-'*50)
print(f'국어 최고점수 = {max(korList)}')
print(f'국어 최고점수에 해당하는 행인덱스 = {korList.index(max(korList))}')
print(f'국어 최고점수의 학생이름은? = {data_list[korList.index(max(korList))+1][1]}')


# 퀴즈1 :
# 4과목('kor', 'eng', 'mat', 'bio')의 총점 구하기
def sumList(n):
    sumList = []
    if n == '국어': n = 2
    elif n == '영어': n = 3
    elif n == '수학' : n = 4
    elif n == '과학' : n=5

    for i in range(1,len(data_list)):
        sumList.append(int(data_list[i][n]))
    return sumList
kor, eng, mat, bio = sum(sumList("국어")),sum(sumList("영어")),sum(sumList("수학")),sum(sumList("과학"))
print(f'kor+eng+mat+bio의 총점 => {kor+eng+mat+bio}')

# 퀴즈2 : 4과목의 전체 평균 구하기
print(f'4과목의 전체 평균 => {(kor+eng+mat+bio)/4}')
print(sumList("국어"))
print(f'각 과목의 평균 => 국어: {kor/len(list(sumList("국어")))}\t\t'
      f'영어: {eng/len(list(sumList("영어")))}\t\t'
      f'수학: {mat/len(list(sumList("수학")))}\t\t'
      f'과학: {bio/len(list(sumList("과학")))}\t\t')

# 퀴즈3 : 전체 총점이 가장 높은 학생의 이름은? (강사님 예제 참고)
personal_scoreList = []
for i in range(1,len(data_list)):
    personal_scoreList.append(int(data_list[i][2])+int(data_list[i][3])+int(data_list[i][4])+int(data_list[i][5]))
print(f'전체 총점이 가장 높은 학생의 이름 => {data_list[personal_scoreList.index(max(personal_scoreList))+1][1]}')


print()

'''
# 강사님 답
# 퀴즈1 : 4과목('kor', 'eng', 'mat', 'bio')의 총점 구하기

# 리스트 초기화
korList = []
engList = []
matList = []
bioList = []

for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
    engList.append(int(data_list[i][3]))
    matList.append(int(data_list[i][4]))
    bioList.append(int(data_list[i][5]))
print(f' kor 총점 = { sum(korList)}')
print(f' eng 총점 = { sum(engList)}')
print(f' mat 총점 = { sum(matList)}')
print(f' bio 총점 = { sum(bioList)}')

print(korList)


# 퀴즈2 : 4과목의 전체 평균 구하기
print(f' kor 평균 = { sum(korList)/len(korList)}')
print(f' eng 평균 = { sum(engList)/len(engList)}')
print(f' mat 평균 = { sum(matList)/len(matList)}')
print(f' bio 평균 = { sum(bioList)/len(bioList)}')

# 퀴즈3 : 전체 총점이 가장 높은 학생의 이름은?
# 각 학생 레코드의 총점 리스트 만들기
totalList = []

for i in range(1, len(data_list)):
    totalList.append(int(data_list[i][2])+int(data_list[i][3])+int(data_list[i][4])+int(data_list[i][5]))
print(totalList)
print(max(totalList))
print(totalList.index(max(totalList))) #가장 큰 값의 인덱스 위치 출력

# data_list의 인덱스 0값은 class,name,kor,eng,mat,bio와 같은 제목이라 totalList의 시작 인덱스 0값은
# data_list의 인덱스 1값을 시작으로 for문을 돌려 list를 완성시켰다. 따라서
# 전체 총점 가장 높은 학생의 이름이 위치한 인덱스 위치 값을 data_list에서 찾기 위해선 +1 해주어야 함
print(data_list[totalList.index(max(totalList))+1])
print('final=>\t',data_list[totalList.index(max(totalList))+1][1]) #2차리스트에서 이름이 위치한 인덱스 [i][1]
'''



# WITH문 이용해 CSV 파일 읽기
with open('population.csv', 'r', encoding='utf-8') as f:
    csv_data = csv.reader(f)
    
    # 2중 리스트 구조로 변경 후 5개만 출력
    data_list2 = []
    for item in csv_data:
        data_list2.append(item)
    print(data_list2[:5], len(data_list2))

    # 첫번째 값 제외시키기 (State, Population 첫행 제목부분)
    data_list2 = data_list2[1:]
    print(data_list2[:3]) #제외여부 확인
    
    # 인구와 관련된 데이터를 정수 리스트로 생성
    # 숫자 중간중간에 들어간 쉼표로 인해 나는 오류 해결방법 => 문자열변수.replace(old, new)
    test = '4,780,131'
    test = int(test.replace(',',''))
    print(test,type(test))

    population_list= []
    for i in range(len(data_list2)):
        temp = int(data_list2[i][1].replace(',',''))
        population_list.append(temp)
    print(population_list)

    #가장 많은 인구수
    print(f'가장 많은 인구 수 => {max(population_list)}')

    #가장 작은 인구수
    print(f'가장 많은 인구 수 => {min(population_list)}')

    print()
    #가장 인구가 많은 주(State), 가장 인구가 적은 주
    print(f'가장 인구가 많은 주(State)? {population_list.index(max(population_list))}') #가장 큰 인구수의 인덱스 위치 찾고
    print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))]}') #해당 인덱스값 이용해 원본 리스트값 출력
    print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))][0]}') #그 중 원하는 값 인덱싱으로 뽑기

    print()
    print(f'가장 인구가 적은 주(State)? {population_list.index(min(population_list))}')
    print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))]}')
    print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))][0]}')




# reader말고 DictReader로 읽어오면 딕셔너리 자료형
f = open('2017.csv','r',encoding='cp949')
csv_data = csv.DictReader(f)
#print(csv_data, type(csv_data))

#for item in csv_data:
#    print(item)

# 리스트안의 딕셔너리 구조로 변경
data_dict_list = []
for item in csv_data:
    data_dict_list.append(item)
print(data_dict_list)
f.close()

print(data_dict_list[0])

# 서울 데이터의 일반인 값은?
# 리스트명[인덱스값][키값]
print(data_dict_list[0]['일반인'])
print(data_dict_list[0]['어린이'])

# 제주 지역의 대중교통 중 사용자 수는?
# 1 _ 구분 리스트 생성
city_list = []
for i in range(len(data_dict_list)):
    city_list.append(data_dict_list[i]['구분'])
print(city_list)

# 2 _ '제주' 인덱스 값 (인덱스 넘버 출력)
print(city_list.index('제주'))

# 3 _'제주' 전체 데이터 출력
print(data_dict_list[city_list.index('제주')])

# 4 _ '제주' 대중교통 총 사용자수
temp = data_dict_list[city_list.index('제주')]
print(temp, type(temp))
print(int(temp['일반인']) + int(temp['어린이']) + int(temp['청소년']))

sum = 0
for key in temp:
    try:
        sum += int(temp[key])
    except:
        pass
print(sum)


# 각 지역이름을 입력하면 총 사용자수가 출력되게 함수 정의하기
def city_total(city, m):
    city_list = city
    temp = data_dict_list[city_list.index(m)]
    sum = 0
    for key in temp:
        try:
            sum += int(temp[key])
        except:
            pass
    print(f'{m} 지역의 총 사용자수 = {sum}')

city_total(city_list, '제주')
city_total(city_list, '서울')


# 퀴즈 - 각 지역별 대중교통총사용자수를 아래와 같은 딕셔너리 구조로
#  생성하여 출력하여라
# {'서울': 4006394, '부산': 952394,
# '대구': 547517, '인천': 716825,
# '광주': 242717, '대전': 262872,
# '울산': 152289, '세종': 22677,
# '경기': 2816335, '강원': 84879,
# '충북': 117371, '충남': 148303,
# '전북': 118447, '전남': 120123, '경북': 165815,
# '경남': 253772, '제주': 63008}


with open('data/traffic_2017.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    list_city = []
    list_user = []

    for row in csv_data:
        list_city.append(row['구분'])
        if row['기타'] == '':
            temp = '0'
        else:
            temp = row['기타']
        list_user.append(int(row['일반인'])+
                         int(row['어린이'])+
                         int(row['청소년'])+int(temp))

    # print(list_city)
    # print(list_user)
    korea_traffic_dict = {}
    for i in range(0, len(list_city)):
        # 딕셔너리변수[키] = 값
        korea_traffic_dict[list_city[i]] = list_user[i]
    print(korea_traffic_dict)
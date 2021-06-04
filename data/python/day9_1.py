'''  11.17(TUE) 오전수업 '''

'''
    지난 수업 복습
    * 파이썬에 외부 자료 이용하기
    - txt, csv, xml, json, html, webURL
'''
import os, csv
#os.chdir('data')


#2차원 리스트
#encoding = 'cp949'는 생략 가능
with open('data/2018.csv', 'r') as f:
    csv_data1 = csv.reader(f)
#    for item in csv_data1:
#        print(item)

    data_list1 = []
    for item in csv_data1:
        data_list1.append(item)
    print(data_list1)

    # 첫번째 리스트 제외
    data_list1 = data_list1[1:]
    print(data_list1, '\n',len(data_list1))

with open('data/2018.csv', 'r')as f:
    csv_data2 = csv.DictReader(f)

#    리스트화 방법 (1)
#    data_list2 = []
#    for item in csv_data2:
#        data_list2.append(item)

#   리스트화 방법 (2)  => list for문 (리스트 안에 있는 for문)
    data_list2 = [item for item in csv_data2]
    print(data_list2)


    # 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
    # 지역 필드를 리스트로 만들기

    city_list = [item['지역'] for item in data_list2]
    print(f'시티리스트 = {city_list}')

    # 1000명이상 필드를 리스트로 만들기
    employ1000_list = [int(item['1000명이상'].replace(',','')) for item in data_list2]
    print(f'1000명이상 필드 리스트 = {employ1000_list}, 정수형인지 확인 = {type(employ1000_list[0])}')

    # 1000명이상 필드에서 최대값
    print(f'1000명이상 필드에서의 최대값 => {max(employ1000_list)}')

    # 1000명이상 필드에서 최대값 갖는 인덱스 번호
    print(f'최대값 갖는 인덱스의 번호 => {employ1000_list.index(max(employ1000_list))}')

    # 1000명이상 회사에 들어간 취업자수가 가장 많은 도시
    print(f'1000명 이상 회사 중 취업자수 가장 많은 도시 => {city_list[employ1000_list.index(max(employ1000_list))]}')

    # 100인 미만 회사에 들어간 취업자수가 가장 적은 도시
    employ100_list = [int(item['51-100인미만'].replace(',', '')) +
                      int(item['6-50인미만'].replace(',', '')) +
                      int(item['1-5인미만'].replace(',', '')) for item in data_list2]
    print(f'100명 미만 회사의 취업자수가 가장 적은 도시 => {city_list[employ100_list.index(min(employ100_list))]}')


print()



'''
    * 정규표현식 (교재 p.291) => 유효성 검사, 특정 문자열이 특정 조건(패턴)에 맞는지 검사
    ex) 회원가입 시 주민번호가 맞는가?, 핸드폰번호 형식이 맞는가?
    
    - 정규표현식 모듈 (re)은 내장모듈 따라서, 파이썬 설치시 자동설치 됨
'''

# 파이썬의 정규표현식 모듈 
import re

# re객체의 속성과 메소드 확인
# dir(모듈명, 클래스명) : 지원되는 속성 및 함수의 목록을 리스트로 표시
print(dir(re))


'''
    * 방식1) 패턴변수 = re.compile(패턴식) / 패턴변수.정규표현식메소드(문자열)
    
    * 패턴식 메타문자
    - ^:문자열의 처음을 나타냄
    - $:문자열의 끝

# 문자열이 특정 글자로 시작하는가? - ^a, ^ca
# 문자열이 특정 글자로 끝나는가? - $y

    * 정규표현식메소드
    - match(문자열) : 문자열 처음부터 검색 => 문자열 / None
    - search(문자열) : 문자열 전체 검색 => 문자열 / None
    - findall(문자열) : 정규식과 매치되는 문자열을 리스트로 반환 
    - finditer(문자열) : 정규식과 매치되는 문자열을 반복가능한 객체(for문으로 개별결과 확인)로 반환

'''


pat1 = re.compile('^ab')
print(pat1, type(pat1)) # re.compile('^ab') <class 're.Pattern'>

# 결과값을 리스트로 반환
print(pat1.findall('above')) # ['ab']
print(pat1.findall('boy'))  # []

# Match Object / None 로 반환 / None
print(pat1.search('above')) # <re.Match object; span=(0, 2), match='ab'>
print(pat1.search('boy')) # None

# callable_iterator 집합형 객체로 반환
print(pat1.finditer('above'))
print(pat1.finditer('pineapple'))
for item in pat1.finditer('above'):
    print(item) # <re.Match object; span=(0, 2), match='ab'>

for item in pat1.finditer('pineapple'):
    print(item)

pat2 = re.compile('y$')
print(pat2.findall('fly')) # ['y']
print(pat2.finditer('doctor lovely fly suddenly'))
for item in pat2.finditer('doctor lovely fly suddenly'):
    print(item)


# 패턴에 맞는 문자열찾기
txt1 = "가나다 009 python ?### 7834 파이썬 java ava WORD cript 784 ENGLISH "
# 한글만 추출 => re.findall(패턴식, 문자열변수)
result = re.findall('[가-힣]', txt1)
print(result, type(result))

# 숫자만 추출
print('숫자만 추출 =>', re.findall('[0-9]', txt1))
# 집합으로 변환 (중복숫자 제거)
print('set 집합으로 중복숫자 제거 => ', set(re.findall('[0-9]', txt1)))

# 대문자소문자 추출
print(re.findall('[a-z]+', txt1)) #['python', 'java', 'ava', 'cript']

# + 를 붙여야 단어단위로 나옴
print(re.findall('[a-z]', txt1)) #['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'a', 'v', 'a', 'c', 'r', 'i', 'p', 't']

print(re.findall('[a-zA-Z]+', txt1))
# ['python', 'java', 'WORD', 'ENGLISH', 'JavaScript']

# 한글, 숫자
print(re.findall('[0-9가-흫]+', txt1)) #['가나다', '009', '7834', '파이썬', '784']

#re.finditer(패턴식, 대상문자열) 메서드 적용
result = re.finditer('[0-9]+', txt1)
print(result, type(result))
for item in result:
    print(item)

# Match object 메서드
# group() : 매치된 문자열을 리턴한다.
# start() : 매치된 문자열의 시작 위치를 돌려준다.
# end() : 매치된 문자열의 끝 위치를 돌려준다.
# span() : 매치된 문자열의 시작,끝 위치를 튜플 형태로 돌려준다.
print('-'*50)
result = re.finditer('[가-힣]+', txt1)
for item in result:
    print(item)
    print(item.group(), item.span(), item.start(), item.end())
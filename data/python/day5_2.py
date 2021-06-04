'''

'''

'''
    파일입출력함수 (교재 p171)

     파일입출력
     파일변수  = open(파일경로, 'r'/'w'/'a', encoding='utf-8/cp949')
                            read, write, append
     파일변수.파일입출력함수(옵션)
    
     파일읽기
     파일변수 생성
     파일변수  = open(파일경로, 'r', encoding='utf-8/cp949')
     파일변수.read() : 파일전체 문자열 구조 =>  문자열
     파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
     파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트
'''

import os

#현재 작업폴더 확인 (current working directory)
print(os.getcwd()) #C:\Anaconda3\python.exe C:/pyclass/h_day5_2.py

#작업폴더 변경 (change directory)
#os.chdir('data') #C:\pyclass

#디렉토리안의 파일 목록을 리스트로 출력 (list directory)
print(os.listdir(os.getcwd()))

#파일 변수 생성
f = open('data/Yesterday.txt', 'r') #r -> 읽기
print(f,type(f))

print(f.read(), type(f.read())) #파일변수.read -> 문서 전체를 읽음
print('*'*30)
f.close()
f = open('data/Yesterday.txt', 'r')

print(f.readline(), type(f.readline()))#.readline() -> 파일의 첫행만
print('*'*30)
f.close()
f = open('data/Yesterday.txt', 'r')

print(f.readlines(), type(f.readlines()))#readlines() -> 각 행이 리스트 구조로 변경
print('*'*30)
f.close()
f = open('data/Yesterday.txt', 'r')


data = f.readlines()
for i in range(0,5):
    print(data[i])
print('*'*30)

#파일 닫기
f.close()

# 문서는 몇개의 어구로 구성되어 있을까?
# 단어별로 구성해서 리스트 구조로 변경
# 문자열변수.split() => 공백기준으로 리스트로 변경
f = open('data/Yesterday.txt', 'r')
data = f.read()

data_list = data.split()
print(len(data_list))  # 134(중복포함)
print(data_list)

data_list2 = list(set(data_list))
print(len(data_list2))
print(data_list2)   # 65(중복포함x)

# 파일 속 글자 count
print(data_list.count('yesterday')+ data_list.count(('Yesterday')))
f.close()


# ex) 파일 단어 전체 수와 3개의 단어가 표시되는 함수 정의
def printWord(url, option):
    f = open(url, 'r', encoding=option)
    data = f.read()
    data_list = data.split()
    print('\n\n 결과값')
    print(f'파일명 : {url}')
    print(f'단어갯수 : {len(data_list)}')
    print(f'단어 3개 출력 : {data_list[0:3]}')
    f.close()

printWord('data/yesterday.txt' , 'cp949')
printWord('data/yesterday.txt' , 'utf-8')

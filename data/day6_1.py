'''
        2020.11.12 수업
'''

import os

# 퀴즈
# data_eng.txt, data_kor.txt
# 파일안의 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
# 함수 정의 => 파일읽기 => 리스트화
# => 리스트의 값 더하기(숫자형데이터로 변환) : 합
# => 합 / 리스트갯수 : 평균

def File_sumAvr(url, op):
    # 파일 변수 생성
    f = open(url, 'r', encoding=op)
    # 파일 읽어서 리스트화
    data_list = f.readlines()
    # list 형변환 (str -> int)
    temp = []
    for item in data_list:
        temp.append(int(item))

    # 합계구하기
    sum = 0
    for item in temp:
        sum += item

    # 평균구하기
    avg = sum/len(temp)

    # 결과출력
    print(f'\t파일명 = {url}')
    print(f'\t데이타 = {temp}')
    print(f'\t총합 = {sum}, 평균 {avg:.3f}')
    print('\t','-'*30)
    f.close()

# 함수 호출
File_sumAvr('data/data_kor.txt', 'cp949')
File_sumAvr('data/data_eng.txt', 'cp949')



'''
    파일 쓰기 'w' :  새로운 파일이 생성되며 내용이 추가 (기존에 파일이 존재 시, 덮어쓰기)
    - 파일변수 = open( 생성파일경로, 'w', encoding='cp949/utf-8')
      파일변수.write(문자열)
      파일변수.close()
'''


# 현재 작업폴더 기준으로 폴더 생성
#os.mkdir('output')
folder_file_list = os.listdir(os.getcwd())
#리스트 목록에 output 폴더 있는지 확인
print('output' in folder_file_list)

# 빈파일 생성
f = open('output/test1.txt', 'w', encoding='cp949')
f.close()

# output폴더 안에 파일 생성 됐는지 check
os.chdir('output')
folder_file_list = os.listdir(os.getcwd())
print((os.getcwd()))
print('test1.txt' in folder_file_list)

# 상위폴더로 이동
os.chdir('../')

# 파일에 내용 저장
f = open('output/test2.txt', 'w', encoding='utf-8')

f.write('= '*20) #str만 가능
f.write('file write testing~\n')
f.write('today we gonna learn about python\n')
f.write('* '*40)

f.close()

# for문으로 파일 내용 추가
f = open('output/test3.txt', 'w', encoding='utf-8')
f.write('= '*20)
f.write('\n test3.txt writting\n')
for i in range(1,11):
    f.write(f'{i}번째 행입니다\n')
f.write('* '*40)
f.close()

# 리스트 요소를 파일 내용으로
foodList = ['라면', '케이크', '무뼈닭발', '마라샹궈', '마카롱', '플랫화이트']
f = open('output/test4.txt', 'w', encoding='utf-8')

#f.write(foodList) 처럼 리스트를 바로 넣어주려고 하면 TypeError 발생 (argument must be str, not list)
f.write(str(foodList))
f.write('\n')
for item in foodList:
    f.write('\n\t' + item)
f.close()

# ex) yesterday 파일에서 10줄 추출해 output 폴더 result.yesterday 파일에 저장하기
yesfile = open('data/Yesterday.txt', 'r')
yesList = yesfile.readlines()
onlyten = yesList[:10]
print(onlyten)
yesfile.close()

resultfile = open('output/resultYesterday.txt','w',encoding='utf-8')
resultfile.write(str(''.join(onlyten) ))
resultfile.close()

'''
#강사님 답
f = open('data/Yesterday.txt', 'r', encoding='cp949')
data = f.readlines()
print(data)
# 리스트에서 '\n' 제거하기
print("'\\n'  갯수 = ",data.count('\n'))
count = data.count('\n')
for i in range(count):
    data.remove('\n')
print("'\\n'  갯수 = ",data.count('\n'))
print(data)
# 10개만 리스트로 저장
data_list = data[0:10]
f.close()

f = open('output/result_Yesterday.txt', 'w', encoding='utf-8')
for i in data_list:
    f.write(i)
f.close()
'''



'''
    내용추가 'a' :  기존 파일에 내용추가
    - 파일변수 = open( 생성파일경로, 'a', encoding='cp949/utf-8')
      파일변수.write(문자열)
      파일변수.close()
'''
f = open('output/test1.txt', 'a', encoding='utf-8')
f.write('A ==> 내용 추가되었습니다')
f.close()

f = open('output/test1.txt', 'a', encoding='utf-8')
f.write('\nB ==> 내용 추가되었습니다')
f.write('\nC ==> 내용 추가되었습니다')
f.close()

f = open('output/test1.txt', 'r', encoding='utf-8')
print(f.read())
f.close()



'''

    with 문 &  파일 입출력 => 파일.close() 를 사용할 필요가 없다.
    - with open(파일경로, 'a'/'w'/'r', encoding='utf-8/cp949') as 파일변수:
        명령문

'''

# with 명령어로 파일 읽기
with open('data/color.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# with 명령어로 파일 쓰기
with open('output/test5.txt', 'w', encoding='utf-8') as f:
    for i in range(10,0,-1):
        f.write(str(i)+'\t')

# with 명령어로 파일에 내용 추가
with open('output/test5.txt', 'a', encoding='utf-8') as f:
    f.write('\n' )
    for i in range(1,10):
        f.write(f'{i}단 출력\n')
        for j in range(1,10):
            f.write(f'{i} * {j} = {i*j}\t')
        f.write('\n')


'''
    Delete 구현 1) 파일변수.write() => 파일변수.wrtie('') 파일 속 내용 삭제 but, 파일은 존재
    Delete 구현 2) 파일 삭제  =>  os.remove(파일경로)
'''

# 삭제 방법 1 (파일의 내용만 삭제)
with open('output/deleteTest.txt','w',encoding='utf-8') as f:
    f.write('')

# 삭제 방법 2 (파일까지 삭제)
# os.remove('output/deleteTest.txt')

# ex) 삭제 여부 묻고 삭제
ans = input('deleteTest.txt 를 삭제하시겠습니까?(y)').strip()
if ans == 'y':
    os.remove('output/deleteTest.txt')
    print('파일이 삭제되었습니다.')
else:
    print("파일 삭제 실패, 정확히 입력해주세요")
    
# ex) 파일이 존재 시 삭제
print(os.getcwd())
os.chdir('output')
print(os.getcwd())
fileList = os.listdir(os.getcwd())

if 'deleteTest.txt' in fileList:
    os.remove('deleteTest.txt')
    print('파일이 삭제되었습니다.')
else:
    print('파일이 이미 삭제된 상태입니다. ')
print(fileList)


"""
2020.11.05 진효주 작성
"""

#python 한 줄 주석

"""
여러줄 주석 처리는 따옴표 아무거나 3개 쓰기 작은따옴표나 큰 따옴표
"""

#파이썬의 print는 기본적으로 자동 줄바꿈
print(12)
print("문자출력")
print(False)

#줄바꿈 없이 출력을 원한다면 end 옵션 사용
print("Hello", end=', ')
print("Python", end=' ')
print("World")

print('"', end="")
print("따옴표 출력해볼까", end='"')

print("")

#변수 선언(할당) 시 자료형 정의 X (변수명만 정의)
num=5
print(num)

#쉼표 이용한 변수 할당 방법 (python만의 특징 중 하나)
word1 , word2 = "원", "투"
print(word1 + word2)

#중복선언도 가능
x = y = 100;
print(x + y)

"""" 퀴즈//  user1과 user2의 변수값 서로 변경하기 """
name1, name2 = "철수", "영희"
print("name1= " + name1)
print("name2= " + name2)

#클래식 방법 (temp 사용)
temp = name1
name1 = name2
name2 = temp
print("name1= " + name1)
print("name2= " + name2)

#파이썬 방법 (쉼표를 이용한 변수 교체)
name1, name2 = name2, name1
print("name1= " + name1)
print("name2= " + name2)

""" ////////// 퀴즈 끝 //////// """


#문자열 연산자 -> +는 연결, *은 반복을 의미
print("문자열" + " 연결할테다")
print("=" * 20)

#이스케이프 코드 (교재 48p)

#변수명 정의 방법 2가지
#카멜 표기법(대소문자로 단어 분리)
userAge = 10

#스네이크 기법(언더바나 대쉬로 단어 연결)
user_age = 10

'''파이썬 코딩 가이드
    변수 < 집합형 < 클래스 < 라이브러리 < 패키지
    
    클래스명은 첫글자 대문자로
    함수명은 소문자로 표시, 변수명은 소문자로 시작
    예약어 변수명으로 사용 X
    예약어를 키워드로 출력하려면 keyword를 import한 후 사용해야 함 
'''

#예약어 키워드로 출력하려면?
import keyword
print(keyword.kwlist) #키워드 리스트 나열
print("키워드 개수= ", len(keyword.kwlist)) #키워드 갯수 나열

#정의된 변수 삭제하기
#del한 후 변수 x를 또 출력하면 정의된 상태가 아니기 떄문에 오류남
del x

#데이터형 확인하기
print("Python is OPP일까? ")
a=True
b="파이팅"
c=123.123

print(a, type(a))
print(b, type(b))
print(c, type(c))



#입력문 (입력받은 값의 데이터형은 문자열)
'''
user_message = input("메세지 입력하쇼...\n")
print("입력받은 message : " + user_message)
print("입력받은 " +  user_message + "의 데이터 타입은", type(user_message))

#입력받은 값을 광범위하게 활용하기 위해선 자료형을 변환하는 캐스팅(Casting) 과정이 필요
print(int(user_message) + 15)



#퀴즈// 2개의 숫자값을 입력받은 후 사칙 연산을 수행하여라
num1, num2 = input("num1입력"), input("num2입력")
num1, num2 = float(num1), float(num2)

print("num1+num2= ", num1+num2)
print("num1-num2= ", num1-num2)
print("num1*num2= ", num1*num2)
print("num1/num2= ", num1/num2)
'''


#산술연산자 차이 (몫, 정수형 몫, 나머지)
print(100/3, 100//3, 100%3)

#대입연산자 (파이썬에는 ++, -- 없음)

#문자열 인덱싱(인덱싱은 문자열의 위치를 숫자료 표시한 것)
#인덱싱 첫 위치 0, 마지막 위치 -1
msg = "가나다라마바사"
print("첫글자" , msg[0])
print("마지막 글자", msg[6])
print("마지막 글자", msg[-1])
print("문자열 전체 길이", len(msg))
print("마지막 글자", msg[len(msg)-1])



#문자열 슬라이싱 : 문자열 일부를 잘라서 표시

#start부터 end-1까지 step 수 만큼 건너뛰기
#start:end:step, start:end, start:, :end
print(msg[2:5:1])
print(msg[1::3]) #end 값 없으면 끝까지라는 의미

#마지막값이 -1임을 참고, 그 뒤로 역순으로 가서 -5값인 곳에서 시작
#end값 -3 까지라는 의미는 end-1이므로 -4가 되서 문자열 "다라"만 출력됨
print(msg[-5:-3])


#출력 포맷 방식 
stName, stAge, score = '멀티캠', 24, 27.5468

#1. print문과 함께 사용하며 %으로 포맷팅
print('장소명 -> %s .. 나이 -> %d .. 성적 -> %.2f' %(stName, stAge, score))

#2. fotmat()이용한 포맷팅
print('장소명 -> {0} .. 나이 -> {1} .. 성적 -> {2:.2f}'.format(stName, stAge, score))

#3. f 이용한 포맷팅
print(f'장소명 -> {stName} .. 나이 -> {stAge} .. 성적 -> {score:.2f}')







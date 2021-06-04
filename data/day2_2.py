# 2개이상의 리스트 삽입
myList = [1 ,2, 3, 4, 5]
print(myList)

myList.extend(['가', '나'])
print(myList)

# 첫번째 위치에 2개 삽입
myList = [50, 90] + myList
print(myList)

# 2번째 위치에 n 개 삽입
myList = [myList[0]] + [True, False, True, True] + myList[1:]
print(myList)

#특정 위치에 리스트로 삽입 (리스트 안에 리스트 : 2차원 리스트)
myList.insert(0,['가','나','다'])
print(myList)




# 캐스팅
# 문자열 => 리스트
# list(문자열변수)

msg1 = "오늘도 좋은 하루"
msg2 = "가나/다라마/바사아자/차카타파하"

# 문자열변수.split() : 공백을 기준으로 해서 리스트화
result1 = msg1.split()

# 문자열변수.split(구분문자) : 구분문자를 기준으로 해서 리스트화
result2 = msg2.split("/")

# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경
result3 = list(msg1)

print(result1, type(result1)) #공복을 기준으로 리스트화
print(result2, type(result2)) #특정 문자열 기준으로 리스트화
print(result3, type(result3)) #['오', '늘', '도', ' ', '좋', '은', ' ', '하', '루'] 공백도 리스트로




# 리스트 => 문자열
# str(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화

list_change=['기차', '차고', '고양이']

# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
result1 = str(list_change)

# '구분자'.join(리스트이름)
result2 = ' '.join(list_change)

print(result1, type(result1), len(result1)) #['기차', '차고', '고양이'] <class 'str'> 19
print(result1[0], result1[-1]) #꺽새, 쉼표 등이 다 포함되기 떄문에 맨 첫번쨰와 맨 끝에 있는 꺽새가 출력 됨,  []
print(result2, type(result2), len(result2)) #기차 차고 고양이 <class 'str'> 9




# 중첩 리스트 구조 : 리스트안에 리스트가 있다

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]
list1 = [1,2,['a', 'b', 'c'], ['포도', '수박']]
print(f'list1={list1}, 리스트 전체 길이는= {len(list1)}') #전체 길이는 일차원 리스트로 봄
print(f'list[0]= {list1[0]}')

# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]
print(f'list1의 3번째에 위치한 리스트 요소의 첫 값은?  {list1[2][0]}')
print(f'list1의 4번째에 위치한 리스트 요소의 마지막 값은?  {list1[3][-1]}')

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
userName=['지뇨쥬','문채원','원필','아델에넬','대니']
userAge=[24,35,30,31,26]
userGender=['여','여','남','여','여']

#2차원 리스트로 정의
userInfo = [userName, userAge, userGender]
print('-'*20)
print(userInfo)

# 퀴즈 -----------------------------------------------------
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''

#내 답
grade=[[100, 80, 85],[55, 70, 35],[80, 80, 100],[90, 70, 88]]
print(f"kor : 합계= {(grade[0][0]+grade[0][1]+grade[0][2])}, 평균={(grade[0][0]+grade[0][1]+grade[0][2])/3:.2f} ")
print(f"math : 합계= {(grade[1][0]+grade[1][1]+grade[1][2])}, 평균={(grade[1][0]+grade[1][1]+grade[1][2])/3:.2f} ")
print(f"eng : 합계= {(grade[2][0]+grade[2][1]+grade[2][2])}, 평균={(grade[2][0]+grade[2][1]+grade[2][2])/3:.2f} ")
print(f"python : 합계= {(grade[3][0]+grade[3][1]+grade[3][2])}, 평균={(grade[3][0]+grade[3][1]+grade[3][2])/3:.2f} ")


#다른사람 답
kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
grade = [[sum(kor),sum(math),sum(eng),sum(python)],[sum(kor)/3,sum(math)/3,sum(eng)/3,sum(python)/3]]

print(f'kor:합계 = {grade[0][0]},평균:{grade[1][0]:.2f}')
print(f'math:합계 = {grade[0][1]},평균:{grade[1][1]:.2f}')
print(f'eng:합계 = {grade[0][2]},평균:{grade[1][2]:.2f}')
print(f'python:합계 = {grade[0][3]},평균:{grade[1][3]:.2f}')


#강사님 답
kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
# 2차원 리스트 생성
grade = [ kor, math, eng, python]
print(grade)

# 합계
korTot = grade[0][0] + grade[0][1] + grade[0][2]
mathTot = grade[1][0] + grade[1][1] + grade[1][2]
engTot = grade[2][0] + grade[2][1] + grade[2][2]
pythonTot = grade[3][0] + grade[3][1] + grade[3][2]

korAvg = korTot/3
mathAvg = mathTot/3
engAvg = engTot/3
pythonAvg = pythonTot/3

print(f'kor : 합계 = {korTot} , 평균 = {korAvg:.2f}')
print('math : 합계 = %d , 평균 = %.2f' % (mathTot, mathAvg))
print('eng : 합계 = %d , 평균 = %.2f' % (engTot, engAvg))
print('python : 합계 = %d , 평균 = %.2f' % (pythonTot, pythonAvg))

# -----------------------------------------------------------

#mysql에서 파이썬으로 데이터를 가져오면 튜플로 들고 옴

# 튜플
# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정)
# 튜플변수 = (값1, 값2...)

# 튜플 생성2 (초기값 지정)
# 튜플변수 = 값1, 값2...

# 튜플 생성3 (빈 튜플)
# 튜플변수 = (), 튜플은 리스트[]와 다르게 괄호()를 사용함

t1 = () #튜플생성3 방법
t2 = (100,200,300) #튜플생성1 방법
t3 = '가','나','다' #튜플생성2 방법

print(f't1={t1}, 자료형: {type(t1)}')
print(f't2={t2}, 자료형: {type(t2)}')
print(f't3={t3}, 자료형: {type(t3)}')

# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]

# 튜플에 새로운 값 추가 시에는 +=  연산자 이용  ex)튜플변수 += (값1, 값2...)
t1 += ('가','나','다')
print(t1, len(t1))

# 한개 추가시에는 쉼표(,)가 필요하니 주의하자 ex)튜플변수 += (값1,)
# t1 += ('스크립트')
# 쉼표 쓰지 않으면 TypeError: can only concatenate tuple (not "str") to tuple 라고 오류남
t1 += ('스크립트',)
print(t1, len(t1))

# 튜플의 값은 교체가 가능한가?
# TypeError , 내용 교체가 불가능하다.


# 튜플의 값은 삭제가 가능한가?
# 튜플 요소 각각의 값 삭제는 불가능
# 튜플변수 전체 삭제는 가능
# del 튜플변수

del t1
#rint(t1, len(t1)) #메모리에서 삭제했기에 NameError: name 't1' is not defined 라는 오류발생


# 튜플의 연산자 + : 튜플끼리 더하기
# 튜플의 연산자 * : 튜플 요소 반복
print(t2+t3)
print(t3*3)


# 각각 튜플 "변수" 정의하기
# 튜플전체변수 = (변수1, 변수2...) = (값1, 값2...)
color = (c1, c2, c3) = ("red", "green", "blue")
print(color) #튜플 전체 변수
print(c1) #각 값
print(c2)
print(c3)


# 튜플 함수
#튜플은 값 교체(안에 있는 내용의 변경)가 불가하기 때문에 sort,reverse 불가
# 튜플변수.sort()  가능한가? AttributeError
# 튜플변수.reverse()  가능한가? AttributeError

# 튜플변수.count(값)
myTuple=(100,200,100,100,300,100, True, '나')
print(myTuple.count(100))

# 튜플변수.index(값)
print(myTuple.index(True))


# 캐스팅
# 문자열 => 튜플 : tuple(문자열변수나 값)
# 리스트 => 튜플 : tuple(리스트변수나 값)
myString = "abcdefgh"
myList=[100,200,300,400]
t1 = tuple(myString)
t2 = tuple(myList)
print(t1, type(t1))
print(t2, type(t2))

# 튜플 => 문자열
# : str(튜플변수나 값)
# : 구분자.join(튜플변수나 값)
#  주의사항은 join() 사용시에는 튜플의 자료형이 문자열이어야 한다.
# 튜플 => 리스트 : list(튜플변수나 값)

myTuple=(1,2,3,4,5)
myTuple2=('a','b','c')

print(myTuple, type(myTuple))
result1 = str(myTuple)
# result2 = ' / '.join(myTuple) # 숫자로 구성된 튜플이라서 에러 발생
# TypeError: sequence item 0: expected str instance, int found
result2 = ' / '.join(myTuple2)
result3 = list(myTuple)

print(result1, type(result1)) # (1, 2, 3, 4, 5) <class 'str'>
print(result2, type(result2)) # a / b / c <class 'str'>
print(result3, type(result3)) # [1, 2, 3, 4, 5] <class 'list'>


#중첩 튜플
t1 = ((1,2,3),(4,5,6))
print(t1, len(t1)) #((1, 2, 3), (4, 5, 6)) 2  // len은 1차원 배열의 길이라서 묶음 당 1로 계산 따라서 2값이 나옴
print(t1[0])
print(t1[0][2])

# 튜플 리스트란?
# 리스트안에 튜플이 삽입되어 있는 구조
tA = (100,200,300)
tB = ('가','나','다')
rList = [tA, tA]
print(rList, len(rList), type(rList))
print(rList[0], len(rList[0]), type(rList[0]))
print(rList[0][0], type(rList[0][0]))
print('*'*30)

# 퀴즈
'''
아래와 같이 튜플을 정의한 후 출력한다.
튜플 리스트 : ('강아지','토끼','돼지','곰')
튜플 요소 추가 후 : ('강아지','토끼','돼지','곰','호랑이')
튜플의 0-3번째 요소 표시 : ('강아지','토끼','돼지','곰')
'강아지' 요소의 위치값은?
튜플을 문자열로 변환하여 출력 : ?
튜플을 리스트로 변환하여 출력 : ?
'''

#내 답
animal = ('강아지','토끼','돼지','곰')
animal += ('호랑이',)
print(f'튜플 리스트: {animal}')
print(f'튜플 0-3번째 요소는? {animal[:4]}')
print(f"'강아지' 요소의 위치값은? {animal.index('강아지')}")
print(f'문자열로 변환된 튜플: {str(animal)} / {type(str(animal))}')
tList=[animal]
print(f'리스트로 변환된 튜플: {tList} / {type(tList)}')


#다른사람 답
tuple = ('강아지','토끼','돼지','곰')
print(f'튜플리스트 : {tuple}')
tuple += ("호랑이",)
print(f'튜플 요소추가후 : {tuple}')
print(f'튜플의 0-3번째 요소 표시 : {tuple[0:4]}')
print(f'강아지 요소의 위치값은? : {tuple.index("강아지")}')
print(f'튜플을 문자열로 변환하여 출력 : {str(tuple), type(str(tuple))}')
print(f'튜플을 리스트로 변환하여 출력 : {list(tuple), type(list(tuple))}')


#강사님 답
# ctrl+d 커서 기준 한줄 복사. ctrl+y 커서 기준 삭제
print('-'*20)
animTuple = ('강아지','토끼','돼지','곰')
print('튜플 리스트 : ', animTuple)
animTuple += ('호랑이',)
print('튜플 리스트 : ', animTuple)
print('튜플의 0-3번째 요소 표시 : ', animTuple[0:4])
print(" '강아지' 위치값 : ", animTuple.index('강아지'))

# 이스케이프 문자
print(' \'강아지\' 위치값 : ', animTuple.index('강아지'))
myStr = ' , '.join(animTuple)
print('튜플을 문자열로 변환하여 출력 : ', myStr, type(myStr))
myList = list(animTuple)
print('튜플을 리스트로 변환하여 출력 :  ', myList)
# ------------------------------------------------

# 리스트는 [], 튜플은 (), 딕셔너리는 {}

# 딕셔너리 -> api이용해 크롤링 할 때 들어오는 JSON값 어쩌구...(?)
# CRUD : Create Read Update Delete
#딕셔너리는 인덱싱, 슬라이싱 불가

# 딕셔너리 생성 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능
dict1 = {'a':'apple', 'b':'banana', 'c':'cat'}
dict2 = {100:'apple', 200:'banana', 300:'cat'}

print(dict1, type(dict1))
print(dict2, type(dict2))

# 딕셔너리 생성 - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키값]=값
dict3 = {}
dict3[100]='백'
dict3[200]='이백'
dict3[300]='삼백'
print(dict3, type(dict3), len(dict3))

# 딕셔너리 요소 조회 : 인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시
print(dict3[100])


# 리스트, 튜플처럼 숫자 인덱싱이 가능할까? NO
# KeyError : 딕셔너리는 키값으로만 호출가능
#print(dict3[-1]) 
# KeyError: -1 에러남

# 리스트, 튜플처럼 슬라이싱이 가능할까? NO
# TypeError 딕셔너리는 슬라이싱이 불가능
# print(f'dict3[0:2] = {dict3[0:2]}')
#print(dict3[0:2])
#TypeError: unhashable type: 'slice' 타입에러 남

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
dict4 = {'a':'apple', 'b':'banana','c':'cat', 'a':'apart'}
print(dict4)
print(dict4['a']) #apart출력됨 -> 키값 중복 시 마지막 키값만 유효함을 볼 수 있음(덮어쓰기라고 보면 됨)

# 딕셔너리 값 교체
# 딕셔너리[키값]=값
dict4['c'] = 1000
print(dict4)



# 딕셔너리 요소 삭제
# 딕셔너리변수.pop(키값)
dict4.pop('a')
print(dict4)

# 딕셔너리변수.clear()
dict4.clear()
print(dict4)

# del 딕셔너리변수
# del 딕셔너리변수[키값]
del dict4
#print(dict4) #삭제돼서 출력에러남-> NameError: name 'dict4' is not defined


# 딕셔너리 함수

# 딕셔너리에서 키값만 리스트로 만들어서 마지막 키값 조회
dict5 = {100:'apple', 200:'banana', 300:'car', 400:'world', 500:'python'}

# 딕셔너리변수.values() : 값 만 표시
print(dict5.values())
print(dict5.values(), '\n', list(dict5.values()))

# 딕셔너리변수.keys() : 키값만 표시
print(dict5.keys(), '\n', list(dict5.keys()))

# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)...
print(dict5.items(), '\n', list(dict5.items()))


# 딕셔너리에서 키값만 리스트로 만들어서 마지막 키값 조회
result = list(dict2.keys())
print(result)
print(result[-1])
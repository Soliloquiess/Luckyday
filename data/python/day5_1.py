'''
        2020.11.11 수업
'''

'''
 수학관련 내장 함수
 절대값 리턴 : abs(숫자)
 최대값 리턴 : max(리스트/튜플/집합...)
 최소값 리턴 : min(리스트/튜플/집합...)
'''
num = -10
print(abs(num))

myList=[10,67,800,65,-100]
myTuple=(10,67,850,65,-100, -150)
print(max(myList), min(myList))
print(max(myTuple), min(myTuple))


'''
    나누기 연산자 /(실수), //(정수) ,  나머지 연산자 %
    divmod(n1,n2) => 몫과 나머지 값 구함 => 튜플
'''
print(divmod(100,33), type(divmod(100,33)))


'''
    enumerate(리스트/튜플/문자열,인덱스숫자)
    인덱스 숫자로 구성된 리스트/튜플/문자열 => enumerate 객체 생성
    for...in 하나씩 아이템 출력 가능 => 각각 튜플아이템으로 생성(인덱스,값)
'''
myList=[10,67,800,65,-100]
myTuple=(10,67,800,65,-100)
myTxt= "가나다하자치"
myDict= dict(enumerate(myList)) #딕셔너리로 캐스팅(형변환)
print(myDict)


result = enumerate(myTuple)
print(result)

for item in result:
    print(item, type(item)) #(인덱스번호, 값) 튜플구조로 출력됨

#인덱스 번호를 51부터 시작하고 싶을 때 (인덱스 번호 셋팅가능)
result = enumerate(myTuple, 51)
for item in result:
    print(item, type(item))

result_dict = dict(enumerate(myTuple, 51))
for key in result_dict:
    print(key , '=>', result_dict[key])

result_list = list(enumerate(myTuple, 51))
for item in result_list:
    print(item)

# 튜플 리스트
print(result_list)
print(result_list[0][0])
# [(51, 10), (52, 67), (53, 800), (54, 65), (55, -100)]

# 문자열 => 딕셔너리
result = dict(enumerate(myTxt, 11))
print(result)


'''
    eval(문자열 계산식) : 문자열 계산식의 결과값을 리턴
'''
#cal = input('계산식 입력...')
#print(cal, type(cal)) #34-12 <class 'str'>
#print(f'{cal} = {eval(cal)}') #34-12 = 22 (결과값 리턴)


# #퀴즈1
# inputList = []
# for i in range(5):
#     inputList.append(input('숫자를 입력하시오..'))
# print(f'{inputList} 의 최대값 => {max(inputList)}, 최소값 => {min(inputList)}')
#
#
# # 퀴즈2 :  divmod() 함수를 이용하여 다음과 같은 출력화면이 나오도록
# 몫 = 27
# 나머지 = 1
#
# # print(f'몫 = {divmod(55,2)[0]}')
# # print(f'나머지 = {divmod(55,2)[1]}')
#
# x, y = divmod(55,2)
# print(f'몫 = {x}')
# print(f'나머지 = {y}')
#
#
# # 퀴즈 3 : 리스트를 양수로 모두 출력하는 함수를 정의하고 호출하여라
# # def absTrans(리스트변수) :
# #       명령문
#
# # 함수 호출
# absTrans([-90, 100, -67, 55, -33])
#
# # 결과
# [90, 100, 67, 55, 33]


# def absTrans(list):
#     result = []
#     for item in list:
#         result.append(abs(item))
#     return result

# def absTrans(list):
#     for i in range(len(list)):
#         list[i] = abs(list[i])
#     return list

# def absTrans(list):
#     return [abs(i) for i in list]
#
# print(absTrans([-90, 100, -67, 55, -33]))




'''
    아스키코드와 관련된 함수 -> chr() , ord()
    - chr(숫자) => 아스키코드값에 해당하는 문자나 숫자, 문자의 아스키 코드 값을 돌려주는 함수
    - ord(관련 문자나 숫자) => 아스키코드값 리턴, chr()과 반대되는 함수
    - ASCII 코드표  https://ko.wikipedia.org/wiki/ASCII
'''
print(chr(56), ord('A'))

#대문자 알파벳으로 구성된 리스트 생성
result = []
for i in range(65,91):
    result.append(chr(i))
print(result)


'''
    # 리스트/튜플 등의 원소값이 False 값인지 True 값인지 Boolean 형(True/False)로 표시
    - all(리스트/튜플/집합) :  값이 모두 True 조건이면 True
    - any(리스트/튜플/집합) : 값중 하나라도 True 조건이면 True
     False 조건값 : None, 0, 0.0, '', False
     True 조건값 : 0이 아닌 숫자, 공백포함+문자열, True
'''
listA = [0, False, '', None]
listB = [10, False, ' ', None]
listC = [3, True, '가나다']
print(all(listA), all(listB), all(listC))
print(any(listA), any(listB), any(listC))

'''
    # 유효성 검사 : 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
    - 문자열변수.isalpha() : 모두 문자(알파벳,한글..)인가? 숫자문자제외 , True/Fasle
    - 문자열변수.isdigit(), 문자열변수.isnumeric() : 모두 숫자문자인가?  , True/Fasle
    - 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
    - islower(), isupper() : 대문자/ 소문자 검사
    - isdecimal() : 모두 10진수인가?
'''


# def makeNumList():
#     result = []
#     while True:
#         data = input('데이터 입력 =>')
#         if data.isdigit():
#             result.append(data)
#             print('리스트가 출력되었습니다')
#         else:
#             print('숫자X, 다시 입력 바랍니다')
#
#         #탈출조건
#         if len(result) == 5:
#             break
# makeNumList()



# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라// 결과 >> 숫자 갯수 : ? 문자 갯수 : ?
testWord = 'Python1234Java4774'

#방법1
def count1():
    digit_cnt, str_cnt = 0, 0
    for i in range(len(testWord)):
        if testWord[i].isdigit():
            digit_cnt += 1
        else:
            str_cnt += 1
    print(f'숫자 갯수 => {digit_cnt}, 문자 갯수=> {str_cnt}')

#방법2
def count2():
    digit_cnt, str_cnt = 0, 0
    for item in testWord:
        if item.isdigit(): digit_cnt += 1
        else: str_cnt += 1
    print(f'숫자 갯수 => {digit_cnt}, 문자 갯수=> {str_cnt}')

count1()
count2()

'''
    dir(자료형) => Reference 기능
    사용가능한 속성과 함수를 리스트 구조로 표시
'''
print(dir('String'))
print(dir(True))
print(dir(100))
print(dir([1,2,3,4,5]))
print(dir((1,2,3,4,5)))
print(dir({1:'하나', 2:'둘'}))
print(dir({1,2,3,4,5}))
print('-'*10, '\n'*2)

'''
    zip(리스트1, 리스트2 .. ): 리스트의 각 아이템요소를 튜플화 구조로 묶음
    zip(*zip객체) : zip으로 묶어준 객체를 원래대로 품
    
    - zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
    - list(zip 객체): [(아이템1,아이템2) ...]
    
    (unzip) zip으로 리스트안의 튜플구조 해제하기 -> 변수1, 변수2 = zip(*리스트튜플이름)
'''

p1 = ['길동', '동미', '미영', '영철']
p1Gender = ['남','여','여', '남']

result = zip(p1, p1Gender)
print(result) #<zip object at 0x0000020CE110E6C0>
for item in result:
    print(item)

#리스트화 (튜플리스트)
print(list(zip(p1,p1Gender)))

#unzip
myListTupe = [('a','apart'),('y','yes'),('b','base')] #리스트 튜플 정의
x, y = zip(*myListTupe)
print(f' x = {x}, {type(x)}')
print(f' y = {y}, {type(y)}')

# ex) 딕셔너리 구조를 튜플 형태로 변경
# 딕셔너리  => 키 리스트, 값 리스트 => zip =>  unzip 튜플
myDict = {'a':'africa', 'd':'drama', 'm':'movie'}
print(f'myDict = {myDict}, {type(myDict)}')
print(list(myDict.keys()))
print(list(myDict.values()))
result = zip(list(myDict.keys()), list(myDict.values()))
for i,j in result:
    print(i, '=', j)
result2 = list(zip(list(myDict.keys()), list(myDict.values())))
print(result2)


#----------------------------점심시간 !!!
'''
    RANDOM (외장모듈)
    - random.randint(start, end) : start~end 사이의 정수 난수
    - random.choice(리스트) : 리스트에서 랜덤하게 뽑기
    - random.shuffle(리스트) : 리스트를 랜덤하게 섞기
'''
import random

#범위 내에서 정수뽑기
print(f'1-30사이 숫자 랜덤뽑기 => {random.randint(1, 30)}')
print(f'1-30사이 숫자 랜덤뽑기 => {random.randint(1, 30)}')

#리스트에서 하나 뽑기
eventList = ['꽝', '카니발','5000만원','스벅 3만원권']
print(f'뽑기 => {random.choice(eventList)}')
print(f'뽑기 => {random.choice(eventList)}')

#실수 난수
print(random.random())

#리스트 섞기 (원본을 섞는거라 바로 print문에 쓸 수 x -> None 출력됨)
print(f'eventList = {eventList}')
random.shuffle(eventList)
print(f'eventList = {eventList}')
random.shuffle(eventList)
print(f'eventList = {eventList}')

# 학생중 2명을 오늘의 청소 당번으로 뽑을 떄
# random.shuffle() 함수를 이용하여 2명만 출력하여라.
studentList = ['기대주', '하민수', '이동백', '김철수', '홍길동', '이승기', '김남길']
def todayclean(list):
    result = random.shuffle(list)
    for i in range(2):
        print(f'오늘의 청소 당번 => {list[i]}')
todayclean(studentList)

'''
    FILTER
    - filter(함수명/lambda 함수, 리스트/튜플)
    
    반환값 list, 사용할 함수는 결과값이 True/False
    함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
    => 참인조건의 리스트만 출력

'''

#리스트에서 짝수만 추출  ver.filter() 미사용
list1 = [10,56, 77, 33, 88, 100]
result=[]
for item in list1:
    if item %2 == 0:
        result.append(item)
print(f'결과 => {result}')

def odd(num):
    if num % 2 == 0:
        return True
print(odd(100)) #True
print(odd(43)) #None

#리스트에서 짝수만 추출  ver.filter() 적용
print(filter(odd,list1)) #<filter object at 0x000002C3D64CA0D0>
for i in filter(odd,list1):
    print(i, end = " ")
print()
print(f'결과 => {list(filter(odd,list1))}')

#람다함수 filter()사용


# 아래 리스트에서 양수만 리스트로 출력하여라
numlist = [10, -30, 20, 5, -100]
print(f'numlist = {numlist}')
# 방법1 => 일반함수
def positive(list):
    result = []
    for item in list:
        if item>0:
            result.append(item)
    return result
print(f' 결과1 = {positive(numlist)}')

# 방법2 => 함수+filter
def positiveOne(n):
    return n>0
# print(positiveOne(90))
# print(positiveOne(-99))
print(f' 결과2 = {list(filter(positiveOne,numlist))}')

# 방법3 => 람다함수+filter
# f = lambda n:n>0
# print(f(100))
# print(f(-100))
print(f' 결과3 = {list(filter(lambda n:n>0,numlist))}')

'''
    MAP() 함수
        - map(함수명/lambda 함수, 리스트/튜플), -> map오브젝트 생성
        - 반환값 list
        - list(map(정의된함수나 lambda함수, 데이타(리스트,튜플))) 형식으로 사용
        : 데이타 요소를 정의된함수의 결과값으로 리턴하고 결과값을 리스트 요소로 추가
'''

#리스트의 제곱을 구해서 새로운 리스트로 만들기
numlist2 = [1,2,3,4]

#방법1) 일반함수
def power_list(list):
    result=[]
    for item in list:
        result.append(item**2)
    return result
print(f'방법1 : {power_list((numlist2))}')

#방법2) 함수 + map()
def power_one(n):
    return n**2
print(f'방법2 : {list(map(power_one,numlist2))} ')

#방법3) 람다 + map()
print(f'방법3 : {list(map(lambda n:n**2,numlist2))} ')


# ex) 두 리스트에서 인덱스가 같은 값을 서로 곱한 후 리스트로 만들기
list1 = [2,3,7]
list2 = [4,5,9]

#방법 1 -> 일반함수
def make_numlist(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i]*list2[i])
    return result
print(f'list1={list1}, list2={list2}')
print(f'방법1 : {make_numlist(list1,list2)}')

# 방법2 => 함수 + map()
def mul_two(x, y):
    return x*y
print(f'방법2 : {list(map(mul_two, list1, list2))}')


# 방법3 => 람다함수 + map()
# f = lambda x,y:x*y
# print(f(10,22))
print(f'방법3 : {list(map(lambda x,y:x*y, list1, list2))}')


'''
    REDUCE()
    - import functools
      functools.reduce(함수명/lambda 함수, 리스트/튜플)
      : 리스트의 요소에 함수를 적용해 1개의 결과를 리턴

    - 모듈내의 함수 사용 사용 시 별칭 지정해 사용할 수도 있음
      import functools as f
      f.reduce(옵션)
'''
import functools

# 리스트의 모든 합을 구해라
numlist3 = [90, 67, 45, 34, 77, 23, 30]

# 방법1 = 일반함수
def sumList(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

print(f'numlist3 : {numlist3}')
print(f'방법1 : {sumList(numlist3)}')

# 방법2 = 함수 +reduce()
def sumNumber(x,y):
    return x+y
print(f'방법2 : {functools.reduce(sumNumber, numlist3)}')

# 방법3 = 람다함수 +reduce()
# f = lambda x,y:x+y
print(f'방법3 : {functools.reduce(lambda x,y:x+y, numlist3)}')
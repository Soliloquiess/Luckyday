# for .. in range(start, end, step) { 명령문 }
# for item in 문자열/튜플/리스트 { 명령문 }
# for key in 딕셔너리 { 명령문 }
# 리스트변수 = [ 결과값 for 문 ]

# 1~10까지 출력한다.
for i in range(1, 11):
    print(i, end = ' ')
print('\n','-'*20)

# 10~1 까지 출력한다.
for i in range(10, 0, -1):
    print(i, end = ' ')

print('\n','-'*20)

#중복 for문 (range안 값이 생략됐다면 0부터 시작하고 5는 END값을 의미)
for i in range(5):
    print(i)
    for j in range(3):
        print(j, end = ' ')
    print()
print('\n','-'*20)

#for item in 문자열/튜플/리스트 {명령문}
myList = [100,200,300,400,500]
for item in myList:
    print(item)
print("\n", "-"*20)

#for key in 딕셔너리 {명령문}
myDict = {'가':'가지', '나':'나라', '다':"다람쥐"}
for key in myDict:
    print(key, '=>', myDict[key])

#list 변수 = [결과값 for 문]
#1-100까지 3의 배수
result = [i for i in range(3,101,3)]
print(result)

#1-100까지 3의 배수 제거
result = [i for i in range(1,101) if i%3 != 0]
print(result)
#--------------------------------- 어제 수업 REVIEW END

print('-'*30, '11월 10일 수업 시작 ', '▶'*10)

# 다중 리스트와 for
# 다중 리스트에서 for문을 쓰려면 2차원 리스트의 갯수가 같아야 함 (아래 예제는 2개씩이므로 ok)
# for (i, j...) in 다중리스트: 명령문

listMulti1 = [[1, 2],
              ['a', 'b'],
              ['홍길동', '춘향이']]

print(listMulti1[0]) # [1, 2]
print(listMulti1[0][0]) # 1
print(listMulti1[1][1]) # b
print()

listMulti2 = [[1, 2, 3],
              ['a', 'b','c'],
              ['홍길동', '춘향이','흥부']]

for (i, j, k) in listMulti2:
    print(f'i = {i} / j = {j} / k = {k}')
    print('-'*10)
    

listMulti3 = [[2,100],
              ['a','b'],
              ["장화","홍련"]]
for(i,j) in listMulti3:
    print(i,j)

# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균   
김태희     30   40   100   ?     ?
...

'''
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

for (name, kor, eng, math) in stGradeList:
    print(f"학생이름\t국어\t영어\t수학\t합계\t평균\n"
          f" {name}\t{kor}\t{eng}\t{math}\t{kor+eng+math}\t{(kor+eng+math)/3:.1f}")


# 사용자정의함수 def 정의
# 호출시 함수명(값1, 값2 ...)
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 함수 정의 1 : 인자와 리턴문 없는 가장 간단한 스타일
# ex) 함수 호출시 특정 메세지 3번 출력
def helloWorld(): #선언
    for i in range(3):
        print("Hello World")
    print()
helloWorld() #호출


# 함수 정의 2 : 인자가 있으나 리턴문 없는 스타일
# ex) 메세지를 인자로 넘겨서 3번 출력하는 함수 정의
def hello(message):
    for i in range(3):
        print(f'hello {message}')
    print()
hello("python")
hello("MySQL")

# ex) 특정 메세지 n번 반복
def helloN(n,message):
    for i in range(n):
        print(f'{i+1} hello {message}') #i가 0부터 시작이라 +1함
    print()

helloN(2,'PANDAS')


# 함수 정의 3 : 인자는 없고 리턴문만 있는 스타일
# 즉, return 문은 함수를 탈출 용도 / return문 아래의 명령은 실행되지 x
# ex) 문자열 반환
def result():
    return 'HelloWorld'
print(result())

# 함수 정의 4 : 인자, 리턴문 둘다 존재
# ex) 이름을 인자로 설정, 인사말 + 이름 리턴
def wecome(name):
    return name + '님 환영합니다'
print(f'{wecome("진효주")}')

# ex) 1-100까지 합 구하는 함수 정의
def sum100():
    sum=0
    for i in range(1,101):
        sum+=i
    return sum
print(f'1-100까지의 합은 => {sum100()}')

'''
퀴즈 1: n까지의 누적합을 반환하는 함수 정의 후 호출 
print(f'1~500까지의 합은? {sumN(500)}')
print(f'1~2000까지의 합은? {sumN(2000)}')

퀴즈 2: x~y까지의 누적합을 반환하는 함수 정의 후 호출 
       2개의 수 x, y를 인자로 전달하여 누적합 구하기        
print(f'100~500까지의 합은? {sumXY(100,500)}')
print(f'500~1000까지의 합은? {sumXY(500, 1000)}')
'''
#퀴즈 1 풀어보기
def sumN(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(f'1~500까지의 합은? {sumN(500)}')
print(f'1~2000까지의 합은? {sumN(2000)}')


#퀴즈 2 풀어보기 (약간 변형해서 품)
def sumXY(x,y):
    sum=0
    for i in range(x,y+1):
        sum += i
    return sum

#print(f'입력받은 시작값 x와 끝값 y의 총 누적값은 => '
#      f'{sumXY(int(input("x값을 입력하시오=>")), int(input("y값을 입력하시오=>")))}')


# 함수 정의 5 : 리턴 값 다중인 스타일
# 다중 return 값의 자료형은 튜플이고 각각의 결과값은 인덱싱 으로 접근

# 인자 X,  리턴값 2개이상
def multiReturn1():
    x = 100
    y = 7
    return x+y, x*y, x-y, x//y, x%y

print(multiReturn1(), type(multiReturn1()))
result = multiReturn1()
print(f'100과 7의 연산 => 더한값은? {result[0]}')
print(f'100과 7의 연산 => 차이값은? {result[2]}')

# 인자 O,  리턴값 2개이상
# ex) n개 입력값 이용 -> 튜플, 리스트로 변환
'''def multiReturn2(n):
    result=[]
    for i in range(n):
        item = input('값 입력 => ')
        result.append(item)
    resultTuple = tuple(result)
    return result, resultTuple
print(multiReturn2(3))'''


# 함수 정의 6  : 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
# ex) 숫자 합 출력 함수 정의 -> 인자 O, return
def sumTwo(x=0, y=0):
    print(f'{x} + {y} = {x+y}')

sumTwo()
sumTwo(100)
sumTwo(23, 67)

# ex) 숫자의 곱을 출력하는 함수 정의 -> 인자 O, return O
def multiTwo(x=1, y=1):
    # return x*y
    return f'{x} * {y} = {x*y}'

print(multiTwo())
print(multiTwo(8))
print(multiTwo(10, 67))

# 함수 정의 7 : 인자의 초기값 설정 (특정 인자만 초기값이 존재할 경우 초기값이 주어진 인자를 뒤로 배치)
'''
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# ex) 숫자의 모든 합
def sumNumber(x, y=0, z=0):
    return f'{x} + {y} + {z} = {x+y+z}'

print()
print(sumNumber(10))
print(sumNumber(10,30))
print(sumNumber(20,50,100))


# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~elif~else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다

# 조건문 if

# 조건문 1 - 단순 if 문
# if 조건:
#   명령문

# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

a, b = 1, 10
if a>b:
    print("a는 b보다 크다")
if a<b:
    print("a는 b보다 작다")
if a==b:
    print("a와 b는 같다")


'''
#짝홀수 판별
num = int(input("짝수 판별할 수를 입력하세요: "))
if (num%2 == 0):
    print(f"{num}은 짝수입니다")
if (num%2 != 0):
    print(f"{num}은 홀수입니다")

#배수 판별
myNum = int(input('숫자값을 입력해주세요 ... '))
if (myNum%3 == 0):
    print(f'{myNum} 은 3의 배수이다')
if (myNum%3 != 0):
    print(f'{myNum} 은 3의 배수가 아니다.')
'''


# 조건식에서 True가 되는 조건 = True, 0빼고 나머지숫자, 문자열
# 조건식에서 False가 되는 조건 = False, 0, '', None

# if True 조건식:
#    실행할 문장

if 124: #0이 아닌 수이기 때문에 True로 인식, True, 문자열 또한 마찬가지
    print("무조건 실행")


# if ~ else ~
'''
num = int(input("짝수 판별할 수를 입력하세요: "))

if (num%2 == 0):
    print(f"{num}은 짝수입니다")
else:
    print(f"{num}은 홀수입니다")
'''

# if ~ elif ~ else 다중 조건문
a = 10
b = 1
if a>b:
    print('a 는 b보다 크다')
elif a<b:
    print('a 는 b보다 작다')
else:
    print('a 와 b는 같다')


# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
'''
태어난 년도를 입력하세요? 2009
당신은 소띠입니다.


animalList = ['원숭이', ' 닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양']
year = int(input("태어난 년도를 입력하세요 =>"))

animal = year%12

if animal == 0:
    print(f"{year}년생인 당신은 {animalList[0]} 띠 입니다")
elif animal == 1:
    print(f"{year}년생인 당신은 {animalList[1]} 띠 입니다")
elif animal == 2:
    print(f"{year}년생인 당신은 {animalList[2]} 띠 입니다")
elif animal == 3:
    print(f"{year}년생인 당신은 {animalList[3]} 띠 입니다")
elif animal == 4:
    print(f"{year}년생인 당신은 {animalList[4]} 띠 입니다")
elif animal == 5:
    print(f"{year}년생인 당신은 {animalList[5]} 띠 입니다")
elif animal == 6:
    print(f"{year}년생인 당신은 {animalList[6]} 띠 입니다")
elif animal == 7:
    print(f"{year}년생인 당신은 {animalList[7]} 띠 입니다")
elif animal == 8:
    print(f"{year}년생인 당신은 {animalList[8]} 띠 입니다")
elif animal == 9:
    print(f"{year}년생인 당신은 {animalList[9]} 띠 입니다")
elif animal == 10:
    print(f"{year}년생인 당신은 {animalList[10]} 띠 입니다")
elif animal == 11:
    print(f"{year}년생인 당신은 {animalList[11]} 띠 입니다")
else:
    print(f"{year}년생인 당신은 {animalList[12]} 띠 입니다")
'''

# 조건문안에 조건문
# 숫자를 입력받아서
# 0, 양수, 음수, 숫자가 아니다.
# 입력받은 데이타가 숫자이면 데이터형 변경.
# 그렇지 않으면 메세지 출력
# 문자열.isdigit() : 문자열이 숫자이면 True

print('12345'.isdigit())
print('akjsj'.isalpha())

# 숫자인지 숫자가 아닌지 판독
data = '가나다라'
if data.isdigit():
    if int(data)>0:
        print('양수')
    else:
        print('0 제로')
else:
    print('숫자가 아니다.')


#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False

# 문자가 문자열에 있는가/없는가?
print('a' in 'banana')  # True
print('x' in 'banana')  # False
print('a' not in 'banana')  # False
print('x' not in 'banana')  # True


# 값이 리스트에 있는가?
myList = [100, 200, 300]
print(100 in myList) # True
print(100 not in myList) # False
print(1 in myList) # False
print(1 not in myList) # True

# if문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문


# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# else:
#   명령문2


# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3

twice = ['나연', '채영', '쯔위']
# item = '조이'
item = '쯔위'
if item in twice:
    print(f'{item}은(는) 트와이스 멤버이다.')
else:
    print(f'{item}은(는) 트와이스 멤버가 아니다.')

if item not in twice:
    print(f'{item}은(는) 트와이스 멤버가 아니다.')
else:
    print(f'{item}은(는) 트와이스 멤버이다.')


fruits = ('수박', '체리', '자두')
if '귤' in fruits:
    print('체리가 냉장고에 있다')
elif '아보카도' in fruits:
    print('아보카도가 냉장고에 있다')
else:
    print('냉장고에 아무것도 없다')



# pass 키워드 이용하기
# 명령문의 일종으로 비실행
# 함수, 클래스 생성시 등록만 시킬때 사용
'''
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
'''

# 반복문
# while 문
# for ... in
# for .. range()
# 다른 언어의 반복문 스타일 :
# for (i:0;i<10;i++)



# 반복문 : while
# while 조건:
#      실행명령
# 조건이 True 이면 명령을 실행해라

# 무한 루프
# while True:
#     명령문

# while True:
#     print('Python')

# while 조건:
#      실행명령
#      False 조건

# 초기값
# while False가 될 조건제시:
#      증감
#      실행명령


# Hello world n번 출력
cnt = 1
while cnt<=10:
    print(f'{cnt} => Hello Wrold')
    cnt += 1
print('while Test Finish')

#숫자 역순 출력 (10~1)
cnt = 10
while cnt>0:
    print(cnt, end=" ")
    cnt -= 1
    

#1-100합 구하기
num, sum =0 ,0
while num <=100:
    sum += num
    num+=1
print(f"1-100까지의 합 => {sum}")

#별찍기
cnt = 1
while cnt<=5:
    print("*"*cnt)
    cnt+=1;

#1-50까지 짝수만 출력
cnt = 1
while cnt<=50:
    if(cnt%2==0):
        print(cnt)
    cnt+=1
    

#n단 출력하기
'''
num =int(input("숫자 입력 => "))
cnt =1
while cnt<=9:
    print(f"{num} x {cnt} = {num*cnt}")
    cnt+=1
'''

# while문 이용해 리스트 요소 출력
list1 = ["사과","바나나","수박","포도"]
cnt=0
while cnt<len(list1):
    print(f'list의 {cnt+1} 요소 값은 {list1[cnt]} 입니다')
    cnt += 1
    
# 짝수번쨰 글자만 출력
txt1="가나다라마바사아"
cnt=1
while cnt<len(txt1):
    print(txt1[cnt])
    cnt+=2

# 점선 출력후 문단 3번찍기 반복하기
cnt1 = 1
while cnt1<=4:
    cnt2 = 1
    while cnt2<=3:
        print('\t Hello World')
        cnt2 += 1

    print('-'*20)
    cnt1 += 1

# 구구단 2-9단
num1 = 2
while num1<=9:
    print(f'{num1} 단')
    num2 = 1
    while num2<=9:
        print(f"{num1} * {num2} = {num1*num2}")
        num2 += 1
    print("*"*20)
    num1 += 1

# 딕셔너리 구조에서 키와 값을 분리시켜서 출력하기
dict1 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y':'yes'}
klist = list(dict1)
vlist = list(dict1.values())

print(klist + vlist)

cnt=0
while cnt<len(klist):
    print(f'{klist[cnt]} => {vlist[cnt]}')
    cnt+=1


# 리스트에서 가장 큰 값을 구한 후 삭제하여라
# 리스트에서 요소 삭제
# 리스트변수.pop() : 마지막 삭제
# 리스트변수.pop(인덱싱값) : 인덱싱값에 해당하는 아이템 삭제
# 리스트변수.remove(값) : 값에 해당하는 아이템 삭제

myNumList = [100, 200, 50, -30, 999, 10, 999]

#s_myNumList = set(myNumList)
#l_myNumList = list(s_myNumList)
l_myNumList = list(set(myNumList))

cnt=0
max=l_myNumList[0];
while cnt<len(l_myNumList):
    if(max<l_myNumList[cnt]):
        max=l_myNumList[cnt]
    cnt+=1
l_myNumList.remove(max)
print(l_myNumList)


#pass는 주로 if문 반복문에선 break continue..
# break
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용


# 값을 입력받아서 리스트에 삽입한다.
# q를 입력하면 리스트를 출력한다.
'''
result = []
while True:
    item = input('리스트 값 입력 (q를 입력하면 입력 종료)....')
    if item == "q":
        break
    else:
        result.append(item)
print(result)
'''

# continue
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.

#1-30까지의 숫자 중 3의 배수만 미출력 시키기
cnt = 1
while cnt < 30:
    cnt += 1
    if cnt % 3 == 0:
        continue
    print(cnt, end=" ")
print('continue Test 종료')



# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경


# list( range(start, end , step) )
# : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) )
# : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) )
# : 순차적으로 숫자로 구성된 집합


print(range(0,10))
# range(0, 10)
print(list(range(0,10)))
print(tuple(range(0,10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(2, 21, 2)))
print(set(range(0,31,3)))
print(set(range(10)))
print(dict(enumerate(list(range(10, 101, 10)))))


# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문

# 1~10까지 출력하기
for i in range(1,11):
    print(i)

# 1~10까지 홀수만 출력하기
for i in range(1,11,2):
    print(i, end=' / ')
print('\n','-'*20)

# 1~100사이의 합 구하기
sum = 0
for i in range(1,101):
    sum += i
print(sum)
print('\n','-'*20)


# for 문에서 조건문 실행
# 1~25 까지 한줄에  5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''
for i in range(1,26):
    print(i, end=" ")
    if i%5 == 0:
        print()


# 1~27 에서 5의 배수만 빼고 출력하기
for i in range(1,28):
    if i%5==0:
        continue
    print(i, end=" ")


#다중 for문
for i in range(1,6):
    print(i)
    for j in range(1,4):
        print('/t/t', j)
    print('++++++++++')

# 다중 for 문을 이용하여 구구단 출력
for i in range(1,10):
    for j in range(1,10):
        print(i, "*", j, "=" , i*j)
    print("*"*15)

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

# 1~10까지 숫자로 이루어진 리스트를 만들어라
numList1 = []
for i in range(1,11):
    numList1.append(i)

numList2= [i for i in range(1,11)]

print('numList1 = ', numList1)
print('numList2 = ', numList2)

#3단의 결과값으로 리스트를 만들어라
numList2 = [i*3 for i in range(1,10)]
print('numList2 = ', numList2)

#3단의 결과값에서 -1한 값으로 리스트를 만들어라
numList2 = [i*3-1 for i in range(1,10)]
print('numList2 = ', numList2)

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']
stars = ['*'*i for i in range(1,11)]
print(stars)

#for문이 2번 있는 리스트 for
#리스트 변수 = [결과값 for 명령문1 for 명령문2 ]
#구구단 결고값으로 리스트 생성하기
gugudan = []
for i in range(2,10):
    for j in range(1,10):
        gugudan.append(i*j)
print('gugudan = ', gugudan)

#위 소스를 아래 한줄로 줄일 수 있다
gugudan2 = [i*j for i in range(2,10) for j in range(1,10)]
print('gugudan2 = ', gugudan2)


#for문 + if문 리스트 for
#리스트 변수=[결과값 for 명령문1 if 조건식 ]

#1-30까지의 숫자 중 5의 배수를 제외한 리스트를 만들어라
nonfive=[i for i in range(1,31) if i%5 != 0]
print(nonfive)


# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문
cityList = ['서울', '부산', '대구', '대전', '제주']

cnt = 0
while cnt<len(cityList) :
    print(cityList[cnt])
    cnt += 1

print('-'*20)

for item in cityList:
    print(item)
print('-'*20)


for item in '도레미파솔라시도':
    print('-----  ', item)
print('-'*20)


# for 를 이용한 딕셔너리 요소 출력
# for 키변수 in 딕셔너리:
#   명령문
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}

for key in myDict:
    print(key,' = > ', myDict[key])
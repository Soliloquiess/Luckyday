# 함수 정의 8 : 가변인자인 경우 -> 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문
'''

# 메세지 출력
def messagePrint(*args):
    return args

print(messagePrint('안녕하세요'), type(messagePrint('안녕하세요')))
print(messagePrint('안녕하세요','반가워요'), type(messagePrint('안녕하세요','반가워요')))
print(messagePrint('고맙습니다.','안녕하세요','반가워요'),
                    type(messagePrint('고맙습니다.','안녕하세요','반가워요')))

#학생 이름을 가변 매개변수로 전달, 세로로 출력
def studentName(*args):
    for item in args:
        print(item)

studentName('진효주', '서은기','강마루')
print()
studentName('진효주','문채원', '서은기','강마루')


def studentName2(*args):
    if len(args)==0:
        print('학생이 없습니다')
    else:
        cnt = 1
        for item in args:
            print(f'{cnt}번째 학생 : {item}')
            cnt += 1

studentName2('진효주', '서은기','강마루')
print()
studentName2('진효주','문채원', '서은기','강마루')
studentName2()


#퀴즈 : n개의 숫자의 합 구하는 가변함수 정의
def sumNumber(*args):
    if len(args) == 0:
        print('인자가 없습니다')
    else:
        sum = 0;
        for item in args:
            sum += item;
        print(f"결과 -> {sum}")
'''
def sumNumber(*args):
    if len(args) == 0:
        print('인자값이 없다')
    else:
        sum = 0
        tempList = []
        for item in args:
            sum+=item
            tempList.append(str(item))
        print(' + '.join(tempList), '=', sum)
'''

sumNumber() # 인자값이 없다
sumNumber(1,2) # 1 + 2 = 3
sumNumber(4,5,6) # 4 + 5 + 6 = 15
sumNumber(4,5,6,10,50) # 4 + 5 + 6 + 10 + 50 = 75



# 함수 정의 9 : 인자랑 가변인자랑 함께 있는 경우
'''
def 함수명(인자, *args):
    인자와 args를 이용한 명령문...
    return 값/변수/수식/명령문
'''
# ex) 문자는 인자, 숫자는 가변인자
def printParam(txt, *args):
    print('txt', '=', txt)
    print('args', '=', args)
    print()
printParam('라임', 10, 20)
printParam('오렌지', 650, 70, 135, 24)


# 계산기호인자 값에 따라서 뒤의 가변인자값을 계산하여라
# 함수 정의
def calChoice(choice, *args) :
    if choice == '*':
        result = 1
        for item in args:
            result *= item
        return print(f'계산결과 => 곱 : {result}')
    elif choice == '+':
        result=0
        for item in args:
            result += item
        return print(f'계산결과 => 합 : {result}')
    else:
        return print("계산오류")

calChoice('*', 20,30)
calChoice('+', 20,30,50)
calChoice('-', 20,30,50) # 해당되는 기호가 없어서 계산 오류



# 함수 정의 10 : 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값, 결과 데이터형은 딕셔너리
# kwargs = Keyword Arguments라고 불리며 **이 붙음
# 호출하는법은 함수명(키1=값1), 함수명(키1=값1, 키2=값3 ...) etc..

'''
def 함수명(**kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''

# ex) 딕셔너리 스타일로 인자 전달후 출력
def printDict(**kwargs):
    print(kwargs, type(kwargs))
printDict(key1='사과')
printDict(key1='사과', key2='바나나', key3='포도')

# ex) 딕셔너리 스타일의 가변인자 전달 후 세로로 출력
def printDict2(**kwargs):
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')
    print()
printDict2(a='apple')
printDict2(a='apple', s='snow', c='christmas', m='make')



# 함수 정의 11 : 초기값이 있는 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리

'''
def 함수명(**kwargs):
    # 초기값 지정
    kwargs[키값] = 값
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''

# ex) 사원 정보에 관련된 함수 정의
# nationality 키값의 초기값은 korea
def personInfo(**kwargs):
    # 초기값 지정
    kwargs['nationality'] = 'Korea'
    print('-'*30)
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')

personInfo(name='Maria', age=23, gender='female')
personInfo(name='홍길동', age=28, gender='male',nationality='USA' )


# 함수 정의 12 : 람다 함수 (def 로 정의하지 않고 한줄로 정의)
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''
# ex) 두수의 합 출력하는 람다 함수 정의
lambda_funtion = lambda x,y : print(f'{x} + {y} = {x+y}')
lambda_funtion(34,100)

# ex) 문자열에 인사말 추가 출력
f = lambda userName : userName + "님 오늘도 좋은 하루 되세요"
print(f('차지원'))



# 함수의 변수 영역 -> 스코프(Scope)
# 전역변수(문서 전체의 공통변수) ?
# 지역변수(함수내부에만 유효한 변수)?

# 함수내에서 지역변수를 전역변수로 정의 -> global 변수명

# 전역변수 정의
x = 10
y = 100
z = 200

def scopeTest():
    # 지역변수
    x = 0
    y = 0
    # 전역변수 선언
    global z
    z = 500
    print(f' 함수안의 x = {x}')
    print(f' 함수안의 y = {y}')
    print(f' 함수안의 z = {z}')

print(f' 함수밖의 x = {x}') # 10
print(f' 함수밖의 x = {y}') # 100
print(f' 함수밖의 z = {z}') #200

scopeTest()
# 함수안의 x = 0
# 함수안의 y = 0
# 함수안의 z = 500

print(f' 함수밖의 x = {x}') # 10
print(f' 함수밖의 x = {y}') # 100
print(f' 함수밖의 z = {z}') # 함수 내에서 global로 z를 전역변수 선언해주었기 때문에 500


# 함수
# 사용자정의함수
# 내장함수 : 별도의 import 명령이 필요없다, 함수(옵션)
# 외장함수 : 별도의 import 명령이 필요,  모듈.함수(옵션)

# datetime 모듈 이용하기
# 시간변수 = datetime.datetime.now()
# 시간변수.year
# 시간변수.month
# 시간변수.day
# 시간변수.hour


# 시간과 관련된 모듈 임포트
import datetime
now = datetime.datetime.now()
print(f' now = {now} , {type(now)}')

print('연도',now.year, '월',now.month, '일', now.day , '시간', now.hour, '분', now.minute)

if now.hour >= 12:
    print(f'현재시간은 오후 {now.hour-12}시 {now.minute}분 입니다.')
else:
    print(f'현재시간은 오전 {now.hour}시 {now.minute}분 입니다')


# 퀴즈2 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 12월은 겨울입니다.


# my answer
def month(month):
    if month in (12,1,2):
        print(f'{month}월은 겨울입니다')
    elif month in (3,4,5):
        print(f'{month}월은 봄입니다')
    elif month in (6,7,8):
        print(f'{month}월은 여름입니다')
    else:
        print(f'{month}월은 가을입니다')
month(now.month)

#강사님 답
def printMonth():
    now = datetime.datetime.now()
    # 봄 구분
    # if now.month>=3 and now.month<=5:
    if 3 <= now.month <= 5:
        print("{}월은 봄입니다!".format(now.month))
    # 여름 구분
    elif 6 <= now.month <= 8:
        print("{}월은 여름입니다!".format(now.month))
    # 가을 구분
    elif 9 <= now.month <= 11:
        print("{}월은 가을입니다!".format(now.month))
    # 겨울 구분
    else:
        print("{}월은 겨울입니다!".format(now.month))
printMonth()

# 요일 찍기
# 요일은 (월요일)0 ~ 6(일요일)
today = datetime.datetime.today().weekday()

print(today, type(today)) 

if today == 1:
    print('화요일 입니다.')
    
dayList = ['월요일','화요일','수요일,''목요일','금요일', '토요일','일요일']

print(f'오늘은 {dayList[today]} 입니다')




# time 모듈 이용하기

# time.time() : 현재 시간을 실수 형태로 리턴한다.
# time.localtime(time.time()) : time.time()의 값을 년도, 월, 일, 시, 분, 초로 변경 -> 리스트 자료 구조 형태

# 시간에 관련된 속성 리스트화
import time #타임모듈 임포트

result = list(time.localtime(time.time()))
print(result) # [2020, 11, 10, 17, 39, 48, 1, 315, 0]
print(type(result))
result2 = ['년', '월', '일', '시', '분', '초']
# ? 년 / ? 월 / ? 일 / ? 시 / ? 분 / ? 초 /
for i in range(0, len(result2) ):
    print(result[i], end=' ')
    print(result2[i], end=' ')


# 여러가지 출력 포맷 이용하기
# time.strftime('포맷코드1 포맷코드2', time.localtime(time.time()))
# 출력할 형식 포맷코드
# %a / %A  : 요일
# %b / %B  :  달
# %c : 날짜와 시간
# %d : 날(day)
# %H :24시간 기준의 시간
# %I :12시간 기준의 시간
# %j :1년중 누적 날짜 표시
# %x : 지역 기반 날짜 출력
# %X : 지역 기반 시간 출력
# %w : 숫자로된 요일 출력. 0은 일요일
# %Y : 년도 출력
# %Z : 시간대 출력
# %p : AM/PM

print('-'*30)
print(time.strftime('%x', time.localtime(time.time()))) # 11/10/20
print(time.strftime('%X', time.localtime(time.time()))) # 17:47:29
print(time.strftime('%c', time.localtime(time.time()))) # Tue Nov 10 17:47:29 2020
print(time.strftime('%a %A', time.localtime(time.time()))) # Tue Tuesday
print(time.strftime('%p %I', time.localtime(time.time()))) # PM 05
print(time.strftime('%p %H', time.localtime(time.time()))) # PM 17
print(time.strftime('%Y %b', time.localtime(time.time()))) # 2020 Nov


# 퀴즈
'''
오늘은 11 월  11 입니다.
1년을 기준으로 ?번째 날입니다.
'''
print(time.strftime('오늘은 %m월 %d일 입니다\n1년을 기준으로 %j번째 날입니다', time.localtime(time.time())))

#강사님 답
m = time.strftime("%m", time.localtime(time.time()))
d = time.strftime("%d", time.localtime(time.time()))
r = time.strftime("%j", time.localtime(time.time()))

print(f'오늘은 {m} 월  {d} 일 입니다.')
print(f'1년을 기준으로 {r} 번째 날입니다.')
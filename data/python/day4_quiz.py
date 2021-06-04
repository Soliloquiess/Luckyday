# ---------- for 반복문  ----------

# 1. 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하세요.
'''
[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
 총 22 개
'''

numList = [i for i in range(1,101) if i%7==0 or i%11==0 ]
print(numList, len(numList))


# 2. 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여 보세요
# ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']

#강사님 풀이
result = [str(i)+'-'+str(j) for i in range(1,6) for j in range(1,4)]
print(result)


# 3. 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여 보세요
# employees = [
#                 ['김수철', '서울', 25, '남', '총무부'],
#                 ['고길동', '부산', 33, '남', '회계부'],
#                 ['최미나', '대전', 22, '여', '기획부'],
#                 ['은지원', '서울', 44, '남', '영업부'],
#                 ['김영탁', '울산', 36, '남', '영업부'],
#                 ['마동탁', '대구', 50, '남', '기획부'],
#                 ['이은미', '창원', 42, '여', '총무부']
#               ]
#
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      고길동     부산     33     남     회계부
#      최미나     대전     22     여     기획부
#      은지원     서울     44     남     영업부
#      김영탁     울산     36     남     영업부
#      마동탁     대구     50     남     기획부
#      이은미     창원     42     여     총무부

employees = [
                 ['김수철', '서울', 25, '남', '총무부'],
                 ['고길동', '부산', 33, '남', '회계부'],
                 ['최미나', '대전', 22, '여', '기획부'],
                 ['은지원', '서울', 44, '남', '영업부'],
                 ['김영탁', '울산', 36, '남', '영업부'],
                 ['마동탁', '대구', 50, '남', '기획부'],
                 ['이은미', '창원', 42, '여', '총무부']
               ]

print('----------------------------------------')
print('사원명\t출신지\t나이\t성별\t부서')
print('----------------------------------------')
for (name, local, age, sex, sub) in employees:
    print(f'{name}\t{local}\t\t{age}\t{sex}\t{sub}')

print()
# 4. 남자 사원 목록만 출력하여 보세요.
for (name, local, age, sex, sub) in employees:
    if(sex=='남'):
        print(f'{name}\t{local}\t\t{age}\t{sex}\t{sub}')


# 5. 성이 '김'인 사원 목록만 출력하여 보세요.
# for (name, local, age, sex, sub) in employees:
#     if(name =='김'):
#         print(f'{name}\t{local}\t\t{age}\t{sex}\t{sub}')

#강사님 풀이
for (name, homtown, age, gender, part) in employees:
    if name[0] == '김':
        print(f' \t {name} \t {homtown} \t {age} \t {gender} \t {part} ')



# ------------------- 함수 퀴즈

# 퀴즈1 : 별찍기
# 숫자만큼 다음과 같은 형태로 출력하는
# 함수를 정의한 후 호출하여라.

'''
starPrint(5)

결과 :
*
**
***
****
*****

starPrint(3)

결과 :
*
**
***
'''

def starPrint(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*', end='')
        print()


starPrint(5)
starPrint(3)



# 퀴즈 2
# 인자값을 받아서 출력하는 구구단 함수를 정의한 후
# 호출하여 출력하여라
'''
def gugu(n):
    ?

gugu(9)

출력 >>
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81

'''
def gugu(num):
    for i in range(1,10):
        print(f'{num} x {i} = {num*i}')
gugu(9)

# 퀴즈 3:
# 리스트를 호출하면 각각의
# 아이템이 다음과 같이 출력되도록 함수를 정의하여라
'''
# printList(['라면', '빙수'])

   오늘의 메뉴   
1  :  라면
2  :  빙수

# printList(['모밀', '탕수육', '육계장'])
   오늘의 메뉴   
1  :  모밀
2  :  탕수육
3  :  육계장
'''

def printList(list):
    print("\t오늘의 메뉴")
    cnt = 1
    for item in list:
        print(f'{cnt} : {item}')
        cnt += 1

printList(['라면', '빙수'])
printList(['모밀', '탕수육', '육계장'])

# 퀴즈 4
# 키와 몸무게를 인자로 입력하여
# 메세지가 출력되도록 함수를 정의하고
# bmi 값에 따라 출력한다.
#
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
#
# bmi = (체중(kg)/키(m)의제곱)*1000
#
# bmi 값에 따라 다음과 출력한다.
#
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

'''
# 함수 호출 
Bmi(170, 68)


키 :  170
몸무게 :  68
과체중
BMI : 23.53

'''
print()
'''
def Bmi(k,w):
    bmi = (w/(k**2))*10000

    if bmi > 35:
        print(f'키 : {k}\n 몸무게 : {w}\n 고도비만\n BMI : {bmi:.2f}')
    elif bmi > 29:
        print(f'키 : {k}\n 몸무게 : {w}\n 중등도 비만\n BMI : {bmi:.2f}')
    elif bmi > 24:
        print(f'키 : {k}\n 몸무게 : {w}\n 경도비만\n BMI : {bmi:.2f}')
    elif bmi > 22:
        print(f'키 : {k}\n 몸무게 : {w}\n 과체중\n BMI : {bmi:.2f}')
    elif bmi > 18.4:
        print(f'키 : {k}\n 몸무게 : {w}\n 정상\n BMI : {bmi:.2f}')
    else:
        print(f'키 : {k}\n 몸무게 : {w}\n 저체중\n BMI : {bmi:.2f}')
'''

#강사님 답
def bmi(k,w):
    # k = k/100
    # bmi = (몸무게/키의제곱)*1000
    bmi = (w/(k**2))*10000

    print('===================')
    print('키 : ', k)
    print('몸무게 : ', w)
    print('BMI : %4.2f' % bmi)

    if bmi >= 35 :
        print('고도 비만')
    if 30 <= bmi < 35 :
        print('중등도 비만')
    if 25 <= bmi < 30 :
        print('경도 비만')
    if 23 <= bmi < 25 :
        print('과체중')
    if 18.5 <= bmi < 23 :
        print('정상')
    if bmi < 18.5 :
        print('저체중')


bmi(170, 68)
print()

# 퀴즈 5
# 아래와 함수를 호출하여 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 
say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 결과값 1
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
--------------------------------------------------
# 결과값 2
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''
def say_myself(name, old, woman=True):
    print(f'내 이름은 {name} 입니다\n나이는 {old}살 입니다.')
    if woman :
        print('여자입니다')
    else:
        print('남자입니다')
    print()

say_myself('김철수', 20, False)
say_myself('백설공주', 15)





'''
#강사님 답
def say_myself(name, old, man=True):
    print('-' * 50)
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    print ('-'*50)
    
say_myself('김철수', 20)
say_myself('백설공주', 15, False)
'''



# 퀴즈 6
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하고 호출하여라
'''
# 함수 호출 
addList(1,2,3,4)
addList('가','나','다','라','마')

결과1 >>>
총 갯수 : 3
데이타형 : <class 'list'>
0 번째 => 1
1 번째 => 2
2 번째 => 3

결과2 >>>
총 갯수 : 5
데이타형 : <class 'list'>
0 번째 => 가
1 번째 => 나
2 번째 => 다
3 번째 => 라
4 번째 => 마


'''






'''
#강사님 답
def addList(*args):
    listResult = list(args)
    print(f'\n\n총 갯수 : {len(listResult)}')
    print(f'데이타형 : {type(listResult)}')
    for i in range(0, len(listResult)):
        print(f'{i} 번째 => {listResult[i]}')

addList(1,2,3,4)
addList('가','나','다','라','마')
'''




# 퀴즈 7
# 첫번째 인자의 값이 'min'이면 다음 인자의 숫자 중
# 최대값을 출력하고
# 첫번째 인자의 값이 'max'이면 다음 인자의 숫자중
# 최소값을 출력하여라
# 이 때 전달하는 숫자의 갯수는 가변으로 한다.

'''
min_max_number('min', 100, 20, 40)
min_max_number('min', 100, 20, 40, 500, 1)
min_max_number('max', 100, 20, 40)
min_max_number('max', 100, 20, 40, 500, 1)

# 결과 
최소값은?  20
최소값은?  1
최대값은?  100
최대값은?  500

'''




'''
#강사님 답 
def min_max_number(choice, *args):
    if choice == "min":
        temp = args[0]
        for i in range(0, len(args)):
            if temp>args[i]:
                temp = args[i]
        return print('최소값은? ', temp)
    elif choice == "max":
        temp = args[0]
        for i in range(0, len(args)):
            if temp < args[i]:
                temp = args[i]
        return print('최대값은? ', temp)

min_max_number('min', 100, 20, 40)
min_max_number('min', 100, 20, 40, 500, 1)
min_max_number('max', 100, 20, 40)
min_max_number('max', 100, 20, 40, 500, 1)
'''




# 퀴즈 8
# **kwargs 인자 가변 함수를 이용하여
# 함수 호출시 결과값이 다음과 같이 딕셔너리 형태로
# 출력되도록 하여라
'''
# 함수 호출 
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

결과1 >>>

{'a': 'apple', 'b': 'banana', 'n': 'nano'}
a : apple
b : banana
n : nano

결과2 >>>
{'b': 'banana', 'n': 'nano', 's': 'soup', 'd': 'dress', 'q': 'quit'}
b : banana
n : nano
s : soup
d : dress
q : quit

'''
def dictDefine(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(f'{key} : {kwargs[key]}')
    print()

dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')


# 퀴즈 9
# 첫글자를 제외한 나머지 글자를 '*'로 표시하는
# 람다함수를 정의하여라. 입력되는 문자열은 3글자로 한다.


'''
# 함수 호출 
# f1('홍길동')
# f1('김철수')

결과: >>
홍**
김**
'''

f1= lambda name : print(''.join(list(name[0])), "**")

#강사님 답 ->   f1 = lambda txt:print(txt[0]+'**')
f1('홍길동')
f1('김철수')


# 퀴즈 10
# 국어,영어,수학 3과목의 합과 평균을 구하는
# 람다 함수를 정의하여라
'''
# 람다 호출 
# f2(100,80,90)

결과 >>
국어:100, 영어:80, 수학:90 , 총점:270, 평균90.00

'''
f2 = lambda kor, eng, math : print(f'kor={kor}, eng={eng}, math={math}, sum={kor+eng+math}, avg={(kor+eng+math)/3:.2f}')
#강사님 답 -> f2 = lambda x,y,z:print(f'국어:{x}, 영어:{y}, 수학:{z} , 총점:{x+y+z}, 평균{(x+y+z)/3:.2f}')

f2(100,80,90)
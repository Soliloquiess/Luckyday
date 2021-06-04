#샘플 문자열 만들기 http://www.lipsum.com

sample='''
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.
'''

print(sample)

#특정 문자열 갯수 출력 -> .count(찾고자 하는 문자열)
print("a의 갯수", sample.count('a'))
print("a의 갯수", sample.count('and'))


# 특정 문자열의 시작인덱스 위치 반환
# 1. 문자열변수.find(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 -1 반환
print("첫번쨰 a의 위치값? ", sample.find('a'))
print("첫번쨰 가의 위치값? ", sample.find('가'))

# 2.문자열변수.index(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 에러 발생
print("첫번쨰 a의 위치값? ", sample.index('a'))
'''print("첫번쨰 가의 위치값? ", sample.index('가'))'''


# 문자열 교체하기
# 문자열변수.replace(찾고자하는문자열, 교체문자열)
# are => was
sample_replace = sample.replace("are", "was")
print(sample.count("are"))
print(sample.count("was"))
print(sample_replace.count("are"))
print(sample_replace.count("was"))

print(sample[:100])
print(sample_replace[:100])


# '연결문자'.join(문자열변수)
myWord = 'Python'
print(' * '.join(myWord)) # P * y * t * h * o * n
print('$'.join(myWord[:3])) #P$y$t


# 좌우 공백 제거하기
# 문자열변수.lstrip()
# 문자열변수.rstrip()
# 문자열변수.strip()
myWord = '      Python      '
print('-'*20)
print(f'**{myWord}**')
print(f'**{myWord.rstrip()}**') #right쪽 공백 제거
print(f'**{myWord.lstrip()}**') #left쪽 공백 제거
print(f'**{myWord.strip()}**')



#-----------------------------------------------

# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형
# 집합형 자료형=콜렉션 : 여러개의 구성요소로 조직화
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }

# 빈 리스트  생성
myList = []
print(myList, type(myList)) # [] <class 'list'>

# myList[0] = 100 # IndexError: list assignment index out of range (빈 리스트에 그냥 값을 바로 넣어버리면 오류남)
# 따라서 파이썬은 append 사용해줘야 함. 아이템 추가 = 리스트명.append( 아이템값)
myList.append(100)
myList.append(200)
print(myList)

#데이터형이 달라도 리스트 생성됨
#즉, 서로 다른 데이터형으로 리스트 정의 가능 -> 파이썬 리스트 특징 중 하나
myList2 = ["가나다" , 20, True, False, 34.34545]
print(myList2, type(myList2))

#리스트 인덱싱
#리스트이름[숫자] : 0부터 시작, 숫자값이 -1 마지막 요소 표시
print(myList2[0])


fruites=['바나나', '사과', '귤', '포도', '수박']
print(fruites)
print(fruites[0])
print(fruites[-1])
print(fruites[0:3])
print(fruites[2:])
print(fruites[:3])
print(fruites[::2]) #홀수, 따라서 바나나,귤,수박 출력됨
print(fruites[1::2]) #짝수, 따라서 사과, 포도 출력됨

print('-'*20)

# 리스트 값 변경하기 => Update
# 리스트변수[인덱스] = 값
print(fruites)
fruites[0] = 100
fruites[-1] = 100
print(fruites)

# 리스트 연산
# 리스트1 + 리스트2 : 같이 표시
# 리스트이름*숫자 : 반복
singer = ["블랙핑크", "데이식스", "권진아", "KatyPerry", "Sia", "ColdPlay"]
drama = ["악의꽃", "청춘기록", "착한남자", "공주의남자", "굿닥터"]
print("singer= ", singer)
print("drama= ", drama)
print("singer+drama= ", singer+drama) #그렇다고 원본이 변경되는 건 아님. 출력만 그렇게 보이는 것!

# 리스트 함수
# 리스트변수.함수명(옵션)
# 정의된 리스트에 새로운 값을 추가
food=[]
# 리스트변수.append(값) : 마지막에 아이템이 추가
food.append("쫄면")
food.append("비빔면")
food.append("오므라이스")
food.append("돈까스")
print(f"food = {food}")

# 리스트변수.insert(삽입위치, 값) : 삽입위치에 아이템이 추가, 삽입위치를 인덱스값으로 줘야 함
food.insert(0, "김밥")
print(f"food = {food}")


# 리스트 삭제와 관련된 함수와 명령어
# 리스트변수.remove(값) : 값으로 삭제하기
food.remove('쫄면')
print(f"food = {food}")

# 리스트변수.pop() : 마지막 요소가 삭제되면서 값이 반환된다.
# 리스트변수.pop(위치값)
# : 위치에 해당하는 요소가 삭제되면서 값이 반환된다.
food.pop()
print(f"food = {food}")
food.pop(2)
print(f"food = {food}")

# 리스트변수.clear() : 리스트안의 값이 모두 삭제. 빈리스트 상태가 돔
food.clear()
print(f"food = {food}")

# del 리스트변수 : 리스트 자체가 삭제된다.
del food
#NameError: name 'food' is not defined 리스트 자체가 삭제되서 출력하려하면 에러남
#print(f"food = {food}")



# 리스트 전체 길이 출력
# 리스트 데이터형 출력
# type(리스트변수)
singer = ["블랙핑크", "데이식스", "권진아", "KatyPerry", "Sia", "ColdPlay"]
print(f'singer list: {singer}')

# len(리스트변수)
print(f'singer list length= {len(singer)}')

#입력받은 값으로 리스트 생성
'''
numberList = []
print(f'numberList = {numberList}')
item = input('리스트 아이템1 => ')
numberList.append(item)
print(f'numberList = {numberList}')
numberList.append(input('리스트 아이템2 => '))
print(f'numberList = {numberList}')
'''

# 리스트 값 정렬하기
list1=[10,40,250,35,23,1]
list2=["하나", "둘", "world", "35"]
list3=[10.78, "google", True, 500]

# 1.오름차순 리스트변수.sort() -> 원본 변하기 때문에 sort작업 후 출력
list1.sort()
print(f"sort confirm: {list1}")
list2.sort() #숫자 < 알파벳 < 한글
print(f"sort confirm: {list2}")

# TypeError 발생
# 주의사항은 리스트변수.sort()의 경우
# 리스트를 이루는 구성요소의 데이터형은 같아야한다
#list3.sort()
#print(f"sort confirm: {list3}") #리스트 속 값들의 자료형이 다를경우 sort 오류
#TypeError: '<' not supported between instances of 'str' and 'float'


# 2.내림차순 리스트변수.reverse()
list1.reverse()
print(f"sort confirm: {list1}")
list2.reverse()
print(f"sort confirm: {list2}")
list3.reverse() #오류는 안남 But, 딱 원하는 값은 아닌..
print(f"sort confirm: {list3}")


#점심시간 Yeah ~~~~~


# 리스트변수.count(값)
# 중복값이 몇개인가?
myList3 = [100, 400, 100, 100, True,True, False, "문자열","문자열","문자열","문자열"]
print(f'List3에서 100의 중복횟수= {myList3.count(100)}')
print(f'List3에서 100의 중복횟수= {myList3.count("문자열")}')
print(f'List3에서 100의 중복횟수= {myList3.count(True)}')

# 리스트변수.index(값)
# 값에 해당하는 요소가 몇번째에 위치하고 있는가?
print(f"List3에서 True의 위치={myList3.index(True)}")
print(f'List3에서 문자열의 위치={myList3.index("문자열")}')

# 여러개의 요소를 한꺼번에 리스트에 추가 싶다면?
# 리스트변수.extend([값1,값2...])
myList3.extend(['apple','cat'])
print(f"List3 :{myList3} ")

#========================================================

#Quiz Time
# 퀴즈 1

'''
2개의 리스트를 정의하고 다음과 같이 출력한다.
myList1 : ['홍길동', '신데렐라', '알라딘', '장화',
 '홍련', '지니', '엘리스']
myList2 : ['토끼', '거북이', '물개', '펭귄']
2개의 리스트 합 : (결과값 출력 )
4개만 출력 : (결과값 출력 )
짝수번째만 출력 : (결과값 출력 )
홀수번째만 출력 : (결과값 출력 )
총 길이 :  11
'''

#내 답
arr1= ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
arr2=['토끼', '거북이', '물개', '펭귄']
print(f"arr1 리스트와 arr2리스트 출력: {arr1+arr2}")
print(f"4개만 출력: {arr1[:4]}")
print(f"홀수번쨰만 출력: {arr1[::2]}")
print(f"짝수번쨰만 출력: {arr1[1::2]}")


#강사님 답
myList1 = ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
myList2 = ['토끼', '거북이', '물개', '펭귄']
print(f'myList1 : {myList1}')
print(f'myList2 : {myList2}')
myList3 = myList1+myList2
print(f'2개의 리스트 합 : {myList3}')
print(f'4개만 출력 : {myList3[:4]}')
print(f'짝수번째만 출력 : {myList3[1::2]}')
print(f'홀수번째만 출력 : {myList3[::2]}')
print(f'총 길이 : {len(myList3)}')
print('-'*30,'\n')



# 퀴즈 2
'''
리스트를 정의한 후 리스트 요소를 편집한다.
(변경, 삭제, 추가)
['사과', '배', '망고']
첫번째 요소 변경 후 : ['포도', '배', '망고']
마지막 위치에 요소 추가후 : ['포도', '배', '망고', '오렌지']
2번째 위치에 요소 추가후 : ['포도', '수박', '배', '망고', 
                        '오렌지']
마지막 위치 삭제 : ['포도', '수박', '배', '망고']
배 삭제 : ['포도', '수박', '망고']
'''

#내 답
arr3=['사과', '배', '망고']
arr3[0]='포도'
print(f"arr3 : {arr3}")
arr3.append('오렌지')
print(f"arr3 : {arr3}")
arr3.insert(1,'수박')
print(f"arr3 : {arr3}")
arr3.pop()
print(f"arr3 : {arr3}")
arr3.remove('배')
print(f"arr3 : {arr3}")

#강사님 답
fruitList = ['사과', '배', '망고']
print(f'{fruitList}')
fruitList[0]= '포도'
print(f'첫번째 요소 변경 후 : {fruitList}')
fruitList.append('오렌지')
print(f'마지막 위치에 요소 추가 후 : {fruitList}')
fruitList.insert(1,'수박')
print(f'2번째 위치에 요소 추가 후 : {fruitList}')
fruitList.pop()
print(f'마지막 위치 삭제 : {fruitList}')
fruitList.remove('배')
print(f'배 삭제 : {fruitList}')
print('-'*30,'\n')


# 퀴즈 3
'''
데이터를 입력받은 후 리스트에 추가하는 예제입니다.
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산
당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''

'''
#내 답 
insertData=[]
insertData.append(input("좋아하는 음식:"))
insertData.append(input("최근 본 영화:"))
insertData.append(input("좋아하는 가수:"))
insertData.append(input("좋아하는 숫자:"))
insertData.append(input("최근 여행지:"))

print(f'insertData = {insertData}')


#강사님 답
yourList = []
yourList.append(input('좋아하는 음식은? ... '))
yourList.append(input('최근 본 영화는?  ... '))
yourList.append(input('좋아하는 가수는? ... '))
yourList.append(input('좋아하는 숫자? ... '))
yourList.append(input('최근 여행지? ... '))
print(f'당신에 관한 리스트 : {yourList}')
print('-'*30,'\n')

'''


# 퀴즈 4
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']

'''

#참고로 pop()은 출력문 안에 바로쓸 수 있지만 remove는 X
#ex) print(f"List: " {List.pop()})

#내 답
foodsList = ['사과','망고','치즈케이크','주스']
print(f"우리집 냉장고에는? {foodsList}")
foodsList.remove('사과')
print(f"동생이 사과를 먹었다\n우리집 냉장고에는? {foodsList}")
foodsList.append('수박')
print(f"이모가 수박을 사오셨다\n우리집 냉장고에는? {foodsList}")
foodsList.remove('치즈케이크')
foodsList.remove('수박')
print(f"동생 친구가 치즈케이크,수박을 먹었다. \n우리집 냉장고에는? {foodsList}")


#강사님 답
foods = ['사과','망고','치즈케이크','주스']
print(f'우리집 냉장고에는?  {foods}')
print(f'동생이 {foods.pop(0)}를 먹었다 ')
print(f'우리집 냉장고에는?  {foods}')
foods.append('수박')
print(f'이모가 {foods[-1]}을 사오셨다. ')
print(f'우리집 냉장고에는?  {foods}')
print(f'동생 친구가 {foods.pop(1)},{foods.pop()}을 먹었다. ')
print(f'우리집 냉장고에는?  {foods}')



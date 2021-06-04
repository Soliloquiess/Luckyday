# 캐스팅
# 딕셔너리 => 리스트
# 리스트 => 딕셔너리
# 값만 모아서 리스트로 생성
# list(딕셔너리변수), list(딕셔너리변수. keys()) => 키값만으로 생성된 리스트
# list(딕셔너리변수. values()) => 값으로 생성된 리스트

dic1 = {'a':'apart','s':'say', 'd':'drama', 'c':'camera', 'l':'love'}
print(dic1, type(dic1))

#키값으로 생성된 리스트
result1 = list(dic1)
result2 = dic1.keys()

result3 = list(dic1.values()) #값으로 생성된 리스트

print(f'result = {result1}, type={type(result1)}')
print(f'result = {result2}, type={type(result2)}')
print(f'result = {result3}, type={type(result3)}')





# 리스트 => 딕셔너리(리스트의 위치를 나타내는 인덱싱 숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시


#존재하는 리스트를 딕셔너리로 체인지 하는 과정 (리스트 뿐만 아니라 튜플, 문자열도 가능)
list1 = ['파이썬', '자바', '시플플','스프링','노드제이']
print(f'list1 = {list1} type={type(list1)}')

# 1. enumerate로 압축해제
result1 = enumerate(list1)
print(f'result1 = {result1} type={type(result1)}') #result1 = <enumerate object at 0x000002D0505DA780> type=<class 'enumerate'>

# 2. 압축해제한 걸 dic로 형변환하면 최종적으로 완료
result2 = dict(result1)
print(f'result3 = {result2} type={type(result2)}')

# 3. 위에는 차근히 했지만 한번에 리스트를 딕셔너리로 변환하려면 
list2 = ['한','번','에','변','환']
result3 = dict(enumerate(list2))
print(f'result3 = {result3} type={type(result3)}')

# 딕셔너리 => 문자열
# str(딕셔너리변수) => {...}
# 구분자.join(딕셔너리변수) => 키값으로 생성된 문자열
dict2 = {'a':'apart', 's':'say', 'd':'drama', 'c':'camera', 'y':'yes'}
result1 = str(dict2)
print(f'result1 = {result1} type={type(result1)}')
result2 = '/'.join(dict2)
print(f'result2 = {result2} type={type(result2)}')
# result1 = {'a': 'apart', 's': 'say', 'd': 'drama', 'c': 'camera', 'y': 'yes'} type=<class 'str'>
# result2 = a/s/d/c/y type=<class 'str'>
print(result1[0], len(result1)) # { 67
print(result2[0], len(result2)) # a 9

# 딕셔너리 => 튜플
# tuple(딕셔너리) => 키값으로 구성된 튜플 생성
# 딕셔너리 키값또는 값으로 이루어진 튜플 생성
print(f'dict2 = {dict2} type={type(dict2)}')
print(tuple(dict2))
print(tuple(dict2.values()))
# dict2 = {'a': 'apart', 's': 'say', 'd': 'drama', 'c': 'camera', 'y': 'yes'} type=<class 'dict'>
# ('a', 's', 'd', 'c', 'y')
# ('apart', 'say', 'drama', 'camera', 'yes')


# 딕셔너리 리스트
# 리스트안에 딕셔너리가 있는 구조
dictList = [{'a':'apple', 'v':'victory'},
            {100:'백', 200:'이백'},
            {'user1':'김철수', 'user2':'고소영'}]
print(dictList, type(dictList), len(dictList))
# [{'a': 'apple', 'v': 'victory'}, {100: '백', 200: '이백'}, {'user1': '김철수', 'user2': '고소영'}] <class 'list'> 3

# 딕셔너리 리스트 인덱싱
# 딕셔너리리스트명[위치인덱스][키]
print(dictList[0], type(dictList[0]))
# {'a': 'apple', 'v': 'victory'} <class 'dict'>
print(dictList[0]['a'], type(dictList[0]['a']))

# print(dictList[0][0], type(dictList[0][0]))는 KeyError: 0 에러남





# 집합 {값1, 값2, 값3....}

# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
set1 = {100,200,300,400}
set2 = {'가','나','다','라'}

# " set은 순서가 없기 때문에 랜덤하게 출력된다 "
# set1 = {200, 100, 400, 300} , type=<class 'set'>
# set2 = {'가', '라', '다', '나'} , type=<class 'set'>
print(f'set1 = {set1} , type={type(set1)}')
print(f'set2 = {set2} , type={type(set2)}')

#빈 집합 만들기
set3 = set({}) #이렇게 하지 않고 그냥 set={}으로 하면 딕셔너리 타입. 따라서 빈 집합은 set({})으로 생성하자
print(f'set2 = {set3} , type={type(set3)}')

#집합은 순서가 없기 때문에 Read로 전체조회만 가능 (인덱싱, 슬라이싱 X)
# "가장 큰 특징은 중복값 불가" 따라서 중복값이 있다면 하나만 출력
set4 = {1,2,56,78,90,100,1,1,56,6,56}
print(f'set2 = {set4} , type={type(set4)}, length={len(set4)}')

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])
set3 = set('')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.add('오렌지')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.update(['바나나', '사과', '감자'])
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')

# 집합의 요소 삭제
# 집합변수.remove(값)
# del 집합변수 => 메모리에서 삭제
set3.remove('사과')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.clear()
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
del set3 #완전삭제라 출력하려고 하면 오류남


# 집합의 연산
# +, * => 불가능
set1={90,6,7,55,4}
set2={55,4,77,100,200}

# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1 | 집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)
print(set1,set2)
print(set1|set2)
print(set1.union(set2))

# 차집합
# 집합변수3 = 집합변수1 - 집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)
print(set1-set2)
print(set1.difference(set2))
print(set2-set1)
print(set2.difference(set1))

# 교집합
# 집합변수3 = 집합변수1 & 집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)
print(set1&set2)
print(set1.intersection(set2))

# 캐스팅
# 집합 => 리스트, 튜플, 딕셔너리
set5 = set('도레미파솔라시도')
print(list(set5), type(list(set5)))
print(tuple(set5), type(tuple(set5)))
#result = dict(enumerate(set5))
#print(result, type(result))
print(dict(enumerate(set5)), type(dict(enumerate(set5))))


# 리스트,문자열,튜플 => 집합
# set(리스트,문자열,튜플)

# 집합 => 튜플





# 퀴즈
# 1. a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과
# 마지막 튜플값을 출력하여라.
tuple1 = ('a', 'b', 'c', 'd', 'e')
print(tuple1[0],tuple1[-1])

#강사님 답
myTuple = ('a', 'b', 'c', 'd', 'e')
print('myTuple = {0}'.format(myTuple))
print('myTuple[0] = {0}, myTuple[-1] = {1}'.format(myTuple[0], myTuple[-1]))



# 2. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
fruit = ["Banana", "Apple", "Orange"]
fruit.remove("Apple")
print(fruit)

#강사님 답
fruits = ["Banana", "Apple", "Orange"]
print(f'fruits = {fruits}')
fruits.remove("Apple" )
print(f'fruits = {fruits}')



# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding0' 데이터를 첫번째에 추가하고,
#    다시 튜플 데이터로 변환하여라.
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
tuplechange = list(tupledata)
print(tuplechange, type(tuplechange))
tuplechange.insert(0,'fun-coding0')
print(tuple(tuplechange), type(tuple(tuplechange)))


#강사님 답
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
print(f'tupledata = {tupledata}')
temp = list(tupledata)
temp.insert(0, 'fun-coding0' )
print(f'temp = {temp}')
tupledata = tuple(temp)
print(f'tupledata = {tupledata}')


# 4. 다음 항목을 딕셔너리(dict)으로 선언하여라.
# : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
charge ={'성인':10000, '청소년':70000, "아동":30000}
print(charge)

#강사님 답
fare = {'성인':100000 , '청소년':70000 , '아동':30000}
print(f'fare = {fare}')



# 5. 4번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
charge["소아"] = 0
print(charge)

#강사님 답
fare['소아'] = 0
print(f'fare = {fare}')



# 6. 5번의 딕셔너리(dict)에서 Key 항목만 리스트로 저장하여 정렬한 후 튜플로 변경하여라.
#  결과 => ('성인', '소아', '아동', '청소년')
charge_list = list(charge.keys())
print(tuple(charge_list), type(tuple(charge_list)))

#강사님 답
temp = list(fare)
print(temp)
temp.sort()
print(temp)
print('결과 => ' , tuple(temp))



# 7. number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
#  number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
print(list(set(number_list)))

#강사님 답
number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
print('-'*20)
print(number_list)
print(list(set(number_list)))



# 8. 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}

set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}

print(f'두 집합의 중복값 리스트 = {list(set1&set2)}, type={type(list(set1&set2))}')


#강사님 답
set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '월E', '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
result = list(set1 & set2)
print('-'*20)
print(result)





# 9. 8의 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
#  아이템1 / 아이템2 / ....
list_hop = str(set1|set2)

#강사님 답
print( ' / '.join(result))




# 10. 빈 집합을 생성하고 값을 입력받아 집합의 원소를 삽입하여라. 집합 원소의 갯수는 5개로 한다.
'''
 mySet = set() <class 'set'>
첫번째 아이템 값 => 갈비탕 
두번째 아이템 값 => 소머리국밥
세번째 아이템 값 => 삼계탕
네번째 아이템 값 => 순두부
다섯번째 아이템 값 => 김치찌게
 mySet = {'김치찌게', '소머리국밥', '갈비탕 ', '순두부', '삼계탕'} <class 'set'>
'''
# nullset = set({})
# nullset.add(input("첫번쨰 아이템 값=>"))
# nullset.add(input("두번쨰 아이템 값=>"))
# nullset.add(input("세번쨰 아이템 값=>"))
# nullset.add(input("네번쨰 아이템 값=>"))
# nullset.add(input("다섯번쨰 아이템 값=>"))
# print(nullset, type(nullset))

#강사님 답
'''
mySet = set([])
print('-'*20)
print( ' mySet ', mySet, type(mySet))
mySet.add(input('첫번째 아이템 값 => '))
mySet.add(input('두번째 아이템 값 => '))
mySet.add(input('세번째 아이템 값 => '))
mySet.add(input('네번째 아이템 값 => '))
mySet.add(input('다섯번째 아이템 값 => '))
print( ' mySet = ', mySet, type(mySet))
'''


# 11. 10의 집합을 다음과 같은 딕셔너리 구조로 변환하여라.
#     ?는 10의 집합값이다.
#  mydict =  {0: '소머리국밥', 1: '갈비탕', 2: '순두부', 3: '김치찌게', 4: '삼계탕'}
#  <class 'dict'>

#print(dict(enumerate(nullset)), type(dict(enumerate(nullset))))

#강사님 답
'''
mydict = dict(enumerate(mySet))
print('-'*20)
print( ' mydict = ', mydict, type(mydict))
'''
'''  11.17(TUE) 오후수업 '''

'''
    * 정규표현식 패턴 - 대문자, 소문자, 숫자 : \지원문자
      [문자클래스스타일]  => 한글씩
      [문자클래스스타일]+ => 단어단위
      [a-z] : 영어소문자
      [A-Z] : 영어대문자
      [0-9] : 숫자
      [가-흫] / [가-힣]: 한글
    
      [\d] : 10진수, [0-9]와같음
      [\D]: 10진수외 [^0-9]
      [\s] :공백문자, [ \t\n\r\f\v]
      [\S]: 공백 문자 외, [ \t\n\r\f\v]
      [\w] : 영문자숫자 , [a-zA-Z0-9]
      [\W]: 영문자숫자외 , [^a-zA-Z0-9]
    
    *  패턴식 메타문자
      ^:문자열의 처음을 나타냄
      $:문자열의 끝
'''

import re

sample1 = "123 **%43    도레미솔솔   word    강아지!!!  음악12345   C#   Python"
# 다중 라인 문자열 ''' , """ /n, '', '/t'
sample2 = '''도레미솔솔
            우리나라 
            anbvf
            123456 '''
print(re.findall('[\W]', sample1)) #영문자, 숫자 외
print(re.findall('[\W]', sample2)) 
print(re.findall('[\w]+', sample1)) #영문자,숫자
print(re.findall('[\w]+', sample2))


# 비밀번호 유효성 검사 
# 비밀번호 조건 -> 전체길이 6~12, 영어대소문자 or 숫자로만 구성
def checkPwd(pwd):
    if 6 <= len(pwd) <= 12:
        result = re.findall('[a-zA-Z0-9]', pwd)
        if len(result) == len(pwd):
            print(f' "{pwd}"\t\t비밀번호 생성 완료')
        else:
            print(f' "{pwd}"\t\t영어대소문자와 숫자만가능')
    else:
        print(f' "{pwd}"\t\t비밀번호 길이가 적당하지 않다.')
checkPwd('abcd')
checkPwd('abcdhgj000')
checkPwd('ab강아지j000')
checkPwd('a@bcj0-0')
checkPwd('12   35 ***    789')
checkPwd('a가나다라마')
checkPwd('wordpython0000000')




print('-'*50)
'''
    * 자릿수 지정 패턴 {} : 
    - [문자열]{n} n번 반복됨
             {n,} n번 이상 반복
             {n, m} 최소 n번 이상 최대 m 번 이하로 반복
             x* : 문자열X가 0번이상 반복
'''

str = "abc 00ab 000cd 00000python 0123400!!! 0000가나다 0도레미"

# [문자열]{n}
print(re.findall('[0]{2}[a-zA-Z]+', str)) # 0이 2번나오고 영어대소문자인 값 찾기 => ['00ab', '00cd', '00python']
print(re.findall('[0]{3}[a-zA-Z]+', str)) # 0이 3번나오고 영어대소문자인 값 찾기 => ['000cd', '000python']
print(re.findall('[0]{4}[a-zA-Z]+', str)) # 0이 4번나오고 영어대소문자인 값 찾기 => ['0000python']
print(re.findall('[0]{4}[a-zA-Z가-힣]+', str)) # 0이 4번나오고 (영어대소문자+한글) 값 찾기 => ['0000python', '0000가나다']

# {n,} n번 이상 반복됨
print(re.findall('[0]{1,}[a-zA-Z가-힣]+', str))
# 0이 1개 이상 + 영어대소문자 => ['00ab', '000cd', '00000python', '0000가나다', '0도레미']

# {n, m} n~m 이상 반복됨
print(re.findall('[0]{2,4}[a-zA-Z가-힣]+', str))
# 0이 2개 이상 4개이하 + 영어대소문자 => ['00ab', '000cd', '0000python', '0000가나다']


# 휴대폰번호 유효성검사
txt = '''010-7777-1234 00-6785-가나다 
        011-5678-8989 01156788989
        333-123 abc-9990-0000 554-8488-7878 
        045-5678-4567 016-8888-9090
        017-7785-7775 010-7777-9999 
        010-!!!!-abcd '''


# 패턴1
# 숫자3자리-숫자4자리-숫자4자리
# [0-9]{3}-[0-9]{4}-[0-9]{4}

# 010-숫자4자리-숫자4자리
# 010-[0-9]{4}-[0-9]{4}

#  | : OR 또는
# 숫자3자리(010/011/016/017)-숫자4자리-숫자4자리
# 01[0|1|6|7]-[0-9]{4}-[0-9]{4}

print(re.findall('[0-9]{3}-[0-9]{4}-[0-9]{4}', txt))
# ['010-7777-1234', '011-5678-8989', '554-8488-7878', '045-5678-4567', '016-8888-9090', '017-7785-7775']
print(re.findall('010-[0-9]{4}-[0-9]{4}', txt))
# ['010-7777-1234', '010-7777-9999']
print(re.findall('01[0|1|6|7]-[0-9]{4}-[0-9]{4}', txt))
# ['010-7777-1234', '011-5678-8989', '016-8888-9090', '017-7785-7775', '010-7777-9999']




# 패턴2 : 숫자6자리-숫자1자리(1|2|3|4)숫자6자리
# [0-9]{6}-[1|2|3|4]{1}[0-9]{6}

quizList = [ '020-28261', '564873-3300998',
'가나다-3300998', '564873-8800998',
'123456-1234567', 'abc456-1234567',
'5555564873-3377777700998', '564873-1234567890' ]

print('*'*50)
pat2 = '[0-9]{6}-[1|2|3|4]{1}[0-9]{6}'
for item in quizList:
    if len(item) == 14:
        # print(item, ' => ', re.search(pat2, item))
        result = re.search(pat2, item)
        if result:
            print(result.group())
print('-'*50)


# ----------------------------------------
'''
    * 그룹핑 이용: 다 되는건 아니고 주로 match나 search object에서 사용
                 정규표현식의 패턴을 그룹화, group(index): index 1부터 시작
    ex) 패턴식 = '(패턴문자열1)-(패턴문자열2)....'
    - re.match(패턴식, 대상문자열).group()
    - re.match(패턴식, 대상문자열).group(index)
    - re.search(패턴식, 대상문자열).group()
    - re.search(패턴식, 대상문자열).group(index)
'''
juminPattern = '([0-9]{6})-([1|2|3|4][0-9]{6})'
result = re.match(juminPattern, '123456-1234567')
print(result) # <re.Match object; span=(0, 14), match='123456-1234567'>
print(result.group()) #123456-1234567
print(result.group(1)) #123456
print(result.group(2)) #1234567


# 퀴즈 : 주민번호데이타에서 주민번호뒷자리 '*******' 패턴 그룹핑 이용해 마킹하기
quizList = [ '020-28261', '564873-3300998',
'가나다-3300998', '564873-8800998',
'123456-1234567', 'abc456-1234567',
'5555564873-3377777700998', '564873-1234567890' ]

pat2 = '([0-9]{6})-([1|2|3|4]{1})([0-9]{6})'
for item in quizList:
    if len(item) == 14:
        result = re.search(pat2, item)
        if result:
            print(result.group(1),'-','*'*7)
            print(result.group(1), '-', result.group(2), '*'*6)


# 정규표현식 퀴즈1
# 다음 리스트에서 '가'로 시작하는 아이템만 결과 리스트로 저장하고
# 출력하여라
# 단, 다음 패턴변수를 이용하여라.
quiz1List = ['가나', '라일락', '가지', '망아지', '강아지',
             '국화', '가로수', '도라지', '화수분']
find_ga = re.compile('^가')
start_ga = [item for item in quiz1List if find_ga.findall(item)]
print(start_ga)


# 정규표현식 퀴즈2
# 다음 리스트에서 '지'로 끝나는 아이템만 출력하여라
# 단 패턴식.정규표현식메소드 방식을 이용하여라.
quiz2List = ['가나', '라일락', '가지', '망아지', '강아지',
             '국화', '가로수', '도라지', '화수분']
find_ji = re.compile('지$')
last_ji = [item for item in quiz2List if find_ji.findall(item)]
print(last_ji)

# 정규표현식 퀴즈3
# 다음 문자열에서 한글로만 구성된 단어를 리스트로 생성하고 총 갯수를 구하여라.
# 단 re.정규표현식메소드 방식을 이용하여라.

'''
*** 퀴즈3 문제 풀이 ***
['구름', '사랑', '도련님', '그림자']
총갯수 =  4
'''
txt = '구름 1004 사랑 도련님 word python 그림자 34친구 JAVA 썬크림345 67마스7878'
txtList = txt.split()
# print(txtList)
for i in txt.split():
    # 숫자가 들어가거나 알파벳이 들어가면 리스트에서 삭제
    if re.findall('[0-9]|[a-zA-Z]', i):
        txtList.remove(i)
print(f'{txtList}\n총 갯수 = {len(txtList)}')

# 정규표현식 퀴즈4
# 다음 리스트에서 숫자가 4번 이상으로 구성되어 있는 리스트 아이템만 출력하여라.
'''
가나12345
%%1234가나다라
파이썬567890
1234
'''
print('*-'*50)
quizList = ['12가나다', '가나12345', 'banana45', '가나12banana567', '34',
            '%%1234가나다라', '파이썬12', '파이썬567890', '1234']

pattern = '[0-9]{4,}'
for i in quizList:
    temp = re.findall(pattern,i)
    # print(temp)
    if temp:
        print(i)

print('-'*60)
for i in quizList:
    temp = re.finditer(pattern, i)
    for j in temp:
        if j.group():
            print(i)



result = []
for item in quizList:
    if re.search('[\d]{4,}', item):
        result.append(item)
print(result)

print('*-'*50)
# 정규표현식 퀴즈5
# 다음 리스트에서 핸드폰 패턴에 맞는 데이타만  0??-****-****
# 스타일로 출력하여라
'''
['010-7777-1234', '011-5678-8989', '554-8488-7878', '045-5678-4567', 
        '016-8888-9090', '017-7785-7775']
'''
data = ['010-7777-1234', '011-5678-8989', '554-8488-7878', '045-5678-4567',
        '016-8888-9090', '017-7785-7775']

mobilePattern = '(01[0|1|6|7])-([0-9]{4})-([0-9]{4})'
for item in data:
    result = re.match(mobilePattern, item)
    if result:
        print(f'{result.group(1)}-{result.group(2)[0]}***-****')
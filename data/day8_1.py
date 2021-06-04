''' 11월 16일 (MON) 오전수업 '''
'''
    * 오류 종류 (Error Code -> Errror Message e)
    - SyntaxError   ex) Print('ddd)
    - NameError
    - IndexError
    - ZeroDivisionError : 0으로 나눈 경우
    - FileNotFoundError : 잘못된 파일 경로
    - ValueError 
    - TypeError 
    
    * 예외처리 : 에러 발생 시 그 아래의 명령 실행되지 않음
'''

# 에러처리 문법 1 (에러코드 알고 있어야 함)
# try..except 에러코드 as e: 에러처리명령
# try: 명령어 except 에러코드 as e: 에러처리명령
myList = [1, 100, 80, 90]
try:
    print(myList[0])
    print(myList[10])
    print(myList[1])
    print(myList[2])
    print(myList[-1])
except IndexError as e:  # e는 에러메세지 출력시 사용 
    print(f'에러메세지 - {e}')



# try..except 명령2 (에러코드 몰라도 됨, Exception으로 퉁침)
# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# try: 명령 except Exception as e: rint(e)
num1 = 10
# num2 = 0
num2 = 5
try:
    result = num1/num2
    print(result)
    print(result2)
# except ZeroDivisionError as e:
except Exception as e:
    print(f'에러메세지 - {e}')



# try..except 명령3 (에러메세지 e 출력 X)
# try: 명령어 except: 에러처리명령
# ex) 파일입출력과 관련된 에러 발생 후 명령어 처리
try:
    with open('도레미.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
except:
    #print('그런 파일 없습니다.')
    pass #에러 자체를 무시
print('-'*50)

'''
    try:
        명령어1
        명령어2
    except:
    except 오류코드 as e:
    except Exception as e:
        에러처리 명령어
        pass
'''



''' QUIZ TIME

# 퀴즈 1 FileNotFoundError
#  data/test.txt 가 없다면 에러메세지(e)와 함께
#  '파일이 없습니다.' 메세지 출력 있다면 파일의 내용 출력
try:
    with open('data/test.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
except Exception as e:
    print(e,'파일이 없습니다')




# 퀴즈 2,  ValueError
# 2개의 숫자글자를 입력받아서 더함.
# 입력된 글자가 숫자글자가 아니라면 에러 메세지 출력
# 입력된 글자가 숫자글자라면  더한후 출력한다.
try:
    a,b = input('첫번째 숫자 입력=>'), input('두번째 숫자 입력=>')
    print(f'{a} + {b} = {int(a+b)} ')
except ValueError as e:
    print('입력하신 글자는 숫자형이 아닙니다 =>',e)
'''


'''
    try: ... except:... else:... finally:... (else, finally는 생략 가능) 
    try: 명령어
    except 에러코드 as e:
    except Eception as e:
    except:
      에러처리명령
    else:
      에러가 발생하기 않은 경우 명령어
    finally:
      무조건 실행되는 명령어
'''

try:
    # 파일 없는 경우 TEST
    f = open ('data/test.txt', 'r',encoding='utf-8')

    # 파일 있는 경우 TEST
    #f = open ('data/yesterday.txt', 'r',encoding='utf-8')

except Exception as e:
    print(f'파일이 없어요 \n\t\t {e}')
else:
    print(f.readline())
    f.close()
finally:
    print('파일읽기 TEST CLOSED')


print()


''' 여러개의 에러메시지 처리    '''
try:
    # myNumber = 77
    print(myNumber)
    print(800 / 0)
except ZeroDivisionError as e:
    print(f'0으로 나누는 경우의 에러 : 에러메세지 - {e}')
except NameError as e:
    print(f'정의되지 않은 변수 에러 : 에러메세지 - {e}')
finally:
    print('테스트종료')


print()


# 정의되지 않은 변수 에러 : 에러메세지 - name 'myNumber' is not defined
# 테스트종료
try:
    myNumber = 77
    print(myNumber)
    print(800 / 0)
except ZeroDivisionError as e:
    print(f'0으로 나누는 경우의 에러 : 에러메세지 - {e}')
except NameError as e:
    print(f'정의되지 않은 변수 에러 : 에러메세지 - {e}')
finally:
    print('테스트종료\n')

# 0으로 나누는 경우의 에러 : 에러메세지 - division by zero
# 테스트종료



'''
    사용자 정의 에러 (raise문 이용)
    - if 조건식 raise Exception (오류메시지)

'''

# ex) 변수값 음수 => 에러발생
x = 0
if x < 0:
    raise Exception('x는 양수이거나 0이어야 함')
elif x == 0:
    print('x는 0')
else:
    print('x는 양수')
    

# 위 예제 "try + raise구문" 으로 change
x = -10
try:
    if x < 0:
        raise Exception('x는 양수이거나 0이어야한다.')
    elif x==0:
        print('x는 0')
    else:
        print('x는 양수')
except Exception as e:
    print('Error Test:', e)
    
'''
# ex) 금칙어 에러
exceptWord = ['바보', '멍청이', '예쁜이' ]
nickname = input('닉네임 입력 => ').strip()
if nickname in exceptWord:
    raise Exception('금칙어, 닉네임으로 사용 불가')
else:
    print(f'당신의 닉네임은 {nickname}\n환영합니다 {nickname}님')

#try except 이용
try:
    nickName = input('닉네임을 입력해주세요...').strip()
    if nickName in exceptWord:
        raise Exception('금칙어, 닉네임으로 사용 불가')
except Exception as e:
    print(f' 에러메세지 - {e}')
else:
    print(f'당신의 닉네임은 {nickName}')
    print(f'환영합니다 {nickName} 님')
finally:
    print('--- 닉네임 테스트 종료--- ')
'''


'''
퀴즈 TIME
'''
# 퀴즈 3 : ValueError, ZeroDivisionError
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?
def division_num():
    try:
        a,b = int(input('1 숫자 입력 -')), int(input('1 숫자 입력 -'))
    except Exception as e:
        print('데이터 오류 ', e)
    else:
        print(f'{a}/{b}={a/b}')

#division_num()


#강사님 답
def plusNum():
    try:
        num1 = int(input('첫번째 값을 입력하세요...'))
        num2 = int(input('두번째 값을 입력하세요...'))
        result = num1/num2

    except ZeroDivisionError as e:
        print(f'ZeroDivisionError 데이타 오류 ... - {e}')
    except ValueError as e:
        print(f'ValueError 데이타 오류 ... - {e}')
    else:
        print(f'{num1} / {num2} = {result}')

#plusNum()


# 퀴즈 4
# data_eng.txt 파일을 파일 변수로 저장한다.
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.
try:
    f = open('data/data_eng.txt', 'r', encoding='utf-8')
except Exception as e:
    print(f'파일 없음 => {e}')
else:
    data = ''.join(f.readlines()).split()
    print(data)
    sum= 0
    for item in data:
        sum += int(item)
    print(f'총합=> {sum}, 평균=> {sum/len(data)}')
    f.close()

# 강사님 답
    def total_avg(url, op):
        try:
            sum = 0
            with open(url, 'r', encoding=op) as f:
                data_list = f.readlines()
                for item in data_list:
                    sum += int(item)
                print(f'sum={sum}')
                print(f'avg={sum / len(data_list)}')
        except:
            print('파일 없음')


    #total_avg('data_eng.txt', 'cp949')
    print('-' * 70)
    #total_avg('data/data_eng.txt', 'cp949')

# 다른 분 답
    try:
        sum=0
        i=0
        with open('data/data_eng.txt','r',encoding='cp949') as f:
            for item in f.readlines():
                sum+=int(item)
                i+=1
            print(f'총합 : {sum}\n평균 : {sum/i}')
    except FileNotFoundError as e:
        print('파일 없음.')


# 퀴즈 5
# 매개변수값에 따라 다음과 같은 메세지를 출력한다.
# 0과 같거나 0보다 작다
# 0보다 크다
# 매개변수값이 숫자가 아닌경우에는 오류를 무시하도록
# try...except 문을 작성하여라
def errorText():
    try:
        x = int(input('매개변수 값 입력->'))
    except Exception:
        pass
    else:
        if x <= 0:
            print(f'입력한 "{x}"값은 0보다 같거나 작다')
        else:
            print(f'입력한 "{x}"값은 0보다 크다')
errorText()


# 퀴즈6
# 학생의 학년을 저장하는 변수 classYear값은
# 1학년, 2학년, 3학년, 4학년 이어야한다.
# 나머지 값은  raise Exception 을
# 이용하여 오류를 발생시켜라
classYear=['1학년','2학년','3학년','4학년']
if classYear not in ('1학년','2학년','3학년','4학년'):
    raise Exception('1-4학년이 존재하지 않습니다')
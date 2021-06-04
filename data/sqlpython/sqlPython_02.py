import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb', charset='utf8')
cursor = conn.cursor()

# 퀴즈 1:
# buyTbl에서 2열만 출력하기
cursor.execute('SELECT * FROM buyTbl')
result = cursor.fetchall();
for i in range(len(result)):
    print(result[i][1], ' ', end="")

print()
# 퀴즈 2:
# buyTbl에서 마지막행만 출력하기
print(result[-1])

# 퀴즈 3:
# buyTbl에서 3행3열의 값 출력하기
print(result[2][2])

# 퀴즈 4:
# userTbl에서 지역(addr)값이 '서울'인 레코드만 표시하기
cursor.execute("SELECT * FROM userTbl WHERE addr = '서울'")
userResult = cursor.fetchall()
for item in userResult:
    print(item)

cursor.execute("select count(*) from userTbl where addr='서울';")
result = cursor.fetchone()
print('총',result[0],'개') # ((4,),)


# 퀴즈 5:
# buyTbl에서 아이디(uesrID)값이 'KBS'인 레코드만 표시하기
cursor.execute("SELECT * FROM buyTbl WHERE userID = 'KBS'")
buyResult = cursor.fetchall()
print(buyResult)

conn.close()
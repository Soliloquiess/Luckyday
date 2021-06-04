import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb', charset='utf8')

# "딕셔너리 리스트 구조" 커서 생성
cursor = conn.cursor(p.cursors.DictCursor)
cursor.execute('SELECT * FROM userTbl;')
result = cursor.fetchall()
print(type(result[0]), result) #list 안 dict 구조


# 딕셔너리 키로 호출해 출력
for row in result:
    print('='*30)
    print('회원 아이디 => ', row['userID'])
    print('회원 이  름 => ', row['name'])
    print('회원 주  소 => ', row['addr'])

conn.close()

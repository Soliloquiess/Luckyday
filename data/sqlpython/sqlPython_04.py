import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb2', charset='utf8')
cursor = conn.cursor()

# cursor.execute('''
#                CREATE TABLE bookTbl(
#                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#                title text NOT NULL,
#                writer VARCHAR(30) NOT NULL,
#                page INT NOT NULL,
#                price INT NOT NULL
#                );
# ''')

'''
# 레코드 삽입 1 : 필드명 지정 X
#  INSERT INTO 테이블명 VALUES(..,..,...);

cursor.execute("INSERT INTO bookTbl VALUES(NULL, '점프투파이썬', '박응용', 500, 30000);")
# 실제 DB에 반영
conn.commit()
'''


"""
# 레코드 삽입 2 : 필드명 지정 O
#  INSERT INTO 테이블명 (필드명1,...) VALUES(값1,..,...);
#  sql변수 = '''  INSERT INTO 테이블명 (필드명1,...) VALUES (%s, .... ); '''
# cursor.execute(sql변수, (값1, ... ))

 sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
 cursor.execute(sql, ('이것이 FLASK이다','김플라',600,32000))
 cursor.execute(sql, ('이것이 JAVA이다','김자바',700,27000))
 conn.commit()
"""

"""
# 레코드 삽입 3 : 필드명 지정 O , 다중레코더 삽입 방식 (데이터가 튜플로 들어감)

# INSERT INTO 테이블명 (필드명 1, ...) VALUES (값 1, ...);
# SQL변수= '''INSERT INTO 테이블명 (필드명 1,...) VALUESE (값1, ...);'''
# 레코드 데이타를 2차원 튜플로 저장 => data = ( (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...) ...)
# cursor.executemany( sql변수, data )
sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
data = (('이것이 수업이다', '신수업', 450, 25000),
        ('이것이 연기다', '문채원', 250, 31000),
        ('이것이 백수다', '진백수', 150, 19000))
cursor.executemany(sql, data)
conn.commit()
"""




# 퀴즈 : input() 문을 이용해서 값을 입력받아 bookTbl 테이블의 레코드로 삽입해 보기
'''
레코드 삽입 
----------
책이름 => ?
저자 => ?
페이지수 => ?
가격 => ?

----------
레코드 출력 (조건-마지막에 삽입한 레코드가 첫번째로 나오게) 
'''

# my answer ===============
# 레코드 삽입
def insertval():
    title, writer, page, price = input('책 제목 입력=>'), input('책 저자 입력=>'), input('책 페이지 입력=>'), input('책 가격 입력=>')
    sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()

# 역순 결과 확인
def reverse_print():
    cursor.execute('SELECT * FROM bookTbl;')
    result = cursor.fetchall()
    for item in reversed(result):
        print(item)

insertval()
reverse_print()

# 강사님은 sql문 이용해 역순으로 출력하심
# cursor.execute('SELECT * FROM bookTBL ORDER BY id DESC;')

print('-'*30)
conn.close()

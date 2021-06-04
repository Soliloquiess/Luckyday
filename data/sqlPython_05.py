import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb', charset='utf8')
cursor = conn.cursor()


# sample data check
"""
cursor.execute("SELECT * FROM buyTbl_sample")
result = cursor.fetchall()
for item in result:
    print(item)
"""



# values modify
# buytbl_sample 테이블에서 1번 레코드의 상품명(prodName) 수정
"""
sql = '''  UPDATE buytbl_sample  
           SET prodname = %s  WHERE num = %s; '''
cursor.execute(sql, ('백팩', 1))
conn.commit()
"""


# values delete
"""
sql = ''' DELETE FROM buyTbl_sample WHERE num = %s; '''
cursor.execute(sql, 2)
conn.commit()
"""

cursor.execute('SELECT * FROM buytbl_sample')
result = cursor.fetchall()
for item in result:
    print(item)


print('-'*30)
conn.close()

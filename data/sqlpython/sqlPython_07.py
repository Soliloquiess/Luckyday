import pymysql as p
conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                 db='sqldb2', charset='utf8')
cursor = conn.cursor()

''' 책 관리 프로그램 =>  pymysql로 DB연동 후 조회,추가,수정,삭제 작업 '''
# 목록보기 함수
def showBook():
    # pass
    print('-'*40, '\n', 'BOOK LIST ▼▼ \n')
    cursor.execute("SELECT * FROM bookTbl;")
    result = cursor.fetchall()
    for row in result:
        print(row)
    print('-'*40, '\n')

# 데이터 추가 함수
def insertBook():
    title, writer, page, price = input('책 제목 입력=>'), input('책 저자 입력=>'), input('책 페이지 입력=>'), input('책 가격 입력=>')
    sql = 'INSERT INTO bookTbl(title, writer, page, price) VALUES (%s, %s, %s, %s);'
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()
    print('\n레코드가 삽입됐습니다')
    print('-' * 40, '\n')


# 데이터 수정 함수
def updateBook():
    print('-' * 40)
    updatenum = input('수정할 책 번호는 => ')

    list(updatenum)

    updatecolumn = input('수정할 컬럼 선택 (1.책제목  2.저자  3.페이지수  4.가격)\n=> ')
    bvalue = input('변경값 입력\n=>')

    if updatecolumn == '1':
        sql = 'UPDATE bookTbl SET title = %s where id = %s;'
        cursor.execute(sql, (bvalue, updatenum))
    elif updatecolumn == '2':
        sql = 'UPDATE bookTbl SET writer = %s where id = %s;'
        cursor.execute(sql, (bvalue, updatenum))
    elif updatecolumn == '3':
        sql = 'UPDATE bookTbl SET page = %s where id = %s;'
        cursor.execute(sql, (bvalue, updatenum))
    elif updatecolumn == '4':
        sql = 'UPDATE bookTbl SET price = %s where id = %s;'
        cursor.execute(sql, (bvalue, updatenum))

    conn.commit()

    list(updatenum)
    print('레코드가 수정됐습니다\n')


def list(updatenum):
    print('-' * 40)
    sql = "SELECT * FROM bookTbl WHERE id = %s;"
    cursor.execute(sql, updatenum)
    pick_book = cursor.fetchall()
    print(f'1.책제목 : {pick_book[0][1]}\n2.저자 : {pick_book[0][2]}\n'
          f'3.페이지수 : {pick_book[0][3]}\n4.가격 : {pick_book[0][4]}')
    print('-' * 40)


# 데이터 삭제 함수
def deleteBook():
    sql = 'DELETE FROM bookTbl WHERE id = %s;'
    cursor.execute(sql, input('삭제할 책 번호를 입력하세요=>'))
    conn.commit()
    print('해당 번호의 레코드가 삭제됐습니다')
    print('-' * 40, '\n')

# main MENU
def main():
    while(True):
        choice = int(input('1.목록보기  2.추가  3.수정  4.삭제  0.종료\n  =>'))
        if choice == 1:
            showBook()
        elif choice == 2:
            insertBook()
        elif choice == 3:
            updateBook()
        elif choice == 4:
            deleteBook()
        elif choice == 0:
            print('프로그램을 종료합니다')
            break
main()
conn.close()

/* 11.23(MON) 수업*/

-- 특정 부분만 표시하기 
-- LEFT(문자열, 길이), RIGHT(문자열, 길이) : 왼쪽이나 오른쪽을 기준으로 길이만큼 잘라서 표시 
-- SUBSTRING(문자열, 시작위치, 길이) : 시작위치에서 길이만큼 잘라서 표시한다 (시작위치 인덱스 1부터 시작) 
-- LENGTH(문자열) : 문자열 길이 반환
SET @sample = 'abcdefghijk';
SELECT @sample, LEFT(@sample,3), RIGHT(@sample,3), SUBSTRING(@sample,3,4), LENGTH(@sample);

-- 연락처 ???-????-????
SELECT * FROM usertbl;
SELECT  CONCAT(SUBSTRING(name,1,1),'**') AS '회원명',
      CONCAT(mobile1,'-',LEFT(mobile2,4),'-',RIGHT(mobile2,4)) AS '연락처'
FROM usertbl;

-- LPAD(문자열, 길이, 채울문자열), RPAD(문자열, 길이, 채울문자열) : 왼쪽이나 오른쪽에 길이만큼 늘려 문자열을 채운다.
-- REPEAT(문자열, 반복횟수) : 문자열을 횟수만큼 반복한다.
SET @userName1 = '서은기';
SET @userName2 = '강마루';
SELECT @userName1, REPEAT(@userName1,3) AS 'RESULT1'
				 , REPEAT('-', 10) AS 'RESULT2'
                 , @userName2
                 ,LPAD(@userName2, 10, '#')
                 ,RPAD(@userName2, 10, '#')
                 , LPAD(LEFT(@userName2, 2), 5, '#');

-- LTRIM(문자열), RTRIM(문자열), TRIM(문자열) : 문자열 공백 없애기 
SET @txt = '                     HELLO MySql                 ';
SELECT LENGTH(@txt), LTRIM(@txt), RTRIM(@txt), TRIM(@txt);

-- usertbl 테이블에서 name 필드값을 다음과 같이 표시하여라 =>  홍**
SELECT CONCAT(SUBSTRING(name,1,1), '**') AS '이름'
FROM usertbl; 

-- usertbl3 테이블에서 name 필드값이 조로 시작하는 문자열을 다음과 같이 변경하여라 => 조관우 회원님 조용필 회원님
CREATE TABLE userTbl3(SELECT * FROM userTbl);

SELECT CONCAT(name,' 회원님')
FROM userTbl3
WHERE name LIKE '조%';

UPDATE userTbl3 SET name = CONCAT(name,' 회원님') 
WHERE name LIKE '조%'; 

SELECT * FROM usertbl3;



-- (p232 p248) 날짜 자료형 종류: YEAR, DATE, TIME, DATETIME  
-- 문자열에서 날짜형 => CAST ( 문자열|문자열필드 AS DATE, TIME, DATETIME)
--                 CONVERT ( 문자열|문자열필드 , DATE, TIME, DATETIME)

-- 날짜형에서 문자열 => CAST ( 시계열변수|시계열필드 AS CHAR(자릿수))
--                 CONVERT ( 시계열|시계열필드 , CHAR(자릿수))

-- EX) 시계열데이타문자열형식  ????-??-?? ??:??:??
SELECT  CONVERT('2020-12-03', DATE) AS '결과1'
       ,CONVERT('12:30:30', TIME) AS '결과2'
	   ,CONVERT('2020-12-03 12:30:30', DATETIME) AS '결과3';

 
-- 현재 시간과 날짜 출력 
-- NOW() : 내장함수로 현재의 날짜와 시간을 표시 
-- SYSDATE() : 내장함수로 현재의 날짜와 시간을 표시 
-- CURDATE() : 현재 날짜 표시 
-- CURTIME() : 현재 시간 표시 
SELECT NOW(), SYSDATE(), CURDATE(), CURTIME(); -- 결과) 2020-11-23 11:13:47,	2020-11-23 11:13:47, 2020-11-23, 11:13:47

-- CAST ( 시계열변수|시계열필드 AS DATE|TIME)
-- CONVERT ( 시계열변수|시계열필드 , DATE|TIME )
SELECT NOW() AS '등록날짜와시간'
      , CAST(now() AS TIME) AS '등록시간'
        , CAST(now() AS DATE) AS '등록날짜'
        , CONVERT(now() , DATE) AS '등록날짜'
        , CONVERT(now() , TIME) AS '등록시간';

/* timeTable 테이블 생성후 날짜형으로 필드명 지정후 레코드 삽입하기 */
-- CREATE TABLE 테이블명 (필드명 자료형 ....);
-- tDate, tTime, tDatetime
USE sqldb;
CREATE TABLE timeTable
   (tDate DATE, tTime TIME, tDatetime DATETIME);
DESC timeTable;

-- EX) 레코드 삽입 
INSERT INTO timeTable (tDate, tTime, tDatetime) 
         VALUES (now(), now(), now()); 

INSERT INTO timeTable (tDate, tTime, tDatetime) 
         VALUES (CURDATE(), CURTIME(), SYSDATE()); 

SELECT * FROM timeTable;



-- YEAR(날짜), MONTH(날짜), DAY(날짜), DAYOFMONTH(날짜), DATE(날짜)  
-- HOUR(시간), MINUTE(시간), SECOND(시간), TIME(시간)  
SELECT now(), YEAR(now()), MONTH(now()), DAY(now()),
      HOUR(now()), MINUTE(now()), SECOND(now()),
        DATE(now()), TIME(now());

-- EX) userTbl 테이블에서 년도, 월, 일 분리 시켜 출력하기 
DESC userTbl;
SELECT * FROM userTbl;
SELECT name, mdate, 
       YEAR(mdate) AS '가입 년도',
       MONTH(mdate) AS '가입 월',
       DAY(mdate) AS '가입 일'
FROM userTbl LIMIT 3;	
   
SELECT name, mdate,  CONCAT(YEAR(mdate) , ' 년 ', MONTH(mdate) , ' 월 ', DAY(mdate), ' 일 ') AS '회원 가입일'
FROM userTbl LIMIT 3;
   
-- EX) userTbl 테이블에서 5월에 가입한 회원 목록 
SELECT * FROM userTbl WHERE MONTH(mdate) = 5;
         
SELECT name, CONCAT(' 회원님의 가입일은 ', YEAR(mdate),'년 ', MONTH(mdate), '월 ', DAY(mdate), '일 입니다.') '결과'
FROM userTbl 
WHERE name = '성시경';

-- DAYOFWEEK(날짜) : 요일표시 1~7(일요일~토요일) | MONTHNAME(날짜) : 달을 영문으로 표시 | DAYOFYEAR(날짜) : 1년중 몇번째 날인지 표시 
SELECT DAYOFWEEK(now()), MONTHNAME(now()), DAYOFYEAR(now()); 	-- 결과 => 2	  November	328

-- EX) 2020년은 얼마나 남았나요...?? ㅠㅠ
SELECT 365-DAYOFYEAR(now()) AS '2021년 카운트';
SELECT DAYOFYEAR(now()) '열심히 달려온 2020년', 365-DAYOFYEAR(now()) '마지막까지 달려갈 2020년';


-- date_format() 함수 
-- date_format(시계열데이타|시계열필드, 포맷형식)
-- 포맷형식1 %Y|%y, %M|%m|%b, %d, %W|%a
-- 포맷형식2 %H|%h, %i, %s
SELECT now(),
       date_format(now(), '%Y-%M-%d') -- 2020-November-23
      ,date_format(now(), '%y-%m-%d') -- 20-11-23
	  ,date_format(now(), '%W') -- Monday
	  ,date_format(now(), '%H : %i : %s'); 


-- 날짜 연산 함수 => DATEDIFF(날짜1, 날짜2) : 날짜1 - 날짜 2  |  TIMEDIFF(시간1, 시간2) : 시간1- 시간2
SELECT DATEDIFF('2020-12-31', now()) AS '디데이', TIMEDIFF('24:00:00', CURTIME()) '남은시간';

-- EX) 수능은 얼마남았을까요? 수능 날짜 12월 3일 
SELECT CONCAT('수능까지 ',DATEDIFF('2020-12-03', now()),'일 남았습니다,') AS '수능 D- Day';


-- ************************************************* 점심시간
-- Q1. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 7의 레코드만 정렬시켜 출력하여라. 
-- 정렬 기준은 emp_no 기준이다. 
/*
사원번호   이름                   생년월일   
499999   Sachin  Tsukuda         1958-05-01
499998   Patricia  Breugel      1956-09-05
499997   Berhard  Lenart         1961-08-03
499996   Zito  Baaz            1953-03-07
499995   Dekang  Lichtner      1958-09-24
499994   Navin  Argence         1952-02-26
499993   DeForest  Mullainathan   1963-06-04
*/        
USE EMPLOYEES;
SELECT emp_no '사원번호', CONCAT(first_name, ' ', last_name) '이름', birth_date '생년월일' 
FROM employees
WHERE emp_no LIKE '4%' ORDER BY emp_no DESC LIMIT 7;


-- Q2. employees 테이블에서 문자열 함수를 이용하여 birth_date 필드값이 
-- ????년 ??-?? 형태로 출력되도록 하여라. 
-- 정렬 기준은 first_name 기준이다.
/*
emp_no  first_name   last_name       birth_date        

11935   Aamer      Jayawardene      1963년  03-23
12160   Aamer      Garrabrants      1954년  12-11
15332   Aamer      Slutz         1961년  12-29
11800   Aamer      Fraisse         1958년  12-09
13011   Aamer      Glowinski      1955년  02-25
*/
SELECT emp_no, first_name, last_name, CONCAT(YEAR(birth_date), '년 ', MONTH(birth_date), '-', DAY(birth_date)) 'birth_date'
FROM employees
ORDER BY first_name;  

-- 강사님 답
select 	emp_no, first_name, last_name, 
		date_format(birth_date, "%Y년 %m-%d") as "birth_date" 
        from employees
        ORDER BY first_name LIMIT 5;
        

        
        
-- Q3. employees 테이블에서 문자열 함수를 이용하여 hire_date 필드값에서
-- '-'를 '__'으로 교체하여 출력되도록 하여라.  
-- REPLACE(문자열, 원래문자열, 교체문자열)
/*
emp_no  first_name   last_name   hire_date             
10001   Georgi      Facello      1986__06__26
10002   Bezalel      Simmel      1985__11__21
10003   Parto      Bamford      1986__08__28
*/

SELECT emp_no, first_name, last_name, REPLACE(hire_date,'-', '__') 'hire_date'
FROM employees;




-- Q4. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--     입사년도의 경우 년도만 출력되도록한다. 
/*
사원명           성별  입사년도
Georgi Facello   M   1986 년
Bezalel Simmel   F   1985 년
Parto Bamford   M   1986 년
...
*/

SELECT CONCAT(first_name, ' ', last_name) '사원명', gender '성별', CONCAT(YEAR(hire_date),'년') '입사년도'
FROM employees;

-- 강사님 답
SELECT 	CONCAT(first_name, ' ', last_name) AS '사원명', 
		gender AS '성 별',
		CONCAT(SUBSTRING(hire_date, 1, 4), ' 년') 
			AS '입사년도'
		FROM employees LIMIT 3;

-- Q5. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--  first_name 필드값의 경우  첫글자 외에서 '*' ,  last_name 필드값의 경우 모든 글자를 '*'로 표시한다.   (모르겠다)
/*
emp_no  first_name  last_name  gender     hire_date

10001   G*****      *******      M      1986-06-26
10002   B******      ******      F      1985-11-21
10003   P****      *******      M      1986-08-28

*/
-- 강사님 답 
SELECT 	emp_no, 
		CONCAT(LEFT(first_name, 1),
        REPEAT('*', length(first_name)-1)) AS 'first_name', 
        REPEAT('*', length(last_name)) AS 'last_name',
        gender, hire_date
		FROM employees LIMIT 3;
        
-- 다른분 답
select emp_no, rpad(substring(first_name, 1, 1), length(first_name) - 1, "*") as "first_name", 
lpad("", length(last_name), "*") as "last_name", gender, hire_date from employees;


-- Q6. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--  성별(gender) 필드값을 M,F를 남자,여자 로 표시한다.
-- IF(조건식, 값1, 값2)
-- 조건식이 True 이면 값1, False 이면 값2 반환 
/*
사원번호   생년월일        사원명          성별    입사일 
10001   1953-09-02   Georgi Facello   남자    1986-06-26
10002   1964-06-02   Bezalel Simmel   여자    1985-11-21
10003   1959-12-03   Parto Bamford   남자    1986-08-28
*/

SELECT emp_no '사원번호', birth_date '생년월일', CONCAT(first_name, ' ', last_name) '사원명', 
		CASE gender
		   WHEN 'F' THEN '여자'
		   ELSE '남자'
		END AS '성별', hire_date '입사일'
FROM employees;

-- 강사님 답
SELECT 	emp_no AS '사원번호', 
		birth_date AS '생년월일', 
        CONCAT(first_name, ' ', last_name) AS '사원명',  
		IF(gender='M', '남자', '여자') AS '성별',
        hire_date AS '입사일'
		FROM employees LIMIT 3;

-- Q7. employees 테이블에서 함수를 이용하여 남자 사원수를 다음과 같이 출력하여라. 
/*
  남자 사원수 
------179973 명
*/

SELECT CONCAT(LPAD(COUNT(gender),12,'-'), ' 명') '남자 사원수' FROM employees
WHERE gender = 'M';



-- Q8. employees 테이블에서 가장 최근에 입사한 사람 3명만 출력하시오
SELECT * FROM employees
ORDER BY hire_date DESC LIMIT 3;

-- Q9. SALARIES 테이블에서 급여가 가장 많은 사람 10명을 제외하고 다음 10명을 구하시오.
--   즉, 11등부터 20등 까지… LIMIT index-1, count
SELECT * FROM salaries
ORDER BY salary DESC LIMIT 10,10;



-- Q10. employees 테이블에서  입사한지 가장 오래된 사람의 레코드를 다음과 같이 출력하여라.
-- date_format(시계열데이타|시계열필드, 포맷형식)
-- 포맷형식1 %Y|%y, %M|%m|%b, %d, %W|%a
-- 포맷형식2 %H|%h, %i, %s
/*
   사원이름               입사일
Margareta Markovitch   1985-January-01-Tuesday
*/

SELECT CONCAT(first_name, ' ', last_name) '사원이름', date_format(hire_date, '%Y-%M-%d-%W')'입사일'
FROM employees ORDER BY HIRE_DATE LIMIT 1;


  
-- Q11. employees 테이블에서  1999년에 입사한 직원 리스트를 구하시오.
SELECT * FROM employees
WHERE YEAR(hire_date) = '1999';



-- Q12. employees 테이블에서  1999년에 입사한 직원 중 여자 직원(GENDER='F') 리스트를 구하시오.
SELECT * FROM employees
WHERE YEAR(hire_date) = '1999'
AND gender = 'F';



-- Q13. employees 테이블에서  1999년에 입사한 직원 중 남자 직원(M)은 몇 명인가?
SELECT COUNT(*) '1999년에 입사한 남직원' FROM employees
WHERE YEAR(hire_date) = '1999'
AND gender = 'M';


-- Q14. employees 테이블에서   1998년이나 1999년에 입사한 직원의 수를 구하시오.
SELECT COUNT(*) FROM employees
WHERE YEAR(hire_date)= 1998 OR YEAR(hire_date)= 1999;



-- Q15. employees 테이블에서  1995년부터 1999년까지 입사한 직원의 수를 구하시오.
SELECT COUNT(*) FROM employees
WHERE YEAR(hire_date) BETWEEN '1995' AND '1999';



-- Q16. 날짜함수를 이용하여 아래와 같이 오늘 날짜를 기준으로 출력하여라 
-- 수료식 날짜는 2020년 12월 24일로 한다. 
/* 수료식 앞으로 ??일 */
SELECT CONCAT('수료식 앞으로 ', DATEDIFF('2020-12-24', now()),'일'); 


-- worldDb 데이타베이스 이용 
-- Q17. country 테이블에서 독립년도(IndepYear)가 NULL인 경우 '알수없음' 으로 표시하여라. 
/*
  국가      독립년도
  ?        알수없음'
  ?          ?
  ?          ?
*/
SELECT name '국가', IF(ISNULL(IndepYear), '알수없음', IndepYear) '독립년도'
FROM country;


-- 강사님 답
SELECT Name AS '국가', 
	IFNULL(IndepYear, '알수없음') AS '독립년도' 
	FROM  country
    LIMIT 20;  
    
SELECT name '국가', 
	IF(ISNULL(IndepYear), '알수없음', IndepYear) '독립년도'
	FROM country;
    
    
    
-- worldDb 데이타베이스 이용 
-- Q18.  country 테이블에서 독립년도(IndepYear)가 음수로 표시된 레코드의 필드값을 'BC' 와 함께 연도를 표시하여라 
/*
  국가         독립년도
  China     BC.1523
    ?            ?
    ?            ?
*/

SELECT * FROM country;
SELECT name '국가', IF(IndepYear<0, REPLACE(IndepYear,'-','BC.'), IndepYear) '독립년도'
FROM country 
WHERE IndepYear IS NOT NULL
ORDER BY IndepYear ;


-- 강사님 답
SELECT 
	Name AS '국가', 
	concat('BC.' , ABS(IndepYear)) AS '독립년도' 
	FROM country 
	WHERE IndepYear<0 ORDER BY IndepYear;
    
select Name as '국가',
      if(IndepYear<0, CONCAT('BC.',-IndepYear), IndepYear) as '독립년도'
       from country;


-- ************************************************* 퀴즈 후 수업
-- 조인이란? 2개이상 테이블에서 조건을 기준으로 출력하는 기능 

-- INNER JOIN 1 --
-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      INNER JOIN 테이블2
--         ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명 이용 
--            (서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

SELECT * FROM userTbl;
SELECT * FROM buyTbl;

-- 이너조인 userTbl + buyTbl
-- 공통 필드(컬럼) 이 있는지 확인 : userId         
SELECT * 
FROM userTbl
     INNER JOIN buyTbl
	 ON userTbl.userID = buyTbl.userID
ORDER BY userTbl.userID;

-- 12
SELECT count(*) 
FROM buyTbl
     INNER JOIN userTbl
	 ON buyTbl.userID = userTbl.userID;        

-- 내부조인으로 두 테이블의 특정 필드 출력 
-- 테이블에 중복으로 있는 필드명이 아니면 그대로 필드이름으로 호출이 가능  
-- userTbl => userID, name, addr
-- buyTbl =>  userID, prodName, price, amount 
-- 내부조인시 각 테이블의 필드는 테이블명.필드명으로 탐색 

SELECT userTbl.userID AS '회원아이디', 
      name, addr, prodName, price, amount 
FROM userTbl
	INNER JOIN buyTbl
	ON userTbl.userId = buyTbl.userId;

-- 각 필드를 테이블명.필드로 지정 
SELECT userTbl.userID AS '회원아이디', 
      userTbl.name, userTbl.addr, 
        buyTbl.prodName, buyTbl.price, buyTbl.amount 
FROM userTbl
	 INNER JOIN buyTbl
	 ON userTbl.userId = buyTbl.userId;
     
-- INNER JOIN 2 
-- 테이블명에 별칭 지정하기  
-- SELECT * 또는 별칭.컬럼명 
--    FROM 테이블1 테이블별칭1
--      INNER JOIN 테이블2 테이블별칭2
--         ON 조인될조건-별칭1.컬럼명 = 별칭2.컬럼명 이용 
--            (서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

-- userTbl + buyTbl 조인시 테이블 별칭 이용하기   U / B
SELECT U.userID AS '회원아이디', U.name, U.addr,  B.prodName, B.price, B.amount 
FROM userTbl U
	 INNER JOIN buyTbl B
	 ON U.userId = B.userId;
      

SELECT U.userID '아이디', U.name '이름', U.addr '지역',  
	   B.prodName '상품명', B.amount '수량', B.price '가격', (B.amount*B.price) '구매금액'
FROM userTbl U
	 INNER JOIN buyTbl B
     ON U.userId = B.userId;
     
 -- FORMAT(필드명|숫자데이타, 소숫점자리수) : 3자리마다 쉼표(,) 
 SELECT 
		B.userID AS '아이디', U.name AS '이름', U.addr AS '지역',
		B.prodName AS '상품명',   B.amount AS '수량',
		format(B.price, 0) AS '가격', format(B.amount * B.price, 0) AS '구매금액'  
FROM buyTbl B
     INNER JOIN userTbl U
	 ON B.userID = U.userID;  
        
        
        
-- employees DB에서 테이블 조인하기
USE employees;

-- => 조인하기 전 데이터 파악
-- emp_no, birth_date, first_name, last_name, gender, hire_date
SELECT * FROM employees LIMIT 5;

-- emp_no, dept_no, from_date(부서근무시작일), to_date(부서근무 마지막날짜 EX.9999-01-01 이면 현재 근무 중)
SELECT * FROM dept_emp LIMIT 5;

-- emp_no, title(부서명), from_date, to_date
SELECT * FROM titles LIMIT 5;

-- employees + dept_emp 테이블 조인하기 (전체 필드 모두 출력)
SELECT * FROM employees e
INNER JOIN dept_emp d
ON e.emp_no = d.emp_no LIMIT 10;

-- 사원번호, 이름, 성별, 부서번호 필드만 출력 
SELECT E.emp_no AS '사원번호', concat(E.first_name, ' ', E.last_name) AS '이름',
    E.gender AS '성별', D.dept_no AS '부서번호'
FROM employees E
      INNER JOIN dept_emp D
      ON E.emp_no = D.emp_no LIMIT 10;
         
-- 남자 사원만 사원번호, 이름, 성별, 부서번호 필드만 출력 
SELECT E.emp_no AS '사원번호', concat(E.first_name, ' ', E.last_name) AS '이름',
    E.gender AS '성별', D.dept_no AS '부서번호'
FROM employees E
     INNER JOIN dept_emp D
     ON E.emp_no = D.emp_no 
WHERE E.gender = 'M' LIMIT 10;

-- 퀴즈 - employees + titles 테이블 조인하기 => 사원번호, 이름, title(부서명), 성별, 입사일 
-- 사원이름이 'S'로 시작하는 레코드만 10개만 출력, 정렬기준은 사원이름 
SELECT e.emp_no '사원번호', CONCAT(first_name,' ',last_name) '이름', t.title '부서명', e.gender '성별', e.hire_date '입사일'
FROM employees e
	 INNER JOIN titles t
	 ON e.emp_no = t.emp_no
WHERE e.first_name LIKE 'S%'
ORDER BY e.first_name LIMIT 10;

SELECT e.emp_no '사원번호', CONCAT(first_name,' ',last_name) '이름', title '부서명', gender '성별', hire_date '입사일'
FROM employees e
	 INNER JOIN titles t
	 ON e.emp_no = t.emp_no
WHERE first_name LIKE 'S%'
ORDER BY first_name LIMIT 10;




-- 3개의 테이블 조인
-- 학생 테이블 (stdTbl) 생성 
USE sqldb; 
DROP TABLE IF EXISTS stdTbl;
CREATE TABLE stdTbl(
	stdName VARCHAR(10) NOT NULL PRIMARY KEY,
    addr CHAR(4) NOT NULL);
DESC stdTbl;

-- 동아리 테이블 (clubTbl) 생성
DROP TABLE IF EXISTS clubTbl;
CREATE TABLE clubTbl(
	clubName VARCHAR(10) NOT NULL PRIMARY KEY,
    roomNo CHAR(4) NOT NULL);
DESC clubTbl;

-- 학생 동아리 테이블 (stdclubTbl) 생성
DROP TABLE IF EXISTS stdclubTbl;
CREATE TABLE stdclubTbl(
	num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    stdName VARCHAR(10) NOT NULL,
    clubName VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubTbl(clubName));
DESC stdclubTbl;

-- stdTbl: 데이타 입력 후 테이블 확인 / 복수개의 레코드 삽입하기 
-- INSERT INTO 테이블명 VALUES (값1, 값2...), (값1, 값2...) ....;
INSERT INTO stdTbl 
VALUES ('김범수','경남'),('성시경','서울'), 
	   ('조용필','경기'),('은지원','경북'),
	   ('바비킴','서울');
SELECT * FROM stdTbl;  

-- clubTbl: 데이타 입력 후 테이블 확인 
INSERT INTO clubTbl 
VALUES ('수영','101호'), ('바둑','102호'),('축구','103호'), ('봉사','104호');
SELECT * FROM clubTbl; 

-- stdclubTbl: 데이타 입력 후 테이블 확인 
-- num 필드가 자동증감, 기본키 
INSERT INTO stdclubTbl 
VALUES (NULL, '김범수','바둑'), (NULL,'김범수','축구'), 
	   (NULL,'조용필','축구'), (NULL,'은지원','축구'), 
	   (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');
SELECT * FROM stdclubTbl; 

-- stdTbl + stdclubTbl
SELECT * FROM stdTbl s
INNER JOIN stdclubTbl sc ON s.stdName  = sc.stdName;

-- clubTbl + stdclubTbl
SELECT * FROM stdclubTbl sc
INNER JOIN  clubTbl c ON sc.clubName = c.clubName;  
    
-- 테이블 3개 조인 (1) : 학생 기준으로 학생이름, 지역, 가입 동아리, 동아리 방번호
-- stdTbl + stdclubTbl + clubTbl => 전체필드 출력
SELECT * FROM stdTbl s
INNER JOIN stdclubTbl sc ON sc.stdName = s.stdName
INNER JOIN clubTbl c ON c.clubName = sc.clubName;

-- stdTbl + stdclubTbl + clubTbl => 학생명, 지역, 동아리명, 동아리방주소
SELECT s.stdName '학생명', s.addr '지역', c.clubName '동아리명', c.roomNo '동아리방주소'
FROM stdTbl s
INNER JOIN stdclubTbl sc ON sc.stdName = s.stdName
INNER JOIN clubTbl c ON c.clubName = sc.clubName;



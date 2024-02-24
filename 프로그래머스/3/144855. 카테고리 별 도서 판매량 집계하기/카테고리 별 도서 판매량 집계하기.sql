-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) as TOTAL_SALES
FROM BOOK as B
INNER JOIN BOOK_SALES as S
ON B.BOOK_ID = S.BOOK_ID
where S.SALES_DATE like '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY
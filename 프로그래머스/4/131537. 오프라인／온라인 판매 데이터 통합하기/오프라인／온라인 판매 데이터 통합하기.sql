-- 코드를 입력하세요
SELECT date_format(SALES_DATE,"%Y-%m-%d") as SALES_DATE,
PRODUCT_ID,USER_ID,SALES_AMOUNT
from online_sale
where sales_date like '%2022-03%'

union all

SELECT date_format(SALES_DATE,"%Y-%m-%d") as SALES_DATE,
PRODUCT_ID,NULL USER_ID,SALES_AMOUNT
from offline_sale
where sales_date like '%2022-03%'

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID

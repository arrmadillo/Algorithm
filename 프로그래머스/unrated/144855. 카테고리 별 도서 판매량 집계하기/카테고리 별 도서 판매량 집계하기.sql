-- 코드를 입력하세요
SELECT
    CATEGORY, SUM(S.SALES)
FROM
    BOOK
INNER JOIN BOOK_SALES AS S USING (BOOK_ID)
WHERE
    DATE_FORMAT(SALES_DATE, '%Y-%m') BETWEEN '2022-01' AND '2022-01'
GROUP BY
    CATEGORY
ORDER BY
    CATEGORY; 
-- 강남 또는 논현만 있는 테이블
WITH KN as (
    SELECT
        *
    FROM MERCHANTS
    WHERE 1=1
        AND NAME REGEXP "강남|논현"
)

SELECT
    M.ID
    , M.NAME
    , COUNT(CASE WHEN C.CATEGORY = 0 then 1 end) as PAY_COUNT
FROM KN M
    INNER JOIN CARD_USAGES C on (M.ID = C.MERCHANT_ID)
GROUP BY
    1
ORDER BY
    1
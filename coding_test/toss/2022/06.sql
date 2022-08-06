-- 나이가 없는 유저의 임시 나이 값
SELECT @TMP_AGE := (
        SELECT 
            ROUND(SUM(AGE)/COUNT(AGE))
        FROM TOSS_AGE_GENDER
    );

-- 성별/나이 구간 별 거래 가능한 회원 테이블
WITH GROUPED_TRADABLE_USER as ( 
    SELECT
        TU.ID
        , TU.TRADE_YN
        , TAG.GENDER
        , TAG.AGE
        , CASE
            WHEN IFNULL(TAG.AGE, @TMP_AGE) < 20 THEN '20대 미만'
            WHEN IFNULL(TAG.AGE, @TMP_AGE) >= 20 AND IFNULL(TAG.AGE, @TMP_AGE) < 30 THEN '20대 이상 30대 미만'
            WHEN IFNULL(TAG.AGE, @TMP_AGE) >= 30 AND IFNULL(TAG.AGE, @TMP_AGE) < 40 THEN '30대 이상 40대 미만'
            WHEN IFNULL(TAG.AGE, @TMP_AGE) >= 40 AND IFNULL(TAG.AGE, @TMP_AGE) < 50 THEN '40대 이상 50대 미만'
            WHEN IFNULL(TAG.AGE, @TMP_AGE) >= 50 AND IFNULL(TAG.AGE, @TMP_AGE) < 60 THEN '50대 이상 60대 미만'
            ELSE '60대 이상'
        END as AGE_RANGE
    FROM TOSS_USER TU
        INNER JOIN TOSS_AGE_GENDER TAG ON (TU.ID = TAG.USER_ID)
    WHERE 1=1
        OR TU.TRADE_YN = 'Y'
        OR TAG.AGE IS NULL
)

SELECT 
    GENDER as '성별'
    , AGE_RANGE as '나이구간'
    , COUNT(1) as '게시글수'
FROM GROUPED_TRADABLE_USER GTU
    INNER JOIN TOSS_COMMUNITY_MESSAGE TCM ON (GTU.ID = TCM.USER_ID)
GROUP BY
    1, 2
ORDER BY
    3 DESC, 2 DESC
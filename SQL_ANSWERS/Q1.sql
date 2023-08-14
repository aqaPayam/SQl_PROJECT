WITH P AS (
	SELECT G.RESIDENCE_ID, AVG(H.SCORE) AS AVG_SCORE FROM RESIDENCE AS G, GUEST_COMMENT_ON_HOST AS H WHERE G.RESIDENCE_ID = H.RID GROUP BY (G.RESIDENCE_ID)
)
SELECT DISTINCT A.RESIDENCE_ID, A."TITLE", (B.IMAGE).IMAGE, C.CITY, D.NATIONAL_CODE,
	(D.PERSONAL_INFORMATION).FIRST_NAME, (D.PERSONAL_INFORMATION).MIDDLE_NAME, (D.PERSONAL_INFORMATION).LAST_NAME,
	E.AVG_SCORE 
	FROM RESIDENCE AS A, PICTURES AS B, ADDRESS AS C, HOST AS D, P AS E
	WHERE A.RESIDENCE_ID = B.RESIDENCE_ID AND B.IMAGE_ID = 1 AND
	A.RESIDENCE_ID = C.RESIDENCE_ID AND C.CITY = 'Tabriz' AND A.MAX_CAPACITY > 3
	AND A.HOST_ID = D.NATIONAL_CODE AND E.RESIDENCE_ID = A.RESIDENCE_ID AND NOT EXISTS(SELECT * FROM RENT AS F WHERE F.RID = A.RESIDENCE_ID AND ('2020-01-03'::DATE >= F.END_DATE AND '2020-01-01'::DATE <= F.END_DATE OR '2020-01-01'::DATE <= F.START_DATE AND '2020-01-03'::DATE >= F.START_DATE) AND F."RENT_STATUS" <> 'Cancelled')
	ORDER BY AVG_SCORE ASC LIMIT 20 OFFSET 0;
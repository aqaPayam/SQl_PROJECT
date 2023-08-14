/* BARAYE HAME YE EGHAMTGAH HA RO NESHOON MIDE */
WITH R AS 
(SELECT RESIDENCE_ID,NATIONAL_CODE,PERSONAL_INFORMATION FROM RESIDENCE INNER JOIN HOST ON HOST.NATIONAL_CODE= RESIDENCE.HOST_ID)
SELECT (R.PERSONAL_INFORMATION).FIRST_NAME,R.NATIONAL_CODE,C.EXPLANATION,C.SCORE,C.SCORED_DATE 
FROM GUEST_COMMENT_ON_HOST AS C INNER JOIN R ON R.RESIDENCE_ID = C.RID 
ORDER BY SCORED_DATE ASC;


/* BARAYE YEK EGHAMTGAH RO NESHOON MIDE */
/* MATN SOAL DAQIQAN IN RO MIKHAD*/
WITH A AS 
(SELECT NATIONAL_CODE , (PERSONAL_INFORMATION).FIRST_NAME FROM HOST
 WHERE NATIONAL_CODE =  (SELECT HOST_ID FROM RESIDENCE WHERE RESIDENCE_ID = '46')),
B AS
(SELECT EXPLANATION,SCORE,SCORED_DATE FROM GUEST_COMMENT_ON_HOST WHERE RID = '46' ORDER BY SCORED_DATE ASC)
SELECT * FROM A,B


/* HALATI KE MANTEGHI TAR BOOD SOAL BEKHAD BE JAYE ESM O ID MIZBAN BARAYE MEHMAN RO MIKHAST */
WITH A AS 
(SELECT GUEST_ID AS NATIONAL_CODE,EXPLANATION,SCORE,SCORED_DATE FROM GUEST_COMMENT_ON_HOST 
WHERE RID = '46' ORDER BY SCORED_DATE ASC),
B AS (SELECT NATIONAL_CODE,(PESONAL_INFORMATION).FIRST_NAME FROM GUEST)
SELECT * FROM B NATURAL JOIN A

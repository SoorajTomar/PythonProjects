import sqlite3
root=sqlite3.connect('movie.db')
root.execute('''CREATE TABLE MOVIEDB (MOVIE_ID INT,MOVIE_NAME TEXT,GENRE TEXT,LANGUAGE TEXT,RATING REAL);''')
root.execute("INSERT INTO MOVIEDB (MOVIE_ID,MOVIE_NAME,GENRE,LANGUAGE,RATING) \
      VALUES (101,'AVENGERS','ACTION','ENG/HIN/TAM/TEL',4.5);")
root.execute("INSERT INTO MOVIEDB (MOVIE_ID,MOVIE_NAME,GENRE,LANGUAGE,RATING) \
      VALUES (102,'AVENGERS 2','ACTION','ENG/HIN/TAM/TEL',3.5);")
root.execute("INSERT INTO MOVIEDB (MOVIE_ID,MOVIE_NAME,GENRE,LANGUAGE,RATING) \
      VALUES (103,'AVENGERS 3','ACTION','ENG/HIN/TAM/TEL',2.5);")
root.execute("INSERT INTO MOVIEDB (MOVIE_ID,MOVIE_NAME,GENRE,LANGUAGE,RATING) \
      VALUES (104,'AVENGERS 4','ACTION','ENG/HIN/TAM/TEL',1.5);")
root.execute("INSERT INTO MOVIEDB (MOVIE_ID,MOVIE_NAME,GENRE,LANGUAGE,RATING) \
      VALUES (105,'AVENGERS REBOOT','ACTION','ENG/HIN/TAM/TEL',0.5);")
root.commit()
root.execute('UPDATE MOVIEDB SET RATING=RATING*1.1 WHERE RATING>0.0;')
root.execute('DELETE FROM MOVIEDB WHERE MOVIE_ID=102;')
root.execute('SELECT * FROM MOVIEDB WHERE RATING>3.0;')
root.close()
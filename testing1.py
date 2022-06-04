import sqlite3
root=sqlite3.connect('Ques1.db')
root.execute("INSERT INTO recipies (ID,NAME,description,category_id,chef_id,created) \
      VALUES (12321,'PMOMO','Chinese',11,224,'2022-12-11 07:01:11')");
root.commit()
root.close()
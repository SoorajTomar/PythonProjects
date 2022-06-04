import sqlite3
root=sqlite3.connect('Ques1.db')
root.execute('''CREATE TABLE recipies1
         (ID INT(11) PRIMARY KEY     NOT NULL,
         NAME           varchar(400)    NOT NULL,
         description            text     NOT NULL,
         category_id       int(11),
         chef_id int(11),created datetime);''')
root.execute("INSERT INTO recipies1 (ID,NAME,description,category_id,chef_id,created) \
      VALUES (11,'MOMO','Chinese',11,224,2022-12-11 )");
root.execute("INSERT INTO recipies1 (ID,NAME,description,category_id,chef_id,created) \
      VALUES (21,'Spring Rolls','Chinese',12,224,2022-12-11 )");
root.execute("INSERT INTO recipies1 (ID,NAME,description,category_id,chef_id,created) \
      VALUES (13,'Idly','Indian',12,225,2022-12-11)");
root.execute("INSERT INTO recipies1 (ID,NAME,description,category_id,chef_id,created) \
      VALUES (12321,'PMOMO','Chinese',11,224,'2022-12-11 07:01:11')");
root.commit()
root.execute('select count(ID) from recipies1 where description="Chinese";')
root.execute('select * from recipies1 where chef_id=000002;')
root.execute('select description from recipies1 where substr(name,1,1)="P";')
root.close()
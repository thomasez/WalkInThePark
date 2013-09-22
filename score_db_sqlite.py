import sqlite3
import os
from score_lib import Player, Course, Walk, WipConfig

class Db:
    def __init__(self):
        self.dbfile = os.environ.get('HOME') + "/" +".walkinthepark.db"
        self.conn = sqlite3.connect(self.dbfile)
        try:
            self.conn.execute("SELECT count(id) FROM Course")
        except:
            print "No tables defined, creating the database."
            self.create_db()
        return None

    def create_db(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("CREATE TABLE Course (id INTEGER PRIMARY KEY, name STRING, baskets INTEGER)")
            cur.execute("CREATE TABLE Basket (id INTEGER PRIMARY KEY, course_id INTEGER, basket_num INTEGER, par INTEGER)")
            cur.execute("CREATE TABLE Player (id INTEGER PRIMARY KEY, name STRING)")
            cur.execute("CREATE TABLE Walk (id INTEGER, course_id INTEGER, started_at LONG, ended_at LONG)")
            cur.execute("CREATE TABLE Throw (id INTEGER PRIMARY KEY, walk_id INTEGER, basket_num INTEGER, thrown LONG, amount INTEGER)")
            cur.execute("INSERT INTO  Course VALUES (null, ?,?)", ('Ekeberg', 18))
            course_id = cur.lastrowid
            ek = [ 3,3,3,4,3,3,3,3,3,3,3,3,3,4,3,3,3,3 ]
            i = 1
            for e in ek:
                cur.execute("INSERT INTO basket VALUES (null, ?, ?, ?)", (course_id, i, e))
                i += 1

    def get_course_list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT name from Course")
        rows = cur.fetchall()
        list = []
        for row in rows:
            list.append(row[0]) 
        return list

    def get_course(self, name):
        cur = self.conn.cursor()
        cur.execute("SELECT id, baskets from Course WHERE name=?", (name,))
        row = cur.fetchone()
        course = Course();
        course.set_name(name)
        course.set_id(int(row[0]))
        course_id = int(row[0])
        course.set_baskets(int(row[1]))
        cur.execute("SELECT par from Basket WHERE course_id=?", (course_id,))
        rows = cur.fetchall()
        i = 1
        coursepar = 0
        course.par = []
        course.par.append(0);
        for row in rows:
            coursepar += int(row[0])
            course.par.append(int(row[0]))
        course.par[0] = course.coursepar = coursepar
        return course
             
    def save_score(self, Walk):
        with self.conn:
            # Is this a running walk?
            cur = self.conn.cursor()
            started_at = Walk.get_started_at()
            cur.execute("SELECT id from Walk WHERE started_at=?", (started_at,))
            row = cur.fetchone()
            if row:
                Walk.set_id(row)
            saved_before = True
            if not Walk.get_id():
                st = cur.execute("INSERT INTO Walk VALUES(null, ?, ?, null)", (Walk.course.get_id(), started_at,))
                Walk.set_id(cur.lastrowid)
                saved_before = False
            print "Walk:" + str(Walk.get_id())
            i = 0
            for s in Walk.get_pure_score_list():
                i += 1
                if saved_before:
                    cur.execute("SELECT id from Throw WHERE walk_id=? AND basket_num=?", (started_at, i,))
                    print "rowid:" + row
                    cur.execute("UPDATE Throw SET amount=? WHERE id=?", (s, row,))
                else:
                    cur.execute("INSERT INTO Throw VALUES(null, ?, ?, null, ?)", (Walk.course.get_id(), i, s,))
                print s

    def save_score_as_course(self, Walk, coursename):
        with open(coursename + '.course', 'wb') as csvfile:

            writer = csv.writer(csvfile, delimiter=';', \
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
            sac = Walk.get_score_as_course()
            sac.insert(0, coursename)
            writer.writerow(sac)


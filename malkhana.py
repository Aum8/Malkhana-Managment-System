
import sqlite3
import hashlib
from datetime import datetime
from datetime import date

conn = sqlite3.connect('malkhana.db')
cursor = conn.cursor()


def login(userid, password):
  cursor.execute(
    "CREATE TABLE IF NOT EXISTS logger (userid TEXT,logintime TEXT,logouttime TEXT)"
  )
  cursor.execute("SELECT userid FROM userdb WHERE userid= ? AND pass= ?",
                 (userid, password))
  result = cursor.fetchone()
  if result:
    logintime(userid)
    return True
  else:
    return False


def logintime(userid):

  lit = str(datetime.now())
  lit = lit[:19]
  cursor.execute("insert into logger (userid,logintime) values(?,?)",
                 (userid, lit))


def logout(userid):

  lot = str(datetime.now())
  lot = lot[:19]
  cursor.execute("update logger SET logouttime =? where userid = ?",
                 (lot, userid))


def viewlog():

  cursor.execute("select * from logger")
  result = cursor.fetchall()
  for row in result:
    print(row)


def users():
  cursor.execute("CREATE TABLE userdb(userid TEXT,pass TEXT)")
  cursor.execute(
    "INSERT INTO userdb (userid,pass) VALUES('aumhadiyal','2502')")
  cursor.execute(
    "INSERT INTO userdb (userid,pass) VALUES('kevinhirole ','0106')")
  cursor.execute(
    "INSERT INTO userdb (userid,pass) VALUES('aumthakkar','0803')")
  cursor.execute(
    "INSERT INTO userdb (userid,pass) VALUES('vedantkahar','2603')")


def createTable():
  cursor.execute(
    '''CREATE TABLE IF NOT EXISTS items (barcode TEXT,item_name TEXT,date DATE,time TEXT,bywhom TEXT,found_where TEXT,inFSL TEXT)'''
  )


def insert(item_name, item_date, item_bywhom, item_found_where, inFSL):
  item_time = str(datetime.now())
  barcode = genuniqid2(item_name, item_time)
  cursor.execute(
    "INSERT INTO items (barcode,item_name,date,time,bywhom,found_where,inFSL) VALUES (?,?,?,?,?,?,?)",
    (barcode, item_name, item_date, item_time, item_bywhom, item_found_where,
     inFSL))
  conn.commit()
  return barcode
  # Call smart contract function to check in the item


def select(what_to_select):
  cursor.execute("SELECT {} FROM items".format(what_to_select))
  result = cursor.fetchall()
  #return result
  #selected_data = select('*')
  printdata(result)


def printdata(selected_data):
  for row in selected_data:
    print(row)


def genuniqid2(name, time):
  ss = name + time
  uniq_id = hashlib.sha256(ss.encode()).hexdigest()
  return uniq_id[:7]


def genuniqid1(name):
  uniq_id = hashlib.sha256(name.encode()).hexdigest()
  return uniq_id[:7]


def fsl_create():
  cursor.execute(
    "CREATE TABLE IF NOT EXISTS fsl_data (fslid TEXT,item_name TEXT,barcode TEXT,sentdate DATE,senttime TIME,whosent TEXT,recdate DATE,rectime TIME,whorec TEXT,details TEXT)"
  )


def fslsend(barcode, whosent, details):
  cursor.execute("SELECT item_name FROM items WHERE barcode= ? ", (barcode, ))
  result = cursor.fetchone()
  item_name = result[0]
  fslid = genuniqid1(barcode)
  sentdate = date.today()
  senttime = datetime.now()
  cursor.execute(
    "INSERT INTO fsl_data (fslid,item_name,barcode,sentdate,senttime,whosent,details) VALUES (?,?,?,?,?,?,?)",
    (fslid, item_name, barcode, sentdate, senttime, whosent, details))
  cursor.execute("UPDATE items SET inFSL='YES' WHERE barcode = ? ",
                 (barcode, ))
  conn.commit()


def fslrec(barcode, whorec):
  recdate = date.today()
  rectime = datetime.now()
  cursor.execute(
    "UPDATE fsl_data SET recdate = ? , rectime = ?, whorec = ? WHERE barcode = ?",
    (recdate, rectime, whorec, barcode))
  cursor.execute("UPDATE items SET inFSL = 'NO' WHERE barcode = ? ",
                 (barcode, ))
  conn.commit()


def printfsl():
  cursor.execute("SELECT * FROM fsl_data")
  result = cursor.fetchall()
  for row in result:
    print(row)


def inFSL(barcode):
  cursor.execute("SELECT inFSL FROM items WHERE barcode = ?", (barcode, ))
  result = cursor.fetchall()
  for row in result:
    print("Item in FSL?? - > ")
    print(row)


def con(choice):
  if choice == "yes" or choice == "YES":
    logincheck()
  else:
    print("end")
    conn.close()


def logincheck():
  global globaluserid
  #cursor.execute("drop table logger")
  userid = input("Enter user id : ")
  password = input("Enter password : ")
  check = login(userid, password)
  if check:
    globaluserid = userid
    print("Login successfull")
  else:
    print("wrong id pass")


#cursor.execute("ALTER TABLE logger RENAME COLUMN lougouttime TO logouttime")
'''cursor.execute("PRAGMA table_info(logger);")
rst = cursor.fetchall()
for rstt in rst:
  print(rstt'''

#cursor.execute("drop table items")
#cursor.execute("drop table fsl_data")
#cursor.execute("drop table logger")

logincheck()
createTable()
bcofitem = insert('Drugs', '2023-07-15', 'vedant', 'parul', 'NO')
print("bla bla bla inserted")
select('*')
fsl_create()
fslsend(bcofitem, "Aum", "for inspection")
print("sent in FSL so")
inFSL(bcofitem)
fslrec(bcofitem, 'Aum Thakkar')
print("recieved from FSL so")
inFSL(bcofitem)
print("details from FSL")
printfsl()
print("updated details in main table")
select('*')
#cursor.execute("SELECT * FROM fsl_data")
#result = cursor.fetchall()
#for row in result:
# print(row)
#logout(userid)
print("wanna log out???")
a = input()
if a == "y":
  logout(globaluserid)
conn.commit()
viewlog()

#cursor.execute("Update userdb set userid = 'kevinhirole' where pass='0106'")
#cursor.execute("DROP table items")
#cursor.execute("DROP table fsl_data")

conn.close()

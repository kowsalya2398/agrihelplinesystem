#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")


import cgi
import pymysql

conn=pymysql.connect("localhost","root","","myproject")
cur=conn.cursor()

f=cgi.FieldStorage()
pid=f.getvalue('id')
q1="""select * from farmer_reg_details where id=%s""" %(pid)
cur.execute(q1)
r=cur.fetchone()


if r!=None:
    q2= """delete from farmer_reg_details where id=%s""" %(pid)
    cur.execute(q2)
    conn.commit()
    print("""<script>alert("data deleted sucessfully");</script>""")

else:
    print("""<script>alert("record not found");</script>""")


q3="""select * from farmer_reg_details"""
try:
    cur.execute(q3)
    res=cur.fetchall()
except:
    print("<p>not inserted</p>")
conn.close()


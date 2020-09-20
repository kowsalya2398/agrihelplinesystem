#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")


import cgi
import pymysql

conn=pymysql.connect("localhost","root","","myproject")
cur=conn.cursor()

f=cgi.FieldStorage()
pid=f.getvalue('id')
q1="""select * from agrireg_details where id=%s""" %(pid)
cur.execute(q1)
r=cur.fetchone()


if r!=None:
    q2= """delete from agrireg_details where id=%s""" %(pid)
    cur.execute(q2)
    conn.commit()
    print("""<script>alert("data deleted sucessfully");
    location.href="adm_agrioff_delete.py?id=%s"
    </script>""" %(pid))


q3="""select * from agrireg_details"""
try:
    cur.execute(q3)
    res=cur.fetchall()
except:
    print("<p>not inserted</p>")
conn.close()


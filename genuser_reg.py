#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi,os,cgitb;cgitb.enable()
import pymysql

conn = pymysql.connect("localhost","root","","myproject")
cur = conn.cursor()
q1="""select max(id) from genuser_reg_details"""
cur.execute(q1)
r=cur.fetchone()
if r[0]==None:
    n=0
else:
    n=r[0]

z=""
if n<10:
    z="000"
elif n<100:
    z="00"
elif n<1000:
    z="0"
else:
    z=""
genuserid="genuser"+z+str(n+1)


print("""
<html>
<head>
<title>Genaral_user registration</title>
<link rel="icon" type="images/ico" href="images/icon.jpg">
<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
<style>
body
{
margin: 0;
padding: 0;
background-image:url("images/n2.jpg");
background-size:cover;
background-position:center;
font-family:sans-serif;
background-repeat:no-repeat;
}
table
{
background:;
color:black;
font-size:16px;
font-family:serif;
width:40%;
height:90%;
text-align:-webkit-center;
}
</style>
</head>
<script>
 function validate()
 {
  var a,b,c,d,e,h,i,j,k,l,m,n,o;
  a=document.getElementById("name1");
  b=document.getElementById("dob1");
  c=document.getElementById("gen1").checked==false;
  d=document.getElementById("gen2").checked==false;
  e=document.getElementById("company1");
  h=document.getElementById("address1");
  i=document.getElementById("district1");
  j=document.getElementById("state1");
  k=document.getElementById("email1");
  l=document.getElementById("phno1").value;
  m=document.getElementById("psw1");
  n=document.getElementById("pswd1");
  o=document.getElementById("ch1");
  if(a.value.trim()=="")
  {
   alert("enter the name");
   return false;
  }
  if(b.value.trim()=="")
  {
   alert("enter the dob");
   return false;
  }
  if( c && d)
  {
   alert("gender field is empty");
   return false;
  }
  if(e.value.trim()=="")
  {
   alert("enter the qual");
   return false;
  }
  if(f.value.trim()=="")
  {
   alert("enter the college");
   return false;
  }
  if(h.value.trim()=="")
  {
   alert("enter the address");
   return false;
  }
  if(i.value.trim()=="")
  {
   alert("enter the district");
   return false;
  }
  if(j.value.trim()=="")
  {
   alert("enter the state");
   return false;
  }
  if(k.value.trim()=="")
  {
   alert("enter the email");
   return false;
  }
  if(l.length<10 || l.length>10)
  {
   alert("enter the valid mob no");
   return false;
  }
  if(m.value.trim()=="")
  {
   alert("enter the psw");
   return false;
  }
  if(n.value.trim()=="")
  {
   alert("enter the pswd");
   return false;
  }
   if(n.value!=m.value)
   {
		alert("Mismatched password...");
		return false;
   }
  if(!o.checked)
  {
   alert("click the checkbox");
   return false;
  }
 return true;
 }
 </script>
 <body>
 <div class="container-fluid" class="jumbotron text-center">
		<div class="row well">
			  <div class="col-sm-2"><img class="img-circle" height="70px" width="70px" src="images/agrilogo.jpg"></div>
			  <div class="col-sm-7"><h1 width="100%"align="center">AGRI HELPLINE SYSTEM</h1></div>
			  <div class="col-sm-1"><h4><span class="glyphicon glyphicon-home"><a href="agri_homepage.py" target="_blank">HOME</h4></a></span></div>
		</div>
		<div class="row">
		<div class="col-sm-1"> . </div>
		<div class="col-sm-10"> 
                  <h1 align="center">Registration Form</h1>
                 <form action="#" method="post" onsubmit="return validate()" enctype="multipart/form-data">
                  <table align="center" cellspacing="5" cellpadding="7" >""")
print("""<tr><td>ID:</td><td><input type="text" name="genuserid" readonly value='%s'></td></tr>"""%(genuserid))
print("""<tr><td>Name:</td><td><input type="text" name="name" id="name1"></td></tr>
                   <tr><td>D.O.B:</td><td><input type="date" name="bday" id="dob1"></td></tr>
                   <tr><td>GENDER:</td><td><input type="radio" id="gen1" value="male" name="gen">Male<input type="radio" id="gen2" value="female" name="gen">Female</td></tr>
                   <tr><td>COMPANY NAME:</td><td><input type="text" name="company" id="cmpy1" placeholder="Address"></td></tr>
                   <tr><td>ADDRESS:</td><td><textarea rows="3" cols="20" name="address" id="address1" placeholder="Address"></textarea></td></tr>
                   <tr><td>DISTRICT:</td><td> <select name="district" id="district1">
                   <option></option>
                   <option>Virudhunagar</option>
                   <option>Madurai</option>
                   <option>Coimbatore</option>
                   <option>Chennai</option>
                   <option>Tirunelveli</option>
                   </select></td></tr>
                   <tr><td>STATE:</td><td><input type="text" id="state1" name="state" placeholder="State"></textarea></td></tr>
                   <tr><td>EMAIL:</td><td><input type="email" name="emailid" placeholder="@gmail.com" id="email1"></td></tr>
                   <tr><td>CONTACT No:</td><td><input type="text" name="phno" id="phno1"></td></tr>
                   <tr><td>CREATE PASSWORD:</td><td><input type="password"  id="psw1" name="pass1" placeholder="Enter_password"></td></tr>
                   <tr><td>CONFIRM PASSWORD:</td><td><input type="password" id="pswd1" name="pass2" placeholder="Reenter_password"></td></tr>
                   <tr><td>PHOTO UPLOAD:</td><td><input type="file" name="pht"></td></tr>
                   <tr align="center"><td colspan="2"><input type="checkbox" id="ch1">I Accept All The Data Is True</td></tr>
                   <tr align="center"><td colspan="2"><input type="submit" name="sub" value="submit"><input type="reset" value="clear"></td></tr>
                  </table>
                 </form>
         </div>
        <div class="col-sm-1"></div>
        </div>
</div>                    
</body>
</html>
""")
f=cgi.FieldStorage()
if len(f)==0:
    psub=None
else:
    pgenid=f.getvalue('genuserid')
    pname=f.getvalue('name')
    pdob=f.getvalue('bday')
    pgen=f.getvalue('gen')
    pcmpy=f.getvalue('company')
    padd=f.getvalue('address')
    pdist=f.getvalue('district')
    pstate=f.getvalue('state')
    pemail=f.getvalue('emailid')
    pcontact=f.getvalue('phno')
    pcreate=f.getvalue('pass1')
    pconfirm=f.getvalue('pass2')
    pphto=f['pht']
    psub=f.getvalue('sub')


if psub!=None:

    if pphto.filename:
        fn = os.path.basename(pphto.filename)
        open("images/" + fn, 'wb').write(pphto.file.read())

        q1="""INSERT INTO genuser_reg_details(genuser_id,name,dob,gender,companyname,address,district,state,email,contactno,createpassword, confirmpassword,photoupload) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(pgenid,pname,pdob,pgen,pcmpy,padd,pdist,pstate,pemail,pcontact,pcreate,pconfirm,fn)

        import smtplib
        fromaddr='agrihelplinesystem2020@gmail.com'
        password ='agrihelplinesystem'
        toaddrs=pemail
        msg="""
        Hi,
        Username: %s
        Password: %s
        """ %(pemail,pconfirm)

        try:
            server=smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromaddr,password)
            server.sendmail(fromaddr,toaddrs,msg)
            server.quit()
            cur.execute(q1)
            conn.commit()
            print("""<script>alert("Mail sent!!");</script>""")
        except:
            print("""<script>alert("Mail not sent!!");</script>""")
        conn.close()

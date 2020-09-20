#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")


import cgi,os,cgitb;cgitb.enable(),
import pymysql

conn=pymysql.connect("localhost","root","","myproject")
cur=conn.cursor()
q1="""select max(id) from agrireg_details"""
cur.execute(q1)
r=cur.fetchone()
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
agrioffid="agrioff"+z+str(n+1)


print("""
<html>
<head>
 <title>Admin page</title>
   <link rel="icon" type="images/ico" href="images/icon.jpg">
   <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
   <link rel="stylesheet" type="text/css" href="bootstrap/styleTV.css">
   <script src="bootstrap/jquery/jquery.min.js"></script>
   <script src="bootstrap/js/bootstrap.min.js"></script>
   <script language="javascript" type="text/javascript" src="username.js"></script>
   <link rel="icon" type="image/ico" href="images/tv_logo.png">
   <script type="text/javascript">
	$(function()
	{
		$(this).bind('contextmenu',function()
		{
			return false;
		})
	})

 </script>
<style>
body
{
margin: 0;
padding: 0;
}
table
{
background:;
color:black;
font-size:16px;
font-family:serif;
width:40%;
height:90%;
}
</style>
</head>
<body>
<div id="header">
	<div class="w3-container w3-teal">
		<nav class="navbar navbar-inverse" style="background-color:transparent;border:none;">
			<div class="container-fluid">
				<div class="row">
					<div class="col-sm-2">
						<img src="images/agrilogo.jpg" class="img-responsive img-circle" height="70px" width="70px" style="margin-top:8px;">
					</div>
					<div class="col-sm-6">
						<p id="font_head">AGRI HELPLINE SYSTEM</p>
					</div>
					<div class="col-sm-4">
						<div class="navbar-header">
							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
								<span class="icon-bar"></span>
								<span class="icon-bar "></span>
								<span class="icon-bar"></span>                        
							</button>
							<a class="navbar-brand" href="#"></a>
						</div>
						<div class="collapse navbar-collapse" id="myNavbar" style="float:right;">	  
							<ul class="nav navbar-nav" style="padding:20px;color:white;">
								<li style="padding-left:5px;padding-top:10px;color:red;" id="font_menu"><p id="name">Admin</p></li>
								<li style="padding-left:5px;"><a href="index.py" id="font_menu"><span class="glyphicon glyphicon-log-out"></span>&nbsp Logout</a></li>	
							</ul>
						</div>
					</div>
				</div>
			</div>
		</nav>
	</div>	
</div>


<!-- Body content-->
<div id="content_body">	

     <!-- Dashboard -->	
	<div id="throbber" style="display:none; min-height:120px;"></div>
		<div id="noty-holder"></div>
			<div id="wrapper">
				<div class="collapse navbar-collapse navbar-ex1-collapse" role="navigation">
					<div class="navbar-header">
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<a class="navbar-brand" href="http://cijulenlinea.ucr.ac.cr/dev-users/"></a>
					</div>
					<ul class="nav navbar-nav side-nav">
						<li>
							<a href="#" data-toggle="collapse" data-target="#submenu-1" id="font_dash"><i class="fa fa-fw fa-search"></i>Agri officer<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:100px;"></span></a>
							<ul id="submenu-1" class="collapse">
								<li><a href="adm_agrioff_add.py" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>Add</a></li>
								<li><a href="adm_agrioff_view.py" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>View</a></li>
							</ul>
						</li>
						<li>
							<a href="adm_farmer_view.py" data-toggle="collapse" data-target="#submenu-2" id="font_dash"><i class="fa fa-fw fa-star"></i>Farmer<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
						</li>
						<li>
							<a href="adm_student_view.py" data-toggle="collapse" data-target="#submenu-3" id="font_dash"><i class="fa fa-fw fa-star"></i>Agri student<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:160px;"></span></a>
						</li>
						<li>
							<a href="adm_genuser_view.py" data-toggle="collapse" data-target="#submenu-3" id="font_dash"><i class="fa fa-fw fa-star"></i>General user<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:160px;"></span></a>
						</li>
						<li>
							<a href="#" data-toggle="collapse" data-target="#submenu-4" id="font_dash"><i class="fa fa-fw fa-star"></i>Market details<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:70px;"></span></a>
						</li>
						<li>
							<a href="#" data-toggle="collapse" data-target="#submenu-5" id="font_dash"><i class="fa fa-fw fa-star"></i>Government schemes<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:15px;"></span></a>
							<ul id="submenu-5" class="collapse">
								<li><a href="adm_govtschm_update.py" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>update</a></li>
							    <li><a href="adm_govtschm_view.py" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>view</a></li> 
							</ul>
						</li>
					</ul>
				</div>	
			</div>
		</div>

		<!-- Page content -->
		<div style="margin-left:260px;margin-top:100px;">
			<div id="page-wrapper">
				<div class="container-fluid">
					<div class="row" id="main">
						<div class="col-sm-12 col-md-12 well">

 <h1 align="center">Registration Form</h1>
 <form action="#" method="post" onsubmit="return validate()" enctype="multipart/form-data">
  <table align="center" cellspacing="5" cellpadding="7" >""")
print("""<tr><td>ID:</td><td><input type="text" name="agrioffid" readonly value='%s'></td></tr>"""%(agrioffid))
print("""<tr><td>Name:</td><td><input type="text" name="name" id="name1"></td></tr>
   <tr><td>D.O.B:</td><td><input type="date" name="bday" id="dob1"></td></tr>
   <tr><td>GENDER:</td><td><input type="radio" id="gen1" value="male" name="gen">Male<input type="radio" id="gen2" value="female" name="gen">Female</td></tr>
   <tr><td>QUALIFICATION:</td><td>
    <select name="qualification" id="qual1">
     <option></option>
     <option>B.E</option>
     <option>B.sc</option>
     <option>Master Degree</option>
    </select>
	<tr><td>WORK EXPERIENCE:</td><td><input type="text" id="exp1"  name="experience" placeholder="experience"></td></tr>
   <tr><td>WORK LOCATION:</td><td><input type="text" id="loc1"  name="location" placeholder="location"></td></tr>
   <tr><td>ADDRESS:</td><td><textarea rows="3" cols="20" name="address" id="address1" placeholder="Address"></textarea></td></tr>
   <tr><td>DISTRICT:</td><td> <select name="district" id="district1">
   <option></option>
   <option>Virudhunagar</option>
   <option>Madurai</option>
   <option>Coimbatore</option>
   <option>Chennai</option>
   <option>Tirunelveli</option>
   </select></td></tr>
   <tr><td>STATE:</td><td><input type="text" id="state1" name="state" placeholder="State"></td></tr>
   <tr><td>EMAIL:</td><td><input type="email" name="emailid" placeholder="@gmail.com" id="email1"></td></tr>
   <tr><td>CONTACT No:</td><td><input type="text" name="phno" id="phno1"></td></tr>
   <tr><td>CREATE PASSWORD:</td><td><input type="password"  id="psw1" name="pass1" placeholder="Enter_password"></td></tr>
   <tr><td>CONFIRM PASSWORD:</td><td><input type="password" id="pswd1" name="pass2" placeholder="Reenter_password"></td></tr>
   <tr><td>PHOTO UPLOAD:</td><td><input type="file" name="pht"></td></tr>      
   <tr align="center"><td colspan="2"><input type="submit" name="sub" value="submit"><input type="reset" value="clear"></td></tr>
  </table>
 </form>


						</div>
					</div>
				</div>
			</div>
		</div>

	</div>
</div>
</body>
<script>
 function validate()
 {
  var a,b,c,d,e,h,i,j,k,l,m,n;
  a=document.getElementById("name1");
  b=document.getElementById("dob1");
  c=document.getElementById("gen1").checked==false;
  d=document.getElementById("gen2").checked==false;
  e=document.getElementById("qual1");
  f=document.getElementById("exp1");
  g=document.getElementById("loc1");
  h=document.getElementById("address1");
  i=document.getElementById("district1");
  j=document.getElementById("state1");
  k=document.getElementById("email1");
  l=document.getElementById("phno1").value;
  m=document.getElementById("psw1");
  n=document.getElementById("pswd1");
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
   alert("enter the exp");
   return false;
  }if(g.value.trim()=="")
  {
   alert("enter the location");
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
   return true;
 }
 </script>

</html>
""")

f=cgi.FieldStorage()
if len(f)==0:
    psub=None
else:
        pagid=f.getvalue('agrioffid')
        pname=f.getvalue('name')
        pdob=f.getvalue('bday')
        pgen=f.getvalue('gen')
        pqual=f.getvalue('qualification')
        pworkex=f.getvalue('experience')
        pworkloc=f.getvalue('location')
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

            q1="""INSERT INTO agrireg_details(agrioff_id,name,dob,gender,qualification,workexperience,worklocation,address,district,state,email,contactno,createpassword,confirmpassword,photoupload) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""  %(pagid,pname,pdob,pgen,pqual,pworkex,pworkloc,padd,pdist,pstate,pemail,pcontact,pcreate,pconfirm,fn)

            import smtplib
            fromaddr='agrihelplinesystem2020@gmail.com'
            password ='agrihelplinesystem'
            toaddrs=pemail

            msg="""
            Hi,
            Username: %s
            Password: %s
            """ %(pemail,pcreate)

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

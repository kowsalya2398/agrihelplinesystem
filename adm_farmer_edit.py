#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi,cgitb;cgitb.enable()
import pymysql


print("""
<html>
<head>
 <title>farmer edit page</title>
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

</head>
<body>
<div id="header">
	<div class="w3-container w3-teal">
		<nav class="navbar navbar-inverse" style="background-color:transparent;border:none;">
			<div class="container-fluid">
				<div class="row">
					<div class="col-sm-2">
						<img src="images/agrilogo.jpg" class="img-responsive img-circle"  height="75px" width="75px" style="margin-top:8px;">
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
								<li style="padding-left:5px;"><a href="agri_homepage.py" id="font_menu"><span class="glyphicon glyphicon-log-out"></span>&nbsp Logout</a></li>	
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
						<div class="col-sm-12 col-md-12 well">""")

conn=pymysql.connect("localhost","root","","myproject")
cur=conn.cursor()

f=cgi.FieldStorage()

if len(f)==1:
    pid=f.getvalue('id')
else:
    pid = f.getvalue('id')
    pfarid = f.getvalue('farmerid')
    pName = f.getvalue('name')
    pdob = f.getvalue('bday')
    pgen = f.getvalue('gen')
    pqual = f.getvalue('qualification')
    padd = f.getvalue('address')
    pdist = f.getvalue('district')
    pstate = f.getvalue('state')
    pemail = f.getvalue('emailid')
    pcontact = f.getvalue('phno')
    pcreate = f.getvalue('pass1')
    pconform = f.getvalue('pass2')
    pphto = f.getvalue('pht')
    psub = f.getvalue('sub')

    if psub!=None:
        q1="""update farmer_reg_details set farmerid='%s',Name='%s',DOB='%s',Gender='%s',Qualification='%s',Address='%s',District='%s',State='%s',Email='%s',Contactno='%s',Createpassword='%s',Confirmpassword='%s',photoupload='%s' where id='%s'""" %(pfarid,pName,pdob,pgen,pqual,padd,pdist,pstate,pemail,pcontact,pcreate,pconform,pphto,pid)
        cur.execute(q1)
        conn.commit()
        print("""
        <script>
        alert("data updated successfully");
        </script>
        """)
q="""select * from farmer_reg_details where id=%s""" %(pid)
cur.execute(q)
r=cur.fetchone()

print(""" <h1 align="center">Registration Form</h1>
             <form action="#" method="get">
                <table align="center" cellspacing="5" cellpadding="7" >
                     <input type="hidden" name="id" value=%s>
                     <tr><td>ID:</td><td><input type="text" name="farmerid" value='%s'></td></tr>
                     <tr><td>Name:</td><td><input type="text" name="name" value='%s'></td></tr>
                     <tr><td>D.O.B:</td><td><input type="date" name="bday" ></td></tr>
                     <tr><td>GENDER:</td><td><input type="radio" value="male" name="gen">Male<input type="radio" id="gen2" value="female" name="gen">Female</td></tr>
                     <tr><td>QUALIFICATION:</td><td>
                        <select name="qualification">
                           <option></option>
                           <option>Below 8th</option>
                           <option>Above 8th</option>
                           <option>Any Degree</option>
                        </select>
                     <tr><td>ADDRESS:</td><td><textarea rows="3" cols="20" name="address">%s</textarea></td></tr>
                     <tr><td>DISTRICT:</td><td> 
                        <select name="district">
                           <option></option>
                           <option>Virudhunagar</option>
                           <option>Madurai</option>
                           <option>Coimbatore</option>
                           <option>Chennai</option>
                           <option>Tirunelveli</option>
                        </select>
                     </td></tr>
                     <tr><td>STATE:</td><td><input type="text" name="state"value='%s'></td></tr>
                     <tr><td>EMAIL:</td><td><input type="email" name="emailid" value='%s'></td></tr>
                     <tr><td>CONTACT No:</td><td><input type="text" name="phno" value='%s'></td></tr>
                     <tr><td>CREATE PASSWORD:</td><td><input type="password" name="pass1" value='%s'></td></tr>
                     <tr><td>CONFIRM PASSWORD:</td><td><input type="password" name="pass2" value='%s'></td></tr>
                     <tr><td>PHOTO UPLOAD:</td><td><input type="file" name="pht" value='%s'></td></tr>      
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
</html>"""%(r[0],r[1],r[2],r[6],r[8],r[9],r[10],r[11],r[12],r[13]))
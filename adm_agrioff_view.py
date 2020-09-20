#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi
import pymysql
import cgitb
cgitb.enable()


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
						<p id="font_head">AGRI HELPLINE SYSTEM </p>
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
						<div class="col-sm-12 col-md-12 well"></html>""")

f = cgi.FieldStorage()
pagid = f.getvalue('agrioffid')
pName = f.getvalue('name')
pdob = f.getvalue('bday')
pgen = f.getvalue('gen')
pqual = f.getvalue('qualification')
pworkex = f.getvalue('experience')
pworkloc = f.getvalue('location')
padd = f.getvalue('address')
pdist = f.getvalue('district')
pstate = f.getvalue('state')
pemail = f.getvalue('emailid')
pcontact = f.getvalue('phno')
pcreate = f.getvalue('pass1')
pconform = f.getvalue('pass2')

conn = pymysql.connect("localhost", "root", "", "myproject")
cur = conn.cursor()

q2 = """SELECT * FROM agrireg_details"""
try:
    cur.execute(q2)
    res = cur.fetchall()
except:
    conn.close()

print("""
<table border="1">
    <tr>
        <th>Agrioffid</th>
        <th>Name</th>
        <th>DOB</th>
        <th>Gender</th>
        <th>Qualification</th>
        <th>Workexperience</th>
        <th>Worklocation</th>
        <th>Address</th>
        <th>District</th>
        <th>State</th>
        <th>Email</th>
        <th>Contactno</th>
        <th>Createpassword</th>
        <th>Confirmpassword</th>
        <th>Photo upload</th>
        <th>update</th>
        <th>delete</th>
    </tr>
""")
for i in res:
    print("""
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><a href="adm_agrioff_edit.py?id=%s">Edit</a></td>
                <td><a href="adm_agrioff_delete.py?id=%s">Delete</a></td>
           </tr>
           """ % (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[0], i[0]))
print("</table>")

print("""

 						</div>
					</div>
				</div>
			</div>
		</div>

	</div>
</div>
</body>
""")


#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi
import pymysql

f=cgi.FieldStorage()
pid=f.getvalue('id')
pevt=f.getvalue('evt')
pchgt=f.getvalue('chgt')
ppla=f.getvalue('pla')
pdte=f.getvalue('dte')
ptmefr=f.getvalue('tmefr')
ptmeto=f.getvalue('tmeto')
psub=f.getvalue('sub')


print("""
<html>
<head>
 <title>Agriofficer page</title>
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
color:black;
font-size:16px;
font-family:serif;
width:40%;
height:50%;
text-align:-webkit-center;
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
						<img src="images/agrilogo.jpg" class="img-responsive img-circle"  height="100px" width="100px" style="margin-top:8px;">
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
								<li style="padding-left:5px;padding-top:10px;color:red;" id="font_menu"><p id="name">agri_officer</p></li>
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
					<ul class="nav navbar-nav side-nav">""")
print("""							<li>
							<a href="agrioff_profile.py?id=%s" data-toggle="collapse" data-target="#submenu-1" id="font_dash"><i class="fa fa-fw fa-search"></i>Profile<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:100px;"></span></a>
							
						</li>
						<li>
			  <a href="#" data-toggle="collapse" data-target="#submenu-2" id="font_dash"><i class="fa fa-fw fa-star"></i>Soil Information<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
						    <ul id="submenu-2" class="collapse">
								<li><a href="agrioff_soil_update.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>Upload</a></li>
								<li><a href="agrioff_soil_view.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>View</a></li>
							</ul>
						</li>
						<li>
							<a href="#" data-toggle="collapse" data-target="#submenu-3" id="font_dash"><i class="fa fa-fw fa-star"></i>Crop Information<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:160px;"></span></a>
						    <ul id="submenu-3" class="collapse">
								<li><a href="agrioff_crop_update.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>Upload</a></li>
								<li><a href="agrioff_crop_view.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>View</a></li>
							</ul>
						</li>
                        <li>
							<a href="#" data-toggle="collapse" data-target="#submenu-4" id="font_dash"><i class="fa fa-fw fa-star"></i>Event<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:160px;"></span></a>
						    <ul id="submenu-4" class="collapse">
								<li><a href="agrioff_event_update.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>Upload</a></li>
								<li><a href="agrioff_event_view.py?id=%s" id="font_dashmenu"><i class="fa fa-angle-double-right"></i>View</a></li>
							</ul>
						</li>
						<li>
							<a href="agrioff_reply.py?id=%s" data-toggle="collapse" data-target="#submenu-5" id="font_dash"><i class="fa fa-fw fa-star"></i>Queries<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:160px;"></span></a>
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
                               <h1 align="center">Event Form</h1>
                                  <form action="#" method="post">
                                    <table align="center" cellspacing="3" cellpadding="5"> 
                                       <tr><td> Event Name:</td><td><input type="text" name="evt"></td></tr>
                                       <tr><td>Chiefguest:</td><td><input type="text" name="chgt"></td></tr>
                                       <tr><td>Place:</td><td><input type="text" name="pla"></td></tr>
                                       <tr><td>Date:</td><td><input type="date" name="dte"></td></tr>
                                       <tr><td>From:</td><td><input type="time" name="tmefr"></td><td>To:</td><td><input type="time" name="tmeto"></td></tr>
                                       <tr align="center"><td colspan="2"><input type="submit" name="sub" value="submit"><input type="reset" name="clr" value="clear"></td></tr>
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
</html>"""
%(pid,pid,pid,pid,pid,pid,pid,pid))

if psub!=None:
    conn=pymysql.connect("localhost","root","","myproject")
    cur=conn.cursor()

    q1="""INSERT INTO event(Eventname,Chiefguest,Place,Date,Timefrom,Timeto) VALUES('%s','%s','%s','%s','%s','%s')""" %(pevt,pchgt,ppla,pdte,ptmefr,ptmeto)

    cur.execute(q1)
    conn.commit()

    print("""<script>alert("Event uploaded!!");</script>""")

    conn.close()
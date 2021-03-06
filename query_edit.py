#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi
import pymysql,cgitb;cgitb.enable()

conn=pymysql.connect("localhost","root","","myproject")
cur=conn.cursor()

f=cgi.FieldStorage()
if len(f)==2:
    pid=f.getvalue("id")
    reqid=f.getvalue("reqid")
    psub=None
else:
    pid = f.getvalue('id')
    pagid=f.getvalue('agoffid')
    reqid = f.getvalue('reqid')
    prep=f.getvalue('rep')
    psub = f.getvalue('sub')

    q="""update queries set Reply='%s',Rep_id='%s' where id=%s""" %(prep,pagid,reqid)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    alert("Reply sent...");
    location.href="agrioff_reply.py?id=%s";
    </script>
    """ %(pid))

q1="""select Agrioffid from agrireg_details where id=%s""" %(pid)
cur.execute(q1)
r=cur.fetchone()

q2="""select Request from queries where id=%s""" %(reqid)
cur.execute(q2)
res=cur.fetchone()

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
</head>
<body>
<div id="header">
	<div class="w3-container w3-teal">
		<nav class="navbar navbar-inverse" style="background-color:transparent;border:none;">
			<div class="container-fluid">
				<div class="row">
					<div class="col-sm-2">
						<img src="images/agrilogo.jpg" class="img-responsive img-circle"  height="100px" width="100px"  style="margin-top:8px;">
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
					<ul class="nav navbar-nav side-nav">
						<li>
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
                            <form action="#" method="get">
                               <table align = "center" cellspacing = "5" cellpadding = "7">"""%(pid,pid,pid,pid,pid,pid,pid,pid))
print("""                           <input type="hidden" name="id" value=%s>
                                    <tr><td>Agriofficer Id:</td><td><input type="text" name="agoffid" readonly value='%s'></td></tr>
                                    <tr><td>Req Id:</td><td><input type="text" name="reqid" readonly value='%s'></td></tr>
                                    <tr><td>REQUEST:</td><td><textarea rows="4" cols="20" name="req">%s</textarea></td></tr>
                                    <tr><td>REPLY:</td><td><textarea rows="4" cols="20" name="rep"></textarea></td></tr>
                                    <tr align="center"><td colspan="2"><input type="submit" name="sub" value="send"><input type="reset" value="clear"></td></tr>
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
</html>"""%(pid,r[0],reqid,res[0]))

#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

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
    background-image:url("images/k6.jpg");
    background-size:cover;
    background-position:center;
    font-family:sans-serif;
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
						<img src="images/agrilogo.jpg" class="img-responsive img-circle" height="100px" width="100px" style="margin-top:8px;">
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
						<div class="col-sm-12 col-md-12 well">



						</div>
					</div>
				</div>
			</div>
		</div>

	</div>
</div>
</body>
</html>
""")
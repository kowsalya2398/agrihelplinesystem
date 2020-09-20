#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi

f = cgi.FieldStorage()
id = f.getvalue("id")
pid = f.getvalue("id")

print("""
<!doctype html>
<html>
<head>
 <title>Student profile</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
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
                        <li style="padding-left:5px;padding-top:10px;color:red;" id="font_menu"><p id="name">Employee</p></li>
                        <li style="padding-left:5px;"><a href="cat.html" id="font_menu"><span class="glyphicon glyphicon-log-out"></span>&nbsp Logout</a></li> 
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
           				<a href="student_profile.py?id=%s" data-toggle="collapse" data-target="#submenu-1" id="font_dash"><i class="fa fa-fw fa-search"></i>Profile<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:100px;"></span></a>
                       	</li>
                       	<li>
							<a href="student_soil_view.py?id=%s" data-toggle="collapse" data-target="#submenu-2" id="font_dash"><i class="fa fa-fw fa-star"></i>Soil Information<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
						</li>
						<li>
							<a href="student_crop_view.py?id=%s" data-toggle="collapse" data-target="#submenu-3" id="font_dash"><i class="fa fa-fw fa-star"></i>Crop information<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
						</li>
						<li>
							<a href="student_govtschm_view.py?id=%s" data-toggle="collapse" data-target="#submenu-3" id="font_dash"><i class="fa fa-fw fa-star"></i>Government Schemes<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
						</li>
						<li>
							<a href="student_query_req.py?id=%s" data-toggle="collapse" data-target="#submenu-4" id="font_dash"><i class="fa fa-fw fa-star"></i>Queries<i class="fa fa-fw fa-angle-down pull-right"></i><span style="padding-left:138px;"></span></a>                    
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
                  <div class="col-sm-12 col-md-12 well">""" % (pid, pid, pid, pid, pid))
conn = pymysql.connect("localhost", "root", "", "myproject")
cur = conn.cursor()
s1 = """select * from student_reg_details where Id=%s""" % (id)
cur.execute(s1)
i = cur.fetchone()
print("""
      <table>
      <tr><td colspan="2" ><img src="%s" height="75" width="75" style="border-radius:50px;"></td></tr>
      <tr><th>Studentid</th><td>%s</td></tr>
      <tr><th>name</th><td>%s</td></tr>
      <tr><th>dob</th><td>%s</td></tr>
      <tr><th>gender</th><td>%s</td></tr>
      <tr><th>qualification</th><td>%s</td></tr>
      <tr><th>college</th><td>%s</td></tr>
      <tr><th>address</th><td>%s</td></tr>
      <tr><th>district</th><td>%s</td></tr>
      <tr><th>state</th><td>%s</td></tr>
      <tr><th>email</th><td>%s</td></tr>
      <tr><th>contactno</th><td>%s</td></tr>
      <tr><th>createpassword</th><td>%s</td></tr>
      <tr><th>conformpassword</th><td>%s</td></tr>
      <td><a href="adm_student_edit.py?id=%s">Edit</a></td>

      """ % ("images/" + i[14], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[0]))
print("</table>")
conn.close()
print("""

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
#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

import cgi
import pymysql

print("""
<html>
 <head>
  <title>farmer login</title>
   <link rel="icon" type="images/ico" href="images/icon.jpg">
  	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
<style>
     body 
      {
         background-color: #d9edf7;
         background: url(images/o8.jpg) no-repeat center center fixed ; 
         background-size: cover;
         margin-top: none;
    
       } 
    .loginbox
    {
    width:320px;
    height:450px;
    background:;
    color:black;
    top:75%;
    left:50%;
    position:absolute;
    transform:translate(-50%,-50%);
    box-sizing:border-box;
    padding:70px 30px;
    }
    .ref
    {
    width:100px;
    height:100px;
    border-radius:50%;
    position:absolute;
    top:-50px;
    left:calc(50% - 50px);
    }
    h1
    {
    margin:0;
    padding:0 0 20px;
    text-align:center;
    font-size:22px;
    }
    .loginbox p
    {
    margin:0;
    padding: 0;
    font-weight:bold;
    }
                .loginbox input
                {
                width:100%;
                margin-bottom:18px;
                }
                .loginbox input[type="text"],input[type="password"]
                {
                border:none;
                border-bottom:1px solid #fff;
                background:transparent;
                outline:none;
                height:40px;
                color:#fff;
                font-size:16px;
                }
                .loginbox input[type="submit"]
                {
                border:none;
                outline:none;
                height:40px;
                background:white;
                color:black;
                font-size:18px;
                border-radius:20px;
                }
                .loginbox input[type="submit"]:hover
                {
                cursor:pointer;
                background:pink;
                color:black;
                }
                .loginbox input[type="reset"]
                {
                border:none;
                outline:none;
                height:40px;
                background:white;
                color:black;
                font-size:18px;
                border-radius:20px;
                text-align: center;
                }
                .loginbox input[type="reset"]:hover
                {
                cursor:pointer;
                background:pink;
                color:black;
                }
                .loginbox a
                {
                text-decoration:none;
                font-size:16px;
                line-height:20px;
                color:white;
                }
                .loginbox a:hover
                {
                color:blue;
                }
</style>	
</head>
<script>
	 function validate()
	 {
	  var a,b;
	  a=document.getElementById("uname");
	  b=document.getElementById("pwd");
	  if(a.value==""||b.value=="")
	  {
	  alert("Enter the user name and Enter the password");
	  return false;
	  }
	 return true;
	 }
	</script>
<body>
	<div class="container-fluid" class="jumbotron text-center">
		<div class="row well">
		     <div class="col-sm-2"><img class="img-circle" height="75px" width="75px" src="images/agrilogo.jpg"></div>
			 <div class="col-sm-7"><h2 width="100%" ><b class="text-default">FARMER LOGIN</b></h2></div>
			 <div class="col-sm-3"><h3 width="100%"><b class="pull-right glyphicon glyphicon-home">&nbsp;<a href="agri_homepage.py" target="_blank">HOME</b></h3></a></div>
		</div>
   </div> 
<div class="loginbox">
<img src="images/log.jpg" class="ref">
<h1>LOGIN FORM</h1>
<form action="#" method="get" onsubmit="return validate()">
	<p>User Name:</p><input type="text" name="uname" id="uname">
	<p>Password:</p><input type="password" name="pwd" id="pwd">
	<input type="submit" value="submit" name="sub"><input type="reset" value="cancel" name="can">
	<a href="#">forget password</a><br><a href="farmer_reg.py" id="new">new user<i>register here</i></a>
	</form>
</div> 
</body>
</html>
""")

f = cgi.FieldStorage()
uname = f.getvalue("uname")
pwd = f.getvalue("pwd")
sub = f.getvalue("sub")

conn = pymysql.connect("localhost", "root", "", "myproject")
cur = conn.cursor()

if sub != None:

    q = """select id from farmer_reg_details where email='%s' and confirmpassword='%s'""" % (uname, pwd)

    cur.execute(q)

    res = cur.fetchone()

    if res != None:
        print("""<script>location.href="farmer_page.py?id='%s'";</script>"""%(res[0]))
    else:
        print("""<script>alert("Invalid data");</script>""")


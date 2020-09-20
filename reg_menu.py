#!C:/Users/KowsRaji/AppData/Local/Programs/Python/Python37/python.exe
print("content-type:html \r\n\r\n")

print("""
<html>
<head>
<title>Register menu</title>
 <link rel="icon" type="images/ico" href="images/icon.jpg">
<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
<style>
body
    {
    margin: 0;
    padding: 0;
    background-image:url("images/ab5.jfif");
    background-size:cover;
    background-position:center;
    font-family:sans-serif;
    }
</style>
</head>
<body id="image">
   <div class="container-fluid" class="jumbotron text-center">
		<div class="row well">
			<div class="col-sm-1"><img class="img-circle" height="65 px" width="65px" src="images/agrilogo.jpg"></div>
			<div class="col-sm-10"><h1 width="100%" align="center">REGISTER</h1></div>
			 <div class="col-sm-1"><h5><span class="glyphicon glyphicon-home"><a href="Faq.html" target="_blank">HOME</h5></a></span></div>
		    </div>
		<div class="row">
   		    <div class="list-group">
		       <div class="col-sm-4"></div>
			    <div class="col-sm-4">
                        <h3><a href="farmer_reg.py" class="list-group-item list-group-item-danger" target="_blank"><span class="glyphicon glyphicon-edit">FARMER</span></a></h3>
                        <h3> <a href="student_reg.py" class="list-group-item list-group-item-warning"target="_blank"><span class="glyphicon glyphicon-edit">AGRI STUDENT</span></a></h3>
                        <h3><a href="genuser_reg.py" class="list-group-item list-group-item-info" target="_blank"><span class="glyphicon glyphicon-edit">GENERALUSER</span></a></h3>
                </div>
			   <div class="col-sm-4"></div>
		    </div>
        </div>
	</div>
</body>
</html>

""")
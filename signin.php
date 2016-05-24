
<?php
session_start();
if(isset($_SESSION['uname'])){
	header("Location:userint.php");
}
?>


<html lang="en">
<head>

	<meta charset="utf-8">
	<meta name ="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	<title>GoCrawl - Lets Crawl Smartly !</title>
		<link href="styles/aboutus.css" rel="stylesheet" style="text/css"</link>
		<link href="animation.css" rel="stylesheet" style="text/css"</link>
	<link href="styles/signin.css" rel="stylesheet" style="text/css"</link>
</head>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.6.3.min.js"></script>
<body>
<nav class="navbar navbar-default navbar-fixed-top" role = "navigation" >
	<div class = "navbar-header">
      <div class = "navbar-brand">
        <img class="logo" src="styles/images/h1.png">
      </div>
   </div>

   <div id="headermodify">
   	<ul class="nav navbar-nav navbar-right">
   		<!--<li class="links"><a href="aboutus.html">About Us</a></li>-->
   		<li class="active">
        <a href="signin.php"><b>Sign In</b></a></li>
   		<li class="links>"><a href="signup.html"><b>Sign Up<b></a></li>
   	</ul>
   </div>	
</nav>
<div class="container">
	<div class="col-md-4"></div>
	<div class="col-md-4">
	<form class="form-signin" action="userint.php" method="post">
		<div class="form-group">
			
				<input type="text" name="uname" class="form-control" id="usr" placeholder="Username" style="color: initial;" autocomplete="off" required autofocus>
			
		</div>
		<div class="form-group">
			
				<input type="password" name="password" class="form-control" id="pwd" placeholder="Password" style="color: initial;" autocomplete="off">
	
		</div>
			<div class="checkbox">
       			<label style="color: white;">
        	  	  <input type="checkbox" value="remember-me"> Remember me
          	</label>
    		</div>
        <button class="btn btn-lg btn-primary btn-block " type="submit" name="signin" onclick="userint.php" method="post">Sign in
	      </button>
    </form>
    </div>
    <div class="col-md-4"></div>
</div>
<div class="down">
	<a href="#aboutus"><div class="arrow-down">
</div>
</a>
</div>
<div class="container-fluid p1" id="aboutus">
      <div class="col-md-4"><img id="one" src="https://www.apifier.com/img/robot-apifier.png">
      </div>
      <div class="col-md-8">  
         <p>
          <h3>What's GoCrawl?</h3>
          <br><br>
  GoCrawl is a web crawler that extracts data from any website. It crawls the website to search data and thus is a basis for a search engine.
         </p>
      </div>
   </div>
   <div class="container-fluid p2">
      <div class="col-md-8">
         <p><h3>How It Works?</h3>
                   <br><br>
  It starts with a list of URL provided by the user. As it visits this URL, it identifies all the hyperlinks in the page and adds them to the list of URL's to visit. By a simple
  mechanism, it thus searches your given query within minutes.
         </p>
      </div>
      <div class="col-md-4"><img id="two" src="https://www.apifier.com/img/people.png">
      </div>
   </div>
   <!--
   <div class="container-fluid p3">
      <div class="col-md-4">
         <img id="three" src="https://www.apifier.com/img/vacuum-cleaner.png">
      </div>
      <div class="col-md-8">
         <p>
            <h3>Who needs this?</h3>
                      <br><br>
  GoCrawl is for anyone who needs data from the web. 
         </p>
   </div>
   </div>
   -->

<script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
<!--<script src="scripts/header.js"></script>
	Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</body>
</html>

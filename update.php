<?php
		session_start();
		if($_POST['oldpassword'] == $_SESSION['password']){
			define('DB_HOST','127.0.0.1');
			define('DB_Name','crawler');
			define('Tble_Name','users');
			define('DB_user','root');
			define('Password','');
			$con=mysql_connect(DB_HOST,DB_user,Password) or die("Connection Problem");
			$db=mysql_select_db(DB_Name) or die("failed to connect to mysql");
			$query="Update RegisteredUser set password='$_POST[newpassword]' ,email_id='$_POST[mail]' where username='$_POST[username]'";
				$que=mysql_query($query);
				echo $que;
				$query="Update User_details set dob='$_POST[dob]' ,email_id='$_POST[mail]' where email_id='$_SESSION[emailid]';";
				$que=mysql_query($query);
				echo $que;
				echo "User details fully updated";
			}

		else
			echo "Fuck! your old password and new password does not match Fuck you Bitch!!!";


?>
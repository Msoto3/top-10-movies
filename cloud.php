<?php 
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "demo";
    $con=mysqli_connect($servername,$username,$password,$dbname);
    if (!$con)
     {
        die("Failed to connect to MySQL: " . mysqli_connect_error());
     }

    $que = "SELECT * FROM movies";
    $res = $con->query($que);

?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Top 10</title>
    <style type="text/css">
    	body{
			background-color:#C47451;
		
		}
		header{
			text-align:center;
		}
		
		.movie-container{
			background-color: lightskyblue;
			width: 100%;
		}
    </style>
  </head>
  <body>
      <header>
        <h1>Top 10 Movies of All Time</h1>
        <h2>According to IMDb</h2>
      </header>
      <main >
      	<?php
          if($res->num_rows>0){
            while($row=$res->fetch_assoc()){
              printf(
                "
                  <div class='movie-container'>
                  	<span>%s.</span>
                    <img src='%s'>
                    <span>%s</span>
                    <span>(%s)</span>
                    
                  </div>
                  <br>
                ",$row['id'],$row['img'],$row['title'],$row['year']);
            }
          }
          $con->close();
          ?>
      </main>
  </body>
</html>
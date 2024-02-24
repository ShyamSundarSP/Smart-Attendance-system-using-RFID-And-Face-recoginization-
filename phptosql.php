
<?php

$servername = "localhost";
$database = "u394450735_clatson";
$username = "u394450735_clatson";
$password = "Game@123456789";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
$sql = "SELECT * FROM clatson WHERE username='clatson';";
$result = mysqli_query($conn, $sql);
$resultCheck = mysqli_num_rows($result);
if ($resultCheck > 0){
    while ($row = mysqli_fetch_assoc($result)){
        echo $row['email'];
        echo "<br>";
    }
}







$connection->close();

?>



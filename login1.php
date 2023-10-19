<?php
$server = "localhost";
$username = "root";
$password = ""; 
$database = "forza";

$conn = mysqli_connect($server, $username, $password, $database);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
$sql1="create table if not exists users(username varchar(30), password varchar(30), email varchar(20))";
mysqli_query($conn,$sql1);

if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $hashed_password = md5($password);
        $email = $_POST['email'];
     
    $sql = "INSERT INTO users (username, password, email) VALUES ('$username', '$hashed_password', '$email')";

    if (mysqli_query($conn, $sql)) {
        echo "User registered successfully.";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }

    mysqli_close($conn);
}
?>

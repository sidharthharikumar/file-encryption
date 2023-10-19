<?php
$dbServer = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "forza";

$conn = mysqli_connect($dbServer, $dbUsername, $dbPassword, $dbName);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if (isset($_POST["submit"])) {
    $file = $_FILES["fileToUpload"];

    if ($file["error"] === UPLOAD_ERR_OK) {
        $fileName = $file["name"];
        $fileTmpName = $file["tmp_name"];
        $fileSize = $file["size"];

        $sql = "INSERT INTO files (file_name, file_data) VALUES (?, ?)";
        $stmt = mysqli_prepare($conn, $sql);
        $null = NULL;
        mysqli_stmt_bind_param($stmt, "sb", $fileName, $null);
        $fileData = file_get_contents($fileTmpName);
        mysqli_stmt_send_long_data($stmt, 1, $fileData);

        if (mysqli_stmt_execute($stmt)) {
            echo "File uploaded and saved to the database successfully.";
        } else {
            echo "Error uploading file: " . mysqli_stmt_error($stmt);
        }

        mysqli_stmt_close($stmt);
    } else {
        echo "Error uploading file.";
    }
}

mysqli_close($conn);
?>

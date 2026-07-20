<?php
// Ini adalah file STUB untuk kebutuhan isolasi testing
$host = 'localhost';
$user = 'root';
$password = '';
$db = 'quiz_pengupil_test'; // Arahkan ke database khusus testing

$con = mysqli_connect($host, $user, $password, $db);
if (!$con) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
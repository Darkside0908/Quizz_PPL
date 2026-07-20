<?php
// GANTI host jadi 127.0.0.1 biar bisa konek via TCP di GitHub Actions
$host = '127.0.0.1';
$user = 'root';
$password = '';
$db = 'quiz_pengupil_test';

$con = mysqli_connect($host, $user, $password, $db);
if (!$con) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
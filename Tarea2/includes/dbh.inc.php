<?php 
//? dbh = data base handler
$serverName = "localhost";
$dBUserame = "root";
$dBPassword = "";
$dBName = "Tarea2";

$conn = mysqli_connect($serverName, $dBUserame, $dBPassword, $dBName);

if(!$conn){
    die("Fallo en la conexion". mysqli_connect_error());
}

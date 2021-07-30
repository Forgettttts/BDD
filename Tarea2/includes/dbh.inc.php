<?php 
//? dbh = data base handler
$serverName = "localhost";
$dBUserame = "root";
$dBPassword = "";
$dBName = "Tarea2"; //! REVISAR SI ES QUE ESTE ES EFECTIVAMENTE EL NOMBRE QUE DEBE TENER

$conn = mysqli_connect($serverName, $dBUserame, $dBPassword, $dBName);

if(!$conn){
    die("Fallo en la conexion". mysqli_connect_error());
}

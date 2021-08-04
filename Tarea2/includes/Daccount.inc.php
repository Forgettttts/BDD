<?php
$user=$_SESSION["usuario"];


$sql="DELETE FROM Usmers WHERE UserName =?);";
$stmt= mysqli_stmt_init($conn); // Iniciamos una accion en la conexion entregada
if (!mysqli_stmt_prepare($stmt, $sql)) { //revisamos que la conecion no falle
    header("location: ../publicaciones.php?error=ConexionFallida");
    exit();
}

mysqli_stmt_bind_param($stmt, "s", $user);// Ingresamos los datos
mysqli_stmt_execute($stmt);//ejecutamos lo anterior

mysqli_stmt_close($stmt);
header("location: ../index.php?error=none");
return mysqli_insert_id($conn);
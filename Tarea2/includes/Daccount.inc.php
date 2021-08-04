<?php
if (isset($_POST["UpdateCuenta"])) {
    require_once 'dbh.inc.php';
    require_once 'funciones.inc.php';
    session_start();
    $user= $_SESSION["usuario"];
    $newUser= $_POST["newuser"];
    $UsuarioExiste=UsuarioOcupado($conn, $username, $username); //? Si es que retorna false, es pq el usuario no se encontro
    if ($UsuarioExiste==false) {
        mysqli_query($conn, "UPDATE Usmer SET UserName = '$newUser' WHERE UserName = '$user'");
        header("location: ../identificarse.php?error=LogInAgain");
        exit();
    }
    else {
        header('location: ../perfil.php?error=UsuarioOcupado');
        exit();
    }
}
else {
    header("location: ../index.php");
    exit();
}
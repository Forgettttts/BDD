<?php

if (isset($_POST["submit"])) {
    $name = $_POST["nombre"];
    $username = $_POST["username"];
    $correo = $_POST["correo"];
    $pwd = $_POST["password"];
    $pwd2 = $_POST["password2"];

    require_once 'dbh.inc.php';
    require_once 'funciones.inc.php';

    //* Comenzamos con el manejo de errores

    if (EntradaVacia($name, $username, $correo, $pwd, $pwd2)!== false) {
        header(("location ../registrarse.php?error=EntradaVacia"));
        exit();
    }
    if (UsuarioInvalido($username)!== false) {
        header(("location ../registrarse.php?error=UsuarioInvalido"));
        exit();
    }
    if (CorreoInvalido($correo)!== false) {
        header(("location ../registrarse.php?error=CorreoInvalido"));
        exit();
    }
    //? Si es que las contraseñas son distintas
    if (pwdMatch($pwd, $pwd2)!== false) {
        header(("location ../registrarse.php?error=PasswordDistintas"));
        exit();
    }
    //? Si es que el usuario ya existe
    if (UsuarioOcupado($conn, $username, $correo)!== false) {
        header(("location ../registrarse.php?error=PasswordDistintas"));
        exit();
    }

    //* Si es que llegamos a este punto, es porque el usuario no cometio ningun error de input al registrarse

    //? Procedemos a crear el usuario
    CrearUsuario($conn, $name, $username, $correo, $pwd);
}
else {
    header("location ../registrarse.php");
    exit();
}
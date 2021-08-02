<?php
if (isset($_POST["submit"])) {
    $username= $_POST["username"];
    $pwd=  $_POST["password"];

    require_once 'dbh.inc.php';
    require_once 'funciones.inc.php';

    //* Comenzamos con el manejo de errores

    if (EntradaVaciaLogin($username, $pwd)!== false) {
        header("location: ../identificarse.php?error=EntradaVacia");
        exit();
    }

    //* Si es que llegamos a este punto, es porque el usuario no cometio ningun error de input al ingresar al USMer
    LoginUser($conn, $username, $pwd);
}
else {
    header("location: ../identificarse.php");
    exit();
}
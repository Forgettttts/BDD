<?php

if(isset($_POST["registrar"])){
    $name = $_POST["nombre"];
    $username = $_POST["username"];
    $pwd = $_POST["password"];
    $pwd2 = $_POST["password2"];

    require_once 'dbh.inc.php';
    require_once 'identificacion.inc.php';

}
else {
    header(("location ../registrarse.php"));
}
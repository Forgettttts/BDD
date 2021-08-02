<?php
if (isset($_POST["Publicar"])) {
    $mensaje= $_POST["mensaje"];
    $visibilidad=  $_POST["visibilidad"];

    require_once 'dbh.inc.php';
    require_once 'funciones.inc.php';

    //* Comenzamos con el manejo de errores

    if (LargoExcedido($mensaje)!== false) {
        header("location: ../usmitos.php?error=LargoErroneo");
        exit();
    }
    //? Se reutiliza una funcion del login
    if (EntradaVaciaLogin($mensaje, $visibilidad)!== false) {
        header("location: ../usmitos.php?error=EntradaVacia");
        exit();
    }
    if (VisibilidadErronea($visibilidad)!== false) {
        header("location: ../usmitos.php?error=VisibilidadErronea");
        exit();
    }

    //* Si es que llegamos a este punto, es porque el usuario no cometio ningun error de input al ingresar al USMer
    SubirUsmito($conn, $mensaje, $visibilidad, $_SESSION["usuario"]);
}
else {
    header("location: ../usmitos.php");
    exit();
}
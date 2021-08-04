<?php
if (isset($_POST["Publicar"])) {
    session_start();
    $mensaje= $_POST["mensaje"];
    $visibilidad=  $_POST["Visibilidades"];
    $tags= $_POST["tags"];

    require_once 'dbh.inc.php';
    require_once 'funciones.inc.php';

    //* Comenzamos con el manejo de errores

    if (LargoExcedido($mensaje)!== false) {
        header("location: ../usmitos.php?error=LargoErroneo");
        exit();
    }
    if (MensajeVacio($mensaje, $visibilidad)!== false) {
        header("location: ../usmitos.php?error=EntradaVacia");
        exit();
    }

    //* Si es que llegamos a este punto, es porque el usuario no cometio ningun error de input al ingresar al USMer
    $IdPublicacion=SubirUsmito($conn, $mensaje, $visibilidad, $_SESSION["usuario"]);
    SubirTags($conn, $tags, $_SESSION["usuario"], $IdPublicacion);
    /*
    if(HayTags($tags)){
        SubirTags($conn, $tags, $_SESSION["usuario"], $IdPublicacion);
    }
    */
}
else {
    header("location: ../usmitos.php");
    exit();
}
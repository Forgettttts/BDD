<?php 
    session_start();
?>

<!DOCTYPE html>
<html lang="es" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>USMwer</title>
        <link rel="stylesheet" href="css/style.css">
        <script src="https://kit.fontawesome.com/333e73cd55.js" crossorigin="anonymous"></script> <!-- Para iconos de cada publicacion-->
    </head>

    <body> 
        <nav>
            <div class="encabezado">
                <div style="display:inline-block;vertical-align:top;">
                    <a href="index.php"><img src="img/minilogo.png" width = "100" height = "100" alt="Logo pagina" style="float:center" style="vertical-align:bottom"></a>
                </div>
                <div style="display:inline-block;">
                    <h1>USMwer</h1>
                </div>

                <ul class="opciones_encabezado">
                    <a href="index.php" class="active">Inicio</a>
                    <?php
                    if (isset($_SESSION["usuario"])) {
                        echo "<a href='includes/logout.inc.php' class='right'>Cerrar sesión de " . $_SESSION["usuario"] .  "</a>";
                        echo "<a href='perfil.php' class='right'>Perfil</a>";
                        echo "<form class='busqueda' method='post'> <input type='text' name='busqueda' placeholder='Ingresa tu busqueda'> </form> ";
                    }
                    else {
                        echo"<a href='identificarse.php' class='right'>Identifícate</a>";
                        echo"<a href='registrarse.php' class='right'>Regístrate</a>";
                    }
                    ?>
                </ul>
            </div>
        </nav>
<div>
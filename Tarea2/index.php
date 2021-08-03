<?php
include_once'header.php'
?>

<div class="row">
    <div class="side"> <!-- Barra lateral izquierda -->
        <?php
        if (isset($_SESSION["usuario"])) {
            echo "<p><b>Bienvenido</b> ". $_SESSION["usuario"]."!</p>";
            echo "<h2>ACA COLOCAMOS LOS TAGS DEL USUARIO</h2>";
        }
        else {
            echo"<h1>Bienvenido!</h1>";
            echo"<p>Inicia sesión para ver tus tags</p>";
        }
        ?>
        
    </div>
    <div class="main"><!-- Seccion central-->
    <?php
    if (isset($_SESSION["usuario"])) {
        include_once'usmitos.php';
        include_once'publicaciones.php';
    }
    else {
        echo"<h1>¿Tienes cuenta?</h1>";
        echo"<p>Inicia sesión para ver lo que se esta hablando en el mundo, desde tu casa. Si no tienes cuenta ¡Create una!</p>";
    }
    ?>
    </div>
</div>

<?php
include_once'footer.php'
?>
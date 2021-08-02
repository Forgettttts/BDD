<?php
include_once'header.php'
?>

<div class="row">
    <div class="side"> <!-- Barra lateral izquierda -->
        <p>
            <b>Bienvenido</b>
            <?php echo $_SESSION["usuario"];?>
        </p>
        <h2>ACA COLOCAMOS LOS TAGS DEL USUARIO</h2>
    </div>
    <div class="main"><!-- Seccion central-->
    <?php
    if (isset($_SESSION["usuario"])) {
        include_once'usmitos.php';
    }
    else {
        echo"<h1>Bienvenido!</h1>";
        echo"<p>Inicia sesión para ver lo que se esta hablando en el mundo, desde tu casa :D</p>";
    }
    ?>
    </div>
</div>

<?php
include_once'footer.php'
?>
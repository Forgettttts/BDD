<?php
include_once'header.php';
require_once 'includes/funciones.inc.php';
?>

<div class="wrapper">
    <p> Perfil de <?php echo $_SESSION["usuario"]; ?></p>
    <br>
    <p> Perfil de <?php echo $_SESSION["nombre"]; ?></p>
</div>

<?php
include_once'footer.php'
?>
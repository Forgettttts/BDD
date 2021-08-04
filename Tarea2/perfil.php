<?php
include_once'header.php';
require_once 'includes/funciones.inc.php';
?>

<div class="wrapper">
    <h1>Perfil personal</h1>
    <p>Usuario: <?php echo $_SESSION["usuario"]; ?></p>
    <br>
    <p>Nombre personal: <?php echo $_SESSION["nombre"]; ?></p>
    <br>
    <p>Correo: <?php echo $_SESSION["correo"]; ?></p>
    <br>
    <p>Sigues a: <?php echo $_SESSION["seguidos"]; ?> personas</p>
    <br>
    <p>Te siguen: <?php echo $_SESSION["seguidores"]; ?> personas</p>
</div>
<form action="includes/Daccount.inc.php">
    <button type="BotonElimnar" name="EliminarCuenta">BORRAR CUENTA</div>
</form>


<?php
include_once'footer.php'
?>
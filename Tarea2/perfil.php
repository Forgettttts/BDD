<?php
include_once'header.php';
include_once'includes/dbh.inc.php';
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
    <br>
    <br>

    <a href="perfil.php?deleteaccount=true">Eliminar mi cuenta</a>
    <br><br>
    <form action="includes/Daccount.inc.php" method="post">
        <input type="text" name="newuser" placeholder="Ingresa aca, si quieres cambiar tu nombre de usuario">
        <button type="BotonUpdate" name="UpdateCuenta">Actualizar nombre de usuario</div>
    </form>
    <?php 
    $infouser = $_SESSION["usuario"];
    if(isset($_GET['deleteaccount'])){
        if($_GET['deleteaccount'] == 'true'){
            mysqli_query($conn, "DELETE FROM Usmer WHERE UserName = '$infouser'");
            header('location: includes/logout.inc.php');
            exit();	
        }
    }
    ?>
</div>
<?php
include_once'footer.php'
?>
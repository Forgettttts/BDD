<?php
include_once'header.php'
?>

<div class="wrapper">
    <section class="identificacion">
        <div>
            <h1>Ingresa a tu cuenta!</h1>
            <form action="identificacion.inc.php" method="post">
                <input type="text" name="username" placeholder="Nombre de usuario">
                <input type="password" name="password" placeholder="Contraseña">
                <button type="submit" name="registrar">Ingresar</button>
            </form>
        </div>
    </section>
</div>

<?php
include_once'footer.php'
?>
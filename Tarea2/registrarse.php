<?php
include_once'header.php'
?>

<div class="wrapper">
    <section class="formulario-registro">
        <div>
            <h1>Registrate!</h1>
            <form action="includes/registro.inc.php" method="post">
                <input type="text" name="nombre" placeholder="Nombre completo">
                <input type="text" name="username" placeholder="Nombre de usuario">
                <input type="text" name="correo" placeholder="Correo">
                <input type="password" name="password" placeholder="Elija contraseña">
                <input type="password" name="password2" placeholder="Repita su contraseña">
                <button type="submit" name="submit">Registrarme</button>
            </form>
        </div>
    </section>
</div>

<?php
include_once'footer.php'
?>
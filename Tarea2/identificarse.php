<?php
include_once'header.php'
?>

<div class="wrapper">
    <section class="identificacion">
        <div>
            <h1>Ingresa a tu cuenta!</h1>
            <form id="Formulario" action="includes/identificacion.inc.php" method="post">
                <input type="text" name="username" placeholder="Nombre de usuario">
                <input type="password" name="password" placeholder="Contraseña">
                <button type="submit" name="ingresar">Ingresar</button>
            <?php
            if (isset($_GET["error"])){
                if (($_GET["error"])=="EntradaVacia"){
                    echo "<p>Por favor, rellena todos los campos.</p>";
                }
                else if (($_GET["error"])=="UsuarioErroneo"){
                    echo "<p>Por favor, ingresa un nombre de usuario válido.</p>";
                }
                else if (($_GET["error"])=="ContraseñaErronea"){
                    echo "<p>El usuario y contraseña no coinciden, intenta nuevamente.</p>";
                }
                else if (($_GET["error"])=="UsuarioYaExistente"){
                    echo "<p>Nombre de usuario ya existente, por favor, prueba con otro.</p>";
                }
                else if (($_GET["error"])=="LogInAgain"){
                    echo "<p>Nombre de usuario cambiado con exito, inicie sesion nuevamente, por seguridad.</p>";
                }
            }
            ?>
            </form>
        </div>
    </section>
</div>

<?php
include_once'footer.php'
?>
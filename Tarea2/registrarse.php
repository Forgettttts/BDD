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
            <?php
            if (isset($_GET["error"])){
                if (($_GET["error"])=="EntradaVacia"){
                    echo "<p>Por favor, rellena todos los campos.</p>";
                }
                else if (($_GET["error"])=="UsuarioInvalido"){
                    echo "<p>Por favor, ingresa un nombre de usuario válido.</p>";
                }
                else if (($_GET["error"])=="CorreoInvalido"){
                    echo "<p>Por favor, ingresa un correo válido.</p>";
                }
                else if (($_GET["error"])=="PasswordDistintas"){
                    echo "<p>Las contraseñas no coinciden.</p>";
                }
                else if (($_GET["error"])=="UsuarioYaExistente"){
                    echo "<p>Nombre de usuario ya existente, por favor, prueba con otro.</p>";
                }
                else if (($_GET["error"])=="ConexionFallida"){
                    echo "<p>Algo salió mal, por favor, intenta nuevamente.</p>";
                }
                else if (($_GET["error"])=="none"){
                    echo "<p>Registro exitoso!.</p>";
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
<?php
include_once'header.php'
?>

<div class="wrapper">
    <section class="usmitos">
        <div>
            <h1>¿En que estas pensando?</h1>
            <form action="includes/usmitacion.inc.php" method="post">
                <textarea name="mensaje" placeholder="Expresate, hasta 279 caracteres"></textarea>
                <input type="text" name="visibilidad" placeholder="¿Quién quieres que lo vea?">
                <button type="submit" name="Publicar">Publicar</button>
            <?php
            if (isset($_GET["error"])){
                if (($_GET["error"])=="EntradaVacia"){
                    echo "<p>Por favor, rellena todos los campos.</p>";
                }
                else if (($_GET["error"])=="LargoErroneo"){
                    echo "<p>Solo puedes usar hasta 279 caracteres.</p>";
                }
                else if (($_GET["error"])=="VisibilidadErronea"){
                    echo "<p>Error en visibilidad, elige bien quien puede ver tu mensaje.</p>";
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
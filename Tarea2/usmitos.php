<?php
include_once'header.php'
?>

<div class="wrapper">
    <section class="usmitos">
        <div>
            <h6>¿En que estas pensando?</h6>
            <form id="NewPost" action="includes/usmitacion.inc.php" method="post">
                <textarea class="ta" name="mensaje" placeholder="Expresate, hasta 279 caracteres"></textarea>
                
                <input type="text" name="tags" placeholder="Ingresa tus tags, separandolos con un espacio">
                
				<br><br>
                <label for="visibilidad">¿Quién quieres que lo vea?</label>
                <select name="Visibilidades" id="Visibilidades">
                    <optgroup label="Opciones Visibilidad:">
                    <option value="Público">Público</option>
                    <option value="CloseFriends">Close Friends</option>
                    </optgroup>
                </select>
				<br><br>
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

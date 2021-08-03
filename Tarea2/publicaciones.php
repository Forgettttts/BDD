<?php
include_once'header.php'
?>


<?php 

require_once 'includes/dbh.inc.php';
//? Ordenamos los psot en orden descendente, como cualquier feed
$stmt = "SELECT * 
FROM Usmitos 
ORDER BY Fecha DESC";
//? Creamos la accion dentro de la BDD
$sql = mysqli_query($conn, $stmt);
while ($publicaciones = mysqli_fetch_array($sql, MYSQLI_ASSOC)){ //? Iteramos sobre la tabla de Usmitos
	$usuario = mysqli_real_escape_string($conn, $Usmitos['Creador']);//? Dentro de usmitos, en la fila actual, extraemos el usuario del creador
	$IdPublicacion = mysqli_real_escape_string($conn, $Usmitos['Identificador']);//? Dentro de usmitos, en la fila actual, extraemos el Id de la publicacion
	$datosUsuario = mysqli_query($conn, "SELECT * FROM Usmer WHERE UserName = '$usuario'"); //? Buscamos los datos del creador, en base al nombre de usuario
	$Publicador = mysqli_fetch_array($datosUsuario); //? Guardamos los datos del publicador
	?>
	<p>Intento de texto, <?php echo $Usmitos['Mensaje'];?></p>
	<div class="wrapper">
		<div class="post-box">
			<br>
			<div class="up-post-box">
				<div class="nombre-box">
					<a id="NombrePublicador" href="profile.php?usuario=<?php echo $Publicador['UserName']?>"><?php echo $Publicador['Nombre']; ?></a>
					<a id="UsuarioPublicador" href="profile.php?usuario=<?php echo $Publicador['UserName']?>"><?php echo '@'.$Publicador['UserName'];?></a>
				</div>
				<div class="fecha-box">
					<a class="fecha" href="post.php?id=<?php echo $IdPublicacion?>"><?php echo $Usmitos['Fecha'];?></a>
				</div>
			</div>
			<div class="text-post-box">
				<div>
					<p><?php echo $Usmitos['Mensaje'];?></p>
				</div>
			</div>

			<div class="options-post-box">
				<div class="respuesta-box">
					<i class="far fa-comment-dots"></i>
					<span>Comentar</span>
				</div>
				<div class="reusmeo-box">
					<i class="fas fa-share-alt-square"></i>
					<span>Reusmear</span>
				</div>
				<div class="meencanta-box">
					<i class="fas fa-heart"></i>
					<span>Me encanta</span>
				</div>
			</div>
			<br>
		</div>
	</div>

<?php
}
?>


<?php
include_once'footer.php'
?>
<?php
/*
Funcion: EntradaVacia
Funcionamiento: Revisa si es que alguno de los parametros esta vacio.
Input: Parametros del formulario de registro
Ouput: Un booleano, True si es que alguno de los campos esta vacio, False si es que no
*/
function EntradaVacia($name, $username, $correo, $pwd, $pwd2){
    if ( empty($name) || empty($username) ||empty($correo) ||empty($pwd) ||empty($pwd2) ){
        $result=true;
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: UsuarioInvalido
Funcionamiento: Revisa si es que el usuario que se ingreso no es valido.
Input: Nombre de usuario
Ouput: Un booleano, True si es que usuario no es valido, False si es que lo es.
*/
function UsuarioInvalido($username){
    //? En el siguiente if se usa expresion regular para que solo contenga alfanumericos 
    if (!preg_match("/^[a-zA-Z0-9]*$/", $username)) {
        $result=true; //Si es que NO hay un match con los parametros dados.
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: CorreoInvalido
Funcionamiento: Revisa si es que el correo que se ingreso no es valido.
Input: Correo ingresado.
Ouput: Un booleano, True si es que correo no es valido, False si es que lo es.
*/
function CorreoInvalido($correo){
    if (!filter_var($correo, FILTER_VALIDATE_EMAIL)) {
        $result=true;
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: pwdMatch
Funcionamiento: Revisa si es que las contraseñas son distintas.
Input: Constraseñas ingresadas ingresado.
Ouput: Un booleano, True si es que las contraseñas no son iguales, False si es que lo son.
*/
function pwdMatch($pwd, $pwd2){
    if ($pwd !== $pwd2) {
        $result=true;
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: UsuarioOcupado
Funcionamiento: Revisa si es que el nombre de usuario ingresado, ya esta ocupado.
Input: Nombre de usuario ingresado.
Ouput: Un booleano, True si es que el nombre de usuario esta ocupado, False si es no.
*/
function UsuarioOcupado($conn, $username, $correo){
    $sql="SELECT * FROM Usmer WHERE UserName=? OR Correo =?;";
    $stmt= mysqli_stmt_init($conn); // Iniciamos una accion en la conexion entregada
    if (!mysqli_stmt_prepare($stmt, $sql)) { //revisamos que la conecion no falle
        header("location: ../registrarse.php?error=ConexionFallida");
        exit();
    }
    mysqli_stmt_bind_param($stmt, "ss", $username, $correo);// "pegamos los datos de la tabla en stmt"
    mysqli_stmt_execute($stmt);//ejecutamos lo anterior

    $resultData= mysqli_stmt_get_result($stmt); //Obtenemos los datos extraidos de la tabla

    if ($row=mysqli_fetch_assoc($resultData)) { //Asociamos los datos extraidos a las variables de la bdd
        return $row; //Lo que retorna es la info del usuario que ya estaba en la BDD
    }
    else {
        $result=false;
        return $result;
    }
    mysqli_stmt_close($stmt);
}

/*
Funcion: CrearUsuario
Funcionamiento: Crea un usuario nuevo.
Input: Datos de nuevo usuario.
Ouput:None
*/
function CrearUsuario($conn, $name, $username, $correo, $pwd){
    $sql="INSERT INTO Usmer (Nombre, UserName, Correo, Contraseña) VALUES (?,?,?,?);";
    $stmt= mysqli_stmt_init($conn); // Iniciamos una accion en la conexion entregada
    if (!mysqli_stmt_prepare($stmt, $sql)) { //revisamos que la conecion no falle
        header("location: ../registrarse.php?error=ConexionFallida");
        exit();
    }
    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);//Hasheamos la contraseña, para dificultar obtener contraseñas

    mysqli_stmt_bind_param($stmt, "ssss", $name, $username, $correo, $hashedPwd);// Ingresamos los datos
    mysqli_stmt_execute($stmt);//ejecutamos lo anterior
    mysqli_stmt_close($stmt);
    header("location: ../registrarse.php?error=none");
    exit();
}
/*
Funcion: EntradaVaciaLogin
Funcionamiento: Revisa si es que alguno de los parametros esta vacio.
Input: Parametros del formulario de login
Ouput: Un booleano, True si es que alguno de los campos esta vacio, False si es que no
*/
function EntradaVaciaLogin($username, $pwd){
    if (empty($username)||empty($pwd)){
        $result=true;
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: LoginUser
Funcionamiento: Ingresa al usuario a su cuenta.
Input: Parametros del formulario de login
Ouput: none (solo hace login).
*/
function LoginUser($conn, $username, $pwd)
{
    $UsuarioExiste=UsuarioOcupado($conn, $username, $username); //? Si es que retorna false, es pq el usuario no se encontro
    if ($UsuarioExiste==false) {
        header("location: ../identificarse.php?error=UsuarioErroneo");
        exit();
    }
    $pwdHashed = $UsuarioExiste["Contraseña"];
    $chechPwd= password_verify($pwd, $pwdHashed);

    if ($chechPwd===false) {
        header("location: ../identificarse.php?error=ContraseñaErronea");
        exit();
    }
    elseif ($chechPwd === true) { //* Igualdad absoluta
        session_start();
        $_SESSION["nombre"]=$UsuarioExiste["Nombre"];
        $_SESSION["usuario"]=$UsuarioExiste["UserName"];
        header("location: ../index.php");
        exit();
    }
}
/*
Funcion: LargoExcedido
Funcionamiento:Comprueba si es que el msje a publicar no supera los 279 caracteres.
Input: Mensaje del usmito a crear.
Ouput: Booleano, true si es que es demasiado largo, false si es que no.
*/
function LargoExcedido($mensaje){
    if (strlen($mensaje)>279) {
        return true;
    }
    else {
        return false;
    }
}

/*
Funcion: MensajeVacio
Funcionamiento: Revisa si es que el mensaje esta vacio.
Input: Mensaje a subir.
Ouput: Un booleano, True si es que el msje esta vacio, False si es que no
*/
function MensajeVacio($mensaje){
    if (empty($mensaje)){
        $result=true;
    }
    else{
        $result=false;
    }
    return $result;
}

/*
Funcion: SubirUsmito
Funcionamiento: Carga a la BDD el usmito.
Input: Mensaje y visibilidad del usmito a crear.
Ouput: none.
*/
function SubirUsmito($conn, $mensaje, $visibilidad, $usuario){
    $sql="INSERT INTO Usmitos (Creador, Mensaje, Visibilidad) VALUES (?,?,?);";
    $stmt= mysqli_stmt_init($conn); // Iniciamos una accion en la conexion entregada
    if (!mysqli_stmt_prepare($stmt, $sql)) { //revisamos que la conecion no falle
        header("location: ../registrarse.php?error=ConexionFallida");
        exit();
    }
    mysqli_stmt_bind_param($stmt, "sss", $usuario, $mensaje, $visibilidad);// Ingresamos los datos
    mysqli_stmt_execute($stmt);//ejecutamos lo anterior
    mysqli_stmt_close($stmt);
    header("location: ../index.php?error=none");
    exit();
}
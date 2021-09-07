function crearColeccion(usuario){
    window.location.href = `${usuario}/crearColeccion`;
}

function salirCuenta(){
    window.location.href = "/logout";
}

function buscarJuego(nombreUser, nombre){
    window.location.href = `/${nombreUser}/${nombre}/search`;
}

function eliminar_coleccion(nombreUser, nombre) {
    if (window.confirm("¿Desea borrar esta colección?") == true)
    window.location.href = `/${nombreUser}/${nombre}/eliminar_coleccion`;
}

function login(){
    window.location.href = '/login';
}

function register(){
    window.location.href = '/register';
}
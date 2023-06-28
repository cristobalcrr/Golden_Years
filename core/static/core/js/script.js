function validarRegistro() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var contraseña = document.getElementById("contraseña").value;
    var edad = document.getElementById("edad").value;
    var numero = document.getElementById("numero").value;
    var foto = document.getElementById("foto").value;
    var descripcion = document.getElementById("descripcion").value;
    
    if (nombre === "" || apellido === "" || contraseña === "" || edad === "" || numero === "" || foto === "" || descripcion === "") {
        alert("Por favor, completa todos los campos.");
        return false;
    }
    
    if (edad < 50) {
        alert("Debes tener al menos 18 años para registrarte.");
        return false;
    }
    

    
    return true;
}





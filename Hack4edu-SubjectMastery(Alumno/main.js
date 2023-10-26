var nivel_actual = 1;
var operando1 = 0;
var operando2 = 0;
var button_siguiente = document.querySelector('#siguiente_pregunta'); // Use '#siguiente_pregunta' to select by ID
var button_resolver = document.querySelector('#resolver');



button_siguiente.addEventListener('click', function(event) { 
    event.preventDefault(); 

    fetch('operandos_actuales.json')
        .then(response => response.json())
        .then(data => {
            operando1 = data.operando1;
            operando2 = data.operando2;
            var p = document.querySelector("#operacion");
            p.innerHTML = operando1 + "+" + operando2;
        });
});

button_resolver.addEventListener('click', function(event) { 
    event.preventDefault(); 
    var resul_usuario = document.querySelector('#resultado').value;
    var resul = operando1 + operando2;
    if(resul_usuario == resul){
        var p = document.querySelector("#correccion");
            p.innerHTML = "CORRECTO";
            nivel_actual = nivel_actual + 1;
            
    }else{
        var p = document.querySelector("#correccion");
            p.innerHTML = "INCORRECTO";
    }
    
    const data = {nivel: nivel_actual};
    const jsonStr = JSON.stringify(data);

    const a = document.createElement("a");
    a.href = "data:application/json;charset=utf-8," + encodeURIComponent(jsonStr);
    a.download = "datos.json";
    a.innerHTML = "Descargar datos.json";

    //a.click();

});

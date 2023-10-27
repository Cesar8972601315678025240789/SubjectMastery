var nivel_actual = 0;
var operando1 = 0;
var operando2 = 0;
var button_siguiente = document.querySelector('#siguiente_pregunta'); // Use '#siguiente_pregunta' to select by ID
var button_resolver = document.querySelector('#resolver');

fetch('operandos_actuales.json')
        .then(response => response.json())
        .then(data => {
            operando1 = data.operando1[0];
            operando2 = data.operando2[0];
            nivel_actual = data.nivel_actual;
            var p = document.querySelector("#operacion");
            p.innerHTML = operando1 + "+" + operando2;
        });




button_resolver.addEventListener('click', function(event) { 
    event.preventDefault(); 
    var resul_usuario = document.querySelector('#resultado').value;
    var resul = operando1 + operando2;
    if(resul_usuario == resul){
        var p = document.querySelector("#correccion");
            p.innerHTML = "CORRECTO";
            if(nivel_actual < 5){
                nivel_actual = nivel_actual + 1;
            }
            
            
    }else{
        var p = document.querySelector("#correccion");
        if(nivel_actual > 1){
            nivel_actual = nivel_actual - 1;
        }
            p.innerHTML = "INCORRECTO";
    }
    
    const data = {nivel: nivel_actual};
    const jsonStr = JSON.stringify(data);

    const a = document.createElement("a");
    a.href = "data:application/json;charset=utf-8," + encodeURIComponent(jsonStr);
    a.download = "datos.json";
    a.innerHTML = "Descargar datos.json";
    a.click();

});

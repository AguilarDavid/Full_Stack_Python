// obtener elementos con id tabla y id contenido
let tabla = document.getElementById("tabla");
let contenido = document.getElementById("contenido");
let carta = document.getElementById("carta");

// consumo de api con fetch
fetch('https://digimon-api.vercel.app/api/digimon')
.then(response => response.json())
.then(data =>{
    // console.log(data);
    mostrarTabla(data); // invocando la función mostrarTabla()
}).catch(error => console.log(error))

// función para obtener los datos del Digimon y mostrarlo en la tabla con id tabla y id contenido
function mostrarTabla(response) {
    // limpiar el elemento con id contenido
    contenido.innerHTML = "";
    // recorrer los datos obtenidos de la api

    // forEach(temp => {//temp es un objeto temporal que contiene los datos del digimon

    // response.forEach(temp => {
    //      contenido.innerHTML +=
    //      `<td>${temp.name}</td>
    //      <td><img src="${temp.img}" alt="" width="50px" height="50px"></td>
    //      `
    //      });

    for(let temp of response){
        // para incrustar valores en el contenido dinamicamente se necesita
        // `` comillas francesas y la anotación o estructura ${temp.key}
        contenido.innerHTML +=
        `<td>${temp.name}</td>
        <td><img src="${temp.img}" alt="" width="50px" height="50px"></td>
        <td>${temp.level}</td>
        `
    }
}
function mostrarCarta() {
    //obtener el valor del input con el id busqueda
    let busqueda = document.getElementById("busqueda").value.toLowerCase();
    console.log(busqueda);
    let tabla = document.getElementById("tablaDigimon");
    let contenido = document.getElementById("tablaContenido");
        if (tabla !=null && contenido !=null) {
            tabla.style.display= "none"
            contenido.styledisplay="none"
        }
    // consumo de api con fetch  
    fetch(`https://digimon-api.vercel.app/api/digimon/name/${busqueda}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            construirCarta(data); // invocando la función carta(data)
        }).catch(error => console.log(error))
}

//funcion para crear la carta del digimon dinamicamente
function construirCarta(params) {
    //ocultal la tabla con id tabla y tbody con id contenido de la tabla
    //document.getElementById("tabla").style.display = "none";
    //document.getElementById("contenido").style.display = "none";
    tabla.innerHTML = "";
    contenido.innerHTML = "";
    carta.innerHTML = "";
    //ciclo para recorrer los datos obtenidos de la api
    for(let temp of params){ // temp es el objeto temporal que que contiene los datos de l digimon
        carta.innerHTML += 
        `
        <div class="card col-sm-12 col-md-6 mx-auto" style="width: 18rem;">
            <img src="${temp.img}" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">${temp.name}</h5>
            <p class="card-text">Nivel: ${temp.level}</p>
            </div>
        </div>
        `
    }
}
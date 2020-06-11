function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

editarAlbum = () => {
    let contenedorInputsAlbum = document.getElementById("inputsAlbum");
    let inputs = contenedorInputsAlbum.getElementsByClassName("form-control");
    let btnPrincipal = document.getElementById("btn-principal");

    for(let x=0; x<inputs.length; x++){
        inputs[x].removeAttribute("disabled");
    }

    btnPrincipal.innerText = "Guardar cambios";
    btnPrincipal.classList.remove("btn-primary");
    btnPrincipal.classList.add("btn-success");
    btnPrincipal.setAttribute("onClick", "actualizarAlbum()");

}

actualizarAlbum = () => {
    // var, const, let
    let idAlbum = document.getElementById("idAlbum").dataset.idalbum;
    let fechaAlbum = document.getElementById("fechaAlbum").value;
    let generoAlbum = document.getElementById("generoAlbum").value;
    let nombreAlbum = document.getElementById("nombreAlbum").value;
    let datos = {
        idAlbum: idAlbum,
        fechaAlbum: fechaAlbum,
        generoAlbum: generoAlbum,
        nombreAlbum: nombreAlbum
    }

    // FETCH
    // FUNCION QUE PERMITE CONECTAR UN SERVIDOR (API) CON TU FRONT
    fetch("http://127.0.0.1:8000/artista/albums/update", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept":'application/json',
            'X-Requested-With':"XMLHttpRequest"
        },
        body: JSON.stringify(datos),
        mode: 'cors',
        cache: 'default',
        credentials: 'include'
    })
    .then(

        respuesta => {
            respuesta.text().then(
                function(data){
                    // console.log(data);

                    if(Boolean(data)){
                        alert("Cambios hechos correctamente");
                        let btnPrincipal = document.getElementById("btn-principal");
                        btnPrincipal.innerText = "Guardar cambios";
                        btnPrincipal.classList.remove("btn-success");
                        btnPrincipal.classList.add("btn-primary");
                        btnPrincipal.setAttribute("onClick", "editarAlbum()");

                        let contenedorInputsAlbum = document.getElementById("inputsAlbum");
                        let inputs = contenedorInputsAlbum.getElementsByClassName("form-control");
                        for(let x=0; x<inputs.length; x++){
                            inputs[x].setAttribute("disabled", "");
                        }


                    }else{
                        alert("Ha ocurrido un error. Intentalo mas tarde");
                    }

                }
            );
        }

    )
    .catch(
        function(error){
            alert("Error");
            console.log(error)
        }
    );

}

eliminarAlbum = () => {
    let idAlbum = document.getElementById("idAlbum").dataset.idalbum;

    fetch("http://127.0.0.1:8000/artista/albums/delete", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept":'application/json',
            'X-Requested-With':"XMLHttpRequest"
        },
        body: JSON.stringify(idAlbum),
        mode: 'cors',
        cache: 'default',
        credentials: 'include'
    })
    .then(

        respuesta => {
            respuesta.text().then(
                function(data){
                    // console.log(data);

                    if(Boolean(data)){
                        alert("Album eliminado correctamente");
                        window.location = "http://127.0.0.1:8000/artista/albums/";

                    }else{
                        alert("Ha ocurrido un error. Intentalo mas tarde");
                    }

                }
            );
        }

    )
    .catch(
        function(error){
            alert("Error");
            console.log(error)
        }
    );


}

agregarCancion = () => {
    let nombreCancion = document.getElementById("nombreCancion");
    let duracionCancion = document.getElementById("duracionCancion");
    let autorCancion = document.getElementById("autorCancion");
    let idAlbum = document.getElementById("albumCancion").dataset.idalbum;
    let archivoCancion = document.getElementById("archivoCancion").files[0];

    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie("csrftoken"));
    formData.append("nombreCancion", nombreCancion.value);
    formData.append("duracionCancion", duracionCancion.value);
    formData.append("autorCancion", autorCancion.value);
    formData.append("idAlbum", idAlbum);
    formData.append("archivoCancion", archivoCancion);

    // AJAX CON JQUERY
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/cancion/add",
        data: formData,
        // UNICOS PARA ESTE CASO DE ENVIO DE UN ARCHIVO
        processData: false, // No procese la informacion, simplemente que la envie
        contentType: false, // No envie el ContentType
        success: function(data){
            console.log(data);
            if(Boolean(data)){
                $("#modal").modal("hide");
                $("#modalExito").modal("show");

                let tabla = document.getElementById("table");
                let filas = tabla.getElementsByTagName("tr");
                let numeroFilas = filas.length;

                let tr = document.createElement("tr");

                let th = document.createElement("th");
                th.setAttribute("scope", "row");
                th.appendChild(document.createTextNode(numeroFilas));
                tr.appendChild(th);

                let td1 = document.createElement("td");
                td1.appendChild(document.createTextNode(nombreCancion.value));
                tr.appendChild(td1);

                let td2 = document.createElement("td");
                td2.appendChild(document.createTextNode(autorCancion.value));
                tr.appendChild(td2);

                let td3 = document.createElement("td");
                td3.appendChild(document.createTextNode(duracionCancion.value));
                tr.appendChild(td3);

                let td4 = document.createElement("td");
                let btn1 = document.createElement("button");
                btn1.setAttribute("class", "btn btn-sm btn-success");
                btn1.appendChild(document.createTextNode("Editar"));
                td4.appendChild(btn1);
                tr.appendChild(td4);

                let td5 = document.createElement("td");
                let btn2 = document.createElement("button");
                btn2.setAttribute("class", "btn btn-sm btn-danger");
                btn2.appendChild(document.createTextNode("Eliminar"));
                td5.appendChild(btn2);
                tr.appendChild(td5);

                tabla.getElementsByTagName("tbody")[0].appendChild(tr);
                nombreCancion.value="";
                duracionCancion.value="";
                autorCancion.value=null;
                document.getElementById("archivoCancion").value=null;
            }else{
                $("#modal").modal("hide");
                $("#modalError").modal("show");
            }
        },
    error: function(data){
        $("#modal").modal("hide");
        $("#modalError").modal("show");

    }
    });

}

eliminarCancion = (elemento) =>{
    let idCancionSucio = elemento.getAttribute("data-id");
    let idCancionSucio2 = idCancionSucio.split("-");
    let idCancion = idCancionSucio2[1];

    let token = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/cancion/delete",
        data: {
            csrfmiddlewaretoken: token,
            idCancion: idCancion
        },
        success: function(data){
            alert(data);
            $("#modalConfirmarCancion").modal('hide');

            document.getElementById(idCancionSucio).innerHTML="";



        },
        error: function(data){
            console.log(data);
            alert("Ha ocurrido un error al eliminar la cancion");
        }
    });

}

editarCancion = (elemento) =>{
    let idElementoTr = elemento.getAttribute("data-id");
    let elementoTr = document.getElementById(idElementoTr);

    let btnEditar = document.getElementById("btn-editar-"+idElementoTr);
    btnEditar.textContent="Guardar cambios";
    btnEditar.removeAttribute("onclick");
    btnEditar.onclick = function(){actualizarCancion(idElementoTr)};

    let btnEliminar = document.getElementById("btn-eliminar-"+idElementoTr);
    btnEliminar.textContent="Cancelar";
    btnEliminar.removeAttribute("data-toggle");
    btnEliminar.removeAttribute("data-target");
    btnEliminar.onclick = function(){cancelarActualizarCancion(idElementoTr)};

    for(let x=1; x<4; x++){
        elementoTr.children[x].classList.add("form-control");
        elementoTr.children[x].classList.add("form-control-sm");
        elementoTr.children[x].setAttribute("contenteditable", "true")
    }

}

actualizarCancion = (id) =>{
    let idCancionSucio = id.split("-");
    let idCancion = idCancionSucio[1];
    let elementoTr = document.getElementById(id);   

    let token = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/cancion/update",
        data: {
            csrfmiddlewaretoken: token,
            idCancion: idCancion,
            nombreCancion: elementoTr.children[1].textContent,
            autorCancion: elementoTr.children[2].textContent,
            duracionCancion: elementoTr.children[3].textContent
        },
        success: function(data){
            alert(data);
        },
        error: function(data){
            console.log(data);
            alert("Ha ocurrido un error al actualizar la cancion");
        }
    });


}

cancelarActualizarCancion = (idElementoTr) =>{
    let elementoTr = document.getElementById(idElementoTr);

    let btnEditar = document.getElementById("btn-editar-"+idElementoTr);
    btnEditar.textContent="Editar";
    btnEditar.onclick = function(){editarCancion(btnEditar)};

    let btnEliminar = document.getElementById("btn-eliminar-"+idElementoTr);
    btnEliminar.textContent="Eliminar";
    btnEliminar.removeAttribute("onclick");

    for(let x=1; x<4; x++){
        elementoTr.children[x].classList.remove("form-control");
        elementoTr.children[x].classList.remove("form-control-sm");
        elementoTr.children[x].removeAttribute("contenteditable", "true")
    }

    setTimeout(function(){
        btnEliminar.setAttribute("data-toggle", "modal");
        btnEliminar.setAttribute("data-target", "modalConfirmarCancion");
    }, 1000)

}

agregarAlbum = () =>{
    let nombreAlbum =  document.getElementById("nombre");
    let fechaAlbum =  document.getElementById("fecha");
    let disqueraAlbum = document.getElementById("disquera"); 
    let generoAlbum =  document.getElementById("genero");
    let fotoAlbum= document.getElementById("foto");


    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", getCookie('csrftoken'));
    formData.append("nombreAlbum", nombreAlbum.value);
    formData.append("fechaAlbum", fechaAlbum.value);
    formData.append("disqueraAlbum", disqueraAlbum.value);
    formData.append("generoAlbum", generoAlbum.value);
    formData.append("fotoAlbum", fotoAlbum.files[0]);

    let numeroCanciones = 0;
    $.each($("#canciones"), function(i, obj){
        $.each(obj.files, function(j, file){
            numeroCanciones=j;
            formData.append('cancion['+j+']', file);
        })
    })
    formData.append("numeroCanciones", numeroCanciones.toString());

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/artista/albums/add",
        data: formData,
        // UNICOS PARA ESTE CASO DE ENVIO DE UN ARCHIVO
        processData: false, // No procese la informacion, simplemente que la envie
        contentType: false, // No envie el ContentType
        success: function(data){
            if(Boolean(data)){
                console.log(data);
                $("#modalExito").modal('show');
                nombreAlbum.value="";
                fechaAlbum.value="";
                disqueraAlbum.value="";
                generoAlbum.value="";
                fotoAlbum.value="";
                document.getElementById("canciones").value="";
            }
            
        },
        error: function(data){
            console.log(data);
            alert("Ha ocurrido un error.")

    }
    });

}



buscarCancion = () =>{
    let texto = document.getElementById("search").value;
    let token = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/reproduccion/busqueda',
        data: {
            csrfmiddlewaretoken: token,
            texto: texto
        },
        success: function(data){
            console.log(data);
            tablaCanciones(data);
        },
        error: function(data){
            alert("Ha ocurrido un error");
            console.log(data);
        }
    });
    
}

tablaCanciones = (data) =>{
    let datos = data['lista'];
    divPadre = document.getElementById("albums");
    divPadre.innerHTML="";

    let tabla = document.createElement("table");
    tabla.setAttribute("class", "table table-dark")
    let thead = document.createElement("thead");
    let tbody = document.createElement("tbody");
    tabla.appendChild(thead);
    tabla.appendChild(tbody);

    let tr1 = document.createElement("tr");
    thead.appendChild(tr1);
    let th1 = document.createElement("th");
    th1.setAttribute("scope", "col");
    th1.appendChild(document.createTextNode("#"));
    let th2 = document.createElement("th");
    th2.setAttribute("scope", "col");
    th2.appendChild(document.createTextNode("Reproducir"));
    let th3 = document.createElement("th");
    th3.setAttribute("scope", "col");
    th3.appendChild(document.createTextNode("Titulo"));
    let th7 = document.createElement("th");
    th7.setAttribute("scope", "col");
    th7.appendChild(document.createTextNode("Album"));
    let th4 = document.createElement("th");
    th4.setAttribute("scope", "col");
    th4.appendChild(document.createTextNode("Autor"));
    let th5 = document.createElement("th");
    th5.setAttribute("scope", "col");
    th5.appendChild(document.createTextNode("Duracion"));

    tr1.appendChild(th1);
    tr1.appendChild(th2);
    tr1.appendChild(th3);
    tr1.appendChild(th7);
    tr1.appendChild(th4);
    tr1.appendChild(th5);

    thead.appendChild(tr1)


    for(let x=0; x<datos.length; x++){
        // console.log(datos[x]);
        let tr = document.createElement("tr");

        let th6 = document.createElement("th")
        th6.setAttribute("scope", "row");
        th6.appendChild(document.createTextNode(x+1));

        let td1 = document.createElement("td")
        let inputMusica = document.createElement("audio");
        inputMusica.setAttribute("preload", "auto");
        inputMusica.setAttribute("controls", "true");
        inputMusica.setAttribute("type", "audio/mp3");
        let sourceMusica = document.createElement("source");
        sourceMusica.setAttribute("src", "/media/" + datos[x][4]);
        inputMusica.appendChild(sourceMusica);
        td1.appendChild(inputMusica);

        let td2 = document.createElement("td");
        td2.appendChild(document.createTextNode(datos[x][0]));
        
        let td5 = document.createElement("td");
        td5.appendChild(document.createTextNode(datos[x][3]));

        let td3 = document.createElement("td");
        td3.appendChild(document.createTextNode(datos[x][2]));

        let td4 = document.createElement("td");
        td4.appendChild(document.createTextNode(datos[x][1]));

        tr.appendChild(th6)
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td5);
        tr.appendChild(td3);
        tr.appendChild(td4);

        tbody.appendChild(tr);
    }

    divPadre.appendChild(tabla);
}
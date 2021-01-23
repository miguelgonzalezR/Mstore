function index() {
    this.ini = function () {
        console.log("Iniciando...");
        this.getInidicadores();
        this.getDatosGraficas();
    }
    this.getInidicadores = function () {

        //Ingresos
        $.ajax({
            statusCode: {
                404: function () {
                    console.log("Esta página no existe");
                }
            },
            url: 'php/servidor.php',
            method: 'POST',
            data: {
                rq: "3"
            }
        }).done(function (datos) {
            //La lógica 3,000
            $("#idIngreso").text(parseFloat(datos).toLocaleString());
        });
    }
    this.getDatosGraficas = function () {
        $.ajax({
            statusCode: {
                404: function () {
                    console.log("Esta página no existe");
                }
            },
            url: 'php/servidor.php',
            method: 'POST',
            data: {
                rq: "4"
            }
        }).done(function (datos) {
            //La lógica
            if (datos != '') {
                let etiquetas = new Array();
                let tVendidos = new Array();
                let tPrecio = new Array();
                let coloresV = new Array();
                let coloresP = new Array();
                var jDatos = JSON.parse(datos);

                var tablaDatos = document.createElement('tabla');
                tablaDatos.classList.add('table', 'table-striped');
                var tr = document.createElement('tr');
                var th = document.createElement('th');
                th.innerText = "Fecha";
                tr.appendChild(th);
                
                th = document.createElement('th');
                th.innerText = "Precio";
                tr.appendChild(th);
                tablaDatos.appendChild(tr);

                for (let i in jDatos) {
                    etiquetas.push(jDatos[i].Nombre);
                    
                    tPrecio.push(jDatos[i].totalPrecio);
                    coloresV.push("#36004D");
                    coloresP.push("679B6B");

                    tr = document.createElement('tr');
                    var td = document.createElement("td");
                    td.innerText = jDatos[i].Nombre;
                    tr.appendChild(td);

                    td = document.createElement("td");
                    td.innerText = parseFloat(jDatos[i].totalVendidos).toLocaleString();
                    tr.appendChild(td);

                    td = document.createElement("td");
                    td.innerText = parseFloat(jDatos[i].totalPrecio).toLocaleString();
                    tr.appendChild(td);
                    
                    tablaDatos.appendChild(tr);
                }

                var idCont = document.getElementById("idContTabla");
        

                var ctx = document.getElementById('idGrafica').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: etiquetas,
                        datasets: [
                            
                            {
                                label: 'Precios',
                                data: tPrecio,
                                backgroundColor: coloresP
                            }
                        ]
                    }
                });
            }
        });
    }
}

var oIndex = new index();
setTimeout(function () { oIndex.ini(); }, 100);
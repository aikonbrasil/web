---
title: 'Sports and other activities - statistics'
date: 2025-10-01
permalink: /health/2025/09/3gpp/
author_profile: false
read_more: enabled
tags:
  - 5G
  - 4G
  - LTE
  - Wireless
  - Real Networks
---

***Abstract:*** Dayly activity is reported in this page, it is for personal usage only.

<html>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
<body>
<canvas id="myChart" style="width:100%;max-width:600px"></canvas>

<script>
const xValues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20,21,22,23,24,25,26,27,28];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{ 
      data: [0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      borderColor: "red",
	  label: "cross-country",
      fill: false
    }, { 
      data: [0,0.5,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      borderColor: "green",
	  label: "swimming",
      fill: false
    }, { 
      data: [0,0.1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      borderColor: "blue",
	  label: "Gym",
      fill: false
    }, { 
      data: [0,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11,5.11],
      borderColor: "black",
	  label: "Acculative of all activities ",
      fill: false
	  }]
  },
  options: {
    legend: {display: true}
  }
});
</script>

</body>
</html>


<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gráfico de Barras con Chart.js</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <canvas id="myChart" width="400" height="200"></canvas>
	
	
<script>
$(document).ready(function() {

    // Cargar el archivo de texto
    $.get('datos.txt', function(data) {
	
        // Procesar los datos del archivo de texto
        let lineas = data.split('\n');
        let etiquetas = [];
        let valores = [];

        lineas.forEach(function(linea) {
            let partes = linea.split(',');
            if (partes.length === 2) {
                etiquetas.push(partes[0]);
                valores.push(parseInt(partes[1]));
            }
        });
		

        // Crear el gráfico de barras
        let ctx = document.getElementById('myChart').getContext('2d');
        let myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: etiquetas,
                datasets: [{
                    label: 'Datos de ejemplo',
                    data: valores,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
		
		
    });
	
 	
});	
	
</script>
</body>
</html>


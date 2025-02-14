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

<html lang="es">
<head>
	<meta charset="UTF-8">
	<title> Gráfico de Barras con Chart.js </title>
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





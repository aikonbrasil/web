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
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
<body>
<canvas id="myChart" style="width:100%;max-width:700px"></canvas>

<script>
document.addEventListener('DOMContentLoaded', () => {
  fetch('data.txt')
    .then(response => response.text())
    .then(text => {
      const lines = text.split('\n');
      const xValues = lines[0].split(',').map(Number);
      const yValues = lines[1].split(',').map(Number);

      new Chart("myChart", {
        type: "line",
        data: {
          labels: xValues,
          datasets: [{
            fill: false,
            lineTension: 0,
            backgroundColor: "rgba(0,0,255,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data: yValues
          }]
        },
        options: {
          legend: {
            display: false
          },
          scales: {
            yAxes: [{
              ticks: {
                min: 6,
                max: 16
              }
            }],
          }
        }
      });
    })
    .catch(error => {
      console.error('Error fetching data', error);
    });
});
</script>

</body>
</html>


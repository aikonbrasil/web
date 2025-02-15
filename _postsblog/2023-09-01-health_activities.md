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


const xValues = 
[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28];
const yCrossCountry = 
[  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0];
const ySwimming = 
[  1,0.5,  0,  0,  0,  0,  0,  0,  0,0.5,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const yGym =
[  0,0.1,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const sSum =
[  1,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,6.1,6.1,6.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,9.1,9.1];



new Chart("myChart", {
  type: "line",
  data: {
	labels: xValues,
	datasets: [{ 
	  data: yCrossCountry,
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: ySwimming,
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: yGym,
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  sSum ,
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

<script>
function myFunction(p1, p2) {
  return p1 * p2;
}

let result = myFunction(4, 3);
document.getElementById("demo").innerHTML = result;
</script>

</body>
</html>
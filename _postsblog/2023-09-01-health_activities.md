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
<head>
	<style>
		h1 {
			text-align: center;
		}
		
		h2 {
			text-align: left;
		}
	</style>
</head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
<body>
<h1>  February 2025 </h1>
<h2>  Activity per day </h2>
<canvas id="myChartPerDay_feb2025" style="width:100%;max-width:600px"></canvas>

<h2>  Activity Accumulated during the entire month </h2>
<canvas id="myChartPerCDF_feb2025" style="width:100%;max-width:600px"></canvas>

<script>


const xValues = 
[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28];
const yCrossCountry = 
[  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,1.5,  0,  0,  0,  0];
const ySwimming = 
[  1,0.5,  0,  0,  0,  0,  0,  0,  0,0.5,  0,  0,  1,0.3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const yGym =
[  0,0.1,  0,  0,  0,  0,  0,  0,  0,  2,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,1.5,  0,  0,  0,  0];


function Arrays_sum(array1, array2) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  if (array2.length === 0)
    return "array2 is empty";

  while (ctr < array1.length && ctr < array2.length) {
    result.push(array1[ctr] + array2[ctr]);
    ctr++;
  }

  if (ctr === array1.length) {
    for (x = ctr; x < array2.length; x++) {
      result.push(array2[x]);
    }
  } else {
    for (x = ctr; x < array1.length; x++) {
      result.push(array1[x]);
    }
  }

  return result;
};


function Arrays_cdf(array1) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  while (ctr < array1.length ) {
	if (ctr === 0){
		x = array1[ctr];
		result.push(x);
	}else{
		x = x + array1[ctr];
		result.push(x);
	}
    ctr++;
  }

  return result;
};



new Chart("myChartPerDay_feb2025", {
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
	  data:  Arrays_sum( Arrays_sum(yCrossCountry,ySwimming), yGym ),
	  borderColor: "black",
	  label: " All activities per day ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Physical Activity per Day (# of Hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



new Chart("myChartPerCDF_feb2025", {
  type: "line",
  data: {
	labels: xValues,
	datasets: [{ 
	  data: Arrays_cdf(yCrossCountry),
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: Arrays_cdf(ySwimming),
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: Arrays_cdf( yGym),
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  Arrays_cdf(  Arrays_sum( Arrays_sum(yCrossCountry,ySwimming), yGym )  ),
	  borderColor: "black",
	  label: "Acculative of all activities ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'CDF (# of hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



</script>



<h1>  March 2025 </h1>
<h2>  Activity per day </h2>
<canvas id="myChartPerDay_march2025" style="width:100%;max-width:600px"></canvas>

<h2>  Activity Accumulated during the entire month </h2>
<canvas id="myChartPerCDF_march2025" style="width:100%;max-width:600px"></canvas>

<script>


const xValues_march = 
[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];
const yCrossCountry_march = 
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const ySwimming_march = 
[  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const yGym_march =
[  0,  0,1.5,1.5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];


function Arrays_sum(array1, array2) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  if (array2.length === 0)
    return "array2 is empty";

  while (ctr < array1.length && ctr < array2.length) {
    result.push(array1[ctr] + array2[ctr]);
    ctr++;
  }

  if (ctr === array1.length) {
    for (x = ctr; x < array2.length; x++) {
      result.push(array2[x]);
    }
  } else {
    for (x = ctr; x < array1.length; x++) {
      result.push(array1[x]);
    }
  }

  return result;
};


function Arrays_cdf(array1) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  while (ctr < array1.length ) {
	if (ctr === 0){
		x = array1[ctr];
		result.push(x);
	}else{
		x = x + array1[ctr];
		result.push(x);
	}
    ctr++;
  }

  return result;
};



new Chart("myChartPerDay_march2025", {
  type: "line",
  data: {
	labels: xValues_march,
	datasets: [{ 
	  data: yCrossCountry_march,
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: ySwimming_march,
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: yGym_march,
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  Arrays_sum( Arrays_sum(yCrossCountry_march,ySwimming_march), yGym_march ),
	  borderColor: "black",
	  label: " All activities per day ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Physical Activity per Day (# of Hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



new Chart("myChartPerCDF_march2025", {
  type: "line",
  data: {
	labels: xValues,
	datasets: [{ 
	  data: Arrays_cdf(yCrossCountry_march),
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: Arrays_cdf(ySwimming_march),
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: Arrays_cdf( yGym_march),
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  Arrays_cdf(  Arrays_sum( Arrays_sum(yCrossCountry_march,ySwimming_march), yGym_march )  ),
	  borderColor: "black",
	  label: "Acculative of all activities ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'CDF (# of hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



</script>



<h1>  April 2025 </h1>
<h2>  Activity per day </h2>
<canvas id="myChartPerDay_april2025" style="width:100%;max-width:600px"></canvas>

<h2>  Activity Accumulated during the entire month </h2>
<canvas id="myChartPerCDF_april2025" style="width:100%;max-width:600px"></canvas>

<script>


const xValues_april = 
[  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
const yCrossCountry_april = 
[  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const ySwimming_april = 
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];
const yGym_april =
[  0,  0,  1,  0,  0,  0,  0,  0,  0,0.5,  0,  0,  0,  0,  1,  0,  0,  0,1.5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0];


function Arrays_sum(array1, array2) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  if (array2.length === 0)
    return "array2 is empty";

  while (ctr < array1.length && ctr < array2.length) {
    result.push(array1[ctr] + array2[ctr]);
    ctr++;
  }

  if (ctr === array1.length) {
    for (x = ctr; x < array2.length; x++) {
      result.push(array2[x]);
    }
  } else {
    for (x = ctr; x < array1.length; x++) {
      result.push(array1[x]);
    }
  }

  return result;
};


function Arrays_cdf(array1) {
  var result = [];

  var ctr = 0;
  var x = 0;

  if (array1.length === 0)
    return "array1 is empty";

  while (ctr < array1.length ) {
	if (ctr === 0){
		x = array1[ctr];
		result.push(x);
	}else{
		x = x + array1[ctr];
		result.push(x);
	}
    ctr++;
  }

  return result;
};



new Chart("myChartPerDay_april2025", {
  type: "line",
  data: {
	labels: xValues_april,
	datasets: [{ 
	  data: yCrossCountry_april,
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: ySwimming_april,
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: yGym_april,
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  Arrays_sum( Arrays_sum(yCrossCountry_april,ySwimming_april), yGym_april ),
	  borderColor: "black",
	  label: " All activities per day ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Physical Activity per Day (# of Hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



new Chart("myChartPerCDF_april2025", {
  type: "line",
  data: {
	labels: xValues,
	datasets: [{ 
	  data: Arrays_cdf(yCrossCountry_april),
	  borderColor: "red",
	  label: "cross-country",
	  fill: false
	}, { 
	  data: Arrays_cdf(ySwimming_april),
	  borderColor: "green",
	  label: "swimming",
	  fill: false
	}, { 
	  data: Arrays_cdf( yGym_april),
	  borderColor: "blue",
	  label: "Gym",
	  fill: false
	}, { 
	  data:  Arrays_cdf(  Arrays_sum( Arrays_sum(yCrossCountry_april,ySwimming_april), yGym_april )  ),
	  borderColor: "black",
	  label: "Acculative of all activities ",
	  fill: false
	  }]
  },
  options: {
	scales: {
	  yAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'CDF (# of hours)'
		}
	  }],
	  xAxes: [{
	    scaleLabel: {
		  display: true,
		  labelString: 'Days'
		}
	  }]
	}
  }
});



</script>



<p id="demo"></p>

<p id="demo1"></p>

<p id="demo2"></p>

<script>
function myFunction(p1, p2) {
  return p1 * p2;
}
  
let result = myFunction(4, 5);
document.getElementById("demo").innerHTML = result;
</script>

<script>
function Arrays_sum(array1, array2) {
  return array1 * array2;
}

let output = Arrays_sum(5, 6);
document.getElementById("demo1").innerHTML = output;
</script>
</body>
</html>



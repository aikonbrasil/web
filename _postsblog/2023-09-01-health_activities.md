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

// Function to calculate the sum of corresponding elements from two arrays
function Arrays_sum(array1, array2) {
  // Initialize an empty array to store the sum of corresponding elements
  var result = [];

  // Initialize counters for iterating through the arrays
  var ctr = 0;
  var x = 0;

  // Check if array1 is empty, return an error message if true
  if (array1.length === 0)
    return "array1 is empty";

  // Check if array2 is empty, return an error message if true
  if (array2.length === 0)
    return "array2 is empty";

  // Iterate through arrays until the end of either array is reached
  while (ctr < array1.length && ctr < array2.length) {
    // Calculate the sum of corresponding elements and push it to the result array
    result.push(array1[ctr] + array2[ctr]);
    // Increment the counter
    ctr++;
  }

  // Check if array1 is exhausted
  if (ctr === array1.length) {
    // Append the remaining elements from array2 to the result array
    for (x = ctr; x < array2.length; x++) {
      result.push(array2[x]);
    }
  } else {
    // Append the remaining elements from array1 to the result array
    for (x = ctr; x < array1.length; x++) {
      result.push(array1[x]);
    }
  }

  // Return the resulting array
  return result;
};


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
	  data:  yGym ,
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
// console.log("progressAPI.js");

// just pass labels and data to the chart_func
let chart_func = function (labels_data, percent_data) {
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels_data,
      datasets: [
        {
          label: "% of Marks",
          data: percent_data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 2,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};

// http://127.0.0.1:8000/exam/api/student/progress?subject=596

// server side more vs client side more
// this means if server side is more then we'll use server side more for the simple logics
// which one is to select decided by which one is more efficient to handle load
let responseHandler = function (response) {
  //   console.log("responseHandler");
  //   console.log(response.data);
  let data = response.data;
  let data_arr = Object.entries(data);
  //   console.log("data array", data_arr);
  //   console.log(data);
  var table_rows = document.getElementById("table-rows");
  //   console.log(table_rows);
  tableinnerHTML = "";
  let labels_data_response = [];
  let percent_data_response = [];
  data_arr.forEach((elem) => {
    tableinnerHTML += `<div class="table-list table-rows">
    <h3 class="left-column">${elem[1][0]}</h3>
    <h3 class="right-column">${elem[1][1]}/${elem[1][2]} = ${elem[1][3]}%</h3>
  </div>`;
    labels_data_response.push(elem[1][0]);
    percent_data_response.push(elem[1][3]);
  });
  table_rows.innerHTML = tableinnerHTML;

  //   https://stackoverflow.com/questions/40056555/destroy-chart-js-bar-graph-to-redraw-other-graph-in-same-canvas
  // destroy the chart before redrawing
  let chartStatus = Chart.getChart("myChart"); // <canvas> id
  if (chartStatus != undefined) {
    chartStatus.destroy();
  }
  chart_func(labels_data_response, percent_data_response);
};

let submitHandler = function () {
  //   console.log("submitHandler");
  let subject = document.getElementById("subselect").value;
  //   console.log(subject);

  // axios request to get the data
  if (subject === "none") {
    alert("Please select a subject");
  } else {
    axios({
      method: "get",
      url: `/exam/api/student/progress?subject=${subject}`,
    })
      .then((res) => responseHandler(res))
      .catch((err) => console.log(err));
  }
};

//     let data = response.data;
//     let subject = data.subject;
//     let exams = data.exams;
//     let total = data.total;
//     let completed = data.completed;
//     let progress = Math.round((completed/total)*100);
//     let progressBar = document.getElementById('progressBar');
//     progressBar.style.width = `${progress}%`;
//     progressBar.innerHTML = `${progress}%`;
//     let progressText = document.getElementById('progressText');
//     progressText.innerHTML = `${completed}/${total}`;
//     let progressTitle = document.getElementById('progressTitle');
//     progressTitle.innerHTML = `${subject}`;

// charts
// https://stackoverflow.com/questions/7985450/eval-unexpected-token-error
// to use eval
console.log(mydata);
console.log(typeof mydata);
// JSON.parse(mydata);
console.log(typeof mydata);
console.log(Object.entries(mydata));

// use eval to convert string to object
// https://www.pluralsight.com/guides/convert-strings-to-json-objects-in-javascript-with-eval
eval("(" + mydata + ")");
console.log(typeof eval("(" + mydata + ")"));
mydata = eval("(" + mydata + ")");
console.log(mydata);
console.log(typeof mydata);

let mydata_arr = Object.entries(mydata);
let labels_data = [];
let percent_data = [];
mydata_arr.forEach((elem) => {
  // console.log(elem);
  labels_data.push(elem[1][0]);
  percent_data.push(elem[1][3]);
});

console.log(labels_data);
console.log(percent_data);

chart_func(labels_data, percent_data);

// In this, when we hit the progress page then we'll get the data from the django dictionary initially
// that is my data which is a dictionary
// then we'll convert it to a json string by using eval
// and we pass on the data to the chart_func function which will convert it to a chart
// chart_func needs only labels and data, in progress page that is labels_data and percent_data

// but if we hit the api for subject then we'll convert that incoming data into labels_data_response and percent_data_response
// and also we've destroyed the chart before redrawing
// and it's done new chart redraw successfully with the new data
// so we've used the chart_func function to redraw the chart with the new data but with same function

// in sum-up this progressAPI page only needs data in a format of json that will converted into Object.entries
// exam_id: [exam_name, marks, max_marks, percentage]

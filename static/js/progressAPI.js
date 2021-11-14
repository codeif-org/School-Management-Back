// console.log("progressAPI.js");

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
  data_arr.forEach((elem) => {
    tableinnerHTML += `<div class="table-list table-rows">
    <h3 class="left-column">${elem[1][0]}</h3>
    <h3 class="right-column">${elem[1][1]}/${elem[1][2]} = ${elem[1][3]}%</h3>
  </div>`;
  });
  table_rows.innerHTML = tableinnerHTML;
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

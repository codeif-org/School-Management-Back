// tutorial for javascript objects
// https://www.javascripttutorial.net/object/convert-an-object-to-an-array-in-javascript/
console.log("leaderboard.js");
var stud_list = document.getElementsByClassName("student-list")[0];
console.log(stud_list);
let responseHandler = function (res) {
  console.log("inside responseHandler", res.data);
  //   console.log(res.data);
  data = res.data;
  console.log(Object.entries(data));

  let stud_inner_html = "";
  
  let data_arr = Object.entries(data);

  var sortedArray = data_arr.sort(function(a, b) {
    if (a[1][2] == b[1][2]) {
      return a[1][1] - b[1][1];
    }
    return b[1][2] - a[1][2];
  });
  console.log("sorted array", sortedArray);
  //   student_id: student_name, roll_no, score
  console.log("data array", data_arr);
  let count = 1;
  data_arr.forEach((elem) => {
    // console.log(elem[1][0]);
    stud_inner_html =
      stud_inner_html +
      `<div class="add-stud-list">
    <p>
      ${count}. ${elem[1][0]} | ${elem[1][1]}
    </p>
    <h2>${elem[1][2]}</h2>
  </div>`;
    count++;
  });
  stud_list.innerHTML = stud_inner_html;
  console.log("done");
};

let submitHandler = function () {
  console.log("submitHandler");
  let exam = document.getElementById("examselect").value;
  let subject = document.getElementById("subselect").value;
  console.log(exam, subject);
  if (exam === "none" && subject === "none") {
    alert("Please select an exam or subject");
    return;
  }

  if (exam === "none" && subject !== "none") {
    url = "/exam/student/leaderboard/api/score?" + "subject=" + subject;
    console.log(url);
  } else if (exam !== "none" && subject === "none") {
    url = "/exam/student/leaderboard/api/score?" + "exam=" + exam;
    console.log(url);
  } else {
    url =
      "/exam/student/leaderboard/api/score?" +
      "exam=" +
      exam +
      "&subject=" +
      subject;
    console.log(url);
  }

  axios({
    method: "get",
    url: url,
  })
    .then((res) => responseHandler(res))
    .catch((err) => console.log(err));
};

// axios.get("http://127.0.0.1:8000/exam/student/leaderboard/api/score?subject=572&exam=384")
//         .then(function (response) {
//             console.log(response);
//             let data = response.data;
//             console.log(data);
//             let table = document.getElementById('leaderboard');
//             table.innerHTML = '';
//             let header = document.createElement('tr');
//             header.innerHTML = '<th>Rank</th><th>Name</th><th>Score</th>';
//             table.appendChild(header);
//             for (let i = 0; i < data.length; i++) {
//                 let row = document.createElement('tr');
//                 let rank = document.createElement('td');
//                 rank.innerHTML = i + 1;
//                 let name = document.createElement('td');
//                 name.innerHTML = data[i].name;
//                 let score = document.createElement('td');
//                 score.innerHTML = data[i].score;
//                 row.appendChild(rank);
//                 row.appendChild(name);
//                 row.appendChild(score);
//                 table.appendChild(row);
//             }
//         }

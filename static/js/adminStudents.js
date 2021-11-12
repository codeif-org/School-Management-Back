console.log("adminStudent.js");

let responseHandler = function (response) {
  console.log("responseHandler");
  // console.log(typeof(response.data));
  let studentList = document.getElementsByClassName("admin-stud-list")[0];
  //   console.log(studentList);

  let studentListItems = "";
  let arr_data = Object.entries(response.data);
  //   console.log(arr_data);
  for (let i = 0; i < arr_data.length; i++) {
    studentListItems += `<div class="stud-list-elem">
        <div>
          <p>${i + 1}. ${arr_data[i][1]}</p>
        </div>
      </div>`;
  }
  studentList.innerHTML = studentListItems;
};

let submitHandler = function (event) {
  console.log("submitHandler");
  // console.log(event.target.value);
  url = "/student/api/classStudent?" + "class=" + event.target.value;
  console.log(url);

  axios({
    method: "get",
    url: url,
  })
    .then((res) => responseHandler(res))
    .catch((err) => console.log(err));
};

// console.log(response);
//         let studentList = document.getElementById('studentList');
//         studentList.innerHTML = "";
//         response.data.forEach(function(student) {
//             let li = document.createElement('li');
//             li.innerHTML = student.name;
//             studentList.appendChild(li);

// import loadHandler from "./adminList.js";
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
        <div class="stud-list-elem-options">
              <button class="btn">Info</button>
              <button class="btn">Progress</button>
              <button class="btn">Attendance</button>
              <button class="btn">Start Discussion</button>
            </div>
      </div>`;
  }
  studentList.innerHTML = studentListItems;
  loadHandler();
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

// adminList.js
console.log("added adminList.js");

// let studs_list = document.querySelectorAll(".stud-list-elem");
// console.log(studs_list);

let compHandler = function (elem) {
  // console.log(elem);
  //   elemInnerHTML = elem.innerHTML;
  //   elem.innerHTML = elemInnerHTML + `Hello`;
  // console.log(elem.childNodes[3]);
  let btnElem = elem.childNodes[3];
  btnElem.classList.toggle("active-block");

  // studs_list.forEach((elem_) => {
  //   if (elem_ !== elem) {
  //     // console.log("yes");
  //     elem_.childNodes[3].classList.remove("active-block");
  //   }
  //   // else {
  //   //   console.log("no");
  //   // }
  // });
};

// studs_list.forEach((elem) => {
//   elem.addEventListener("click", function () {
//     compHandler(elem);
//   });
// });

var loadHandler = function () {
  console.log("loadHandler");
  let studs_list = document.querySelectorAll(".stud-list-elem");
  studs_list.forEach((elem) => {
    elem.addEventListener("click", function () {
      compHandler(elem);
    });
  });

  return 0;
};

window.onload = loadHandler();

// export default loadHandler();

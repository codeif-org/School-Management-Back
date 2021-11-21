axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";
console.log("exam.js added");
var student_elems = document.querySelectorAll(".marks-stud-list");
// var student_elems = document.querySelectorAll(".edit-student-marks");

// console.log(student_elems);

// student_elems.forEach((elem) => {
//   elem.addEventListener("click", clickHandler);
// }

// var clickHandler = function () {
//   console.log(elem);
//   // console.log(elem.childNodes[3])
//   // let editElem = elem.childNodes[3]
//   // console.log(editElem)
//   elem.parentNode.innerHTML = `<input type="text" class="student-marks-input"><i class="fas fa-check done-student-marks"></i>`;
//   // elem.classList.remove("edit-student-marks");
//   // elem.classList.add("done-student-marks");
//   done_elem_func();
// });

// let done_elem_func = function () {
//   let done_elem = document.querySelector(".done-student-marks");
//   console.log(done_elem);
//   let input_elem = document.querySelector(".student-marks-input");
//   console.log(input_elem);

//   done_elem.addEventListener("click", function () {
//     console.log(input_elem.value);
//     // console.log("inside done elem", done_elem)
//     done_elem.parentNode.innerHTML = `${input_elem.value}<i class="fas fa-edit edit-student-marks" onclick="marks_edit()"></i>`;
//     // var student_elems = document.querySelectorAll(".edit-student-marks");
//     // window.top.location.reload(true)
//     // marks_edit()
//   });
// };

var marks_edit = function (eve) {
  let elem = eve.target;
  // console.log(elem);
  elem.parentNode.innerHTML = `<input type="text" class="student-marks-input"><i class="fas fa-check done-student-marks" onclick="marks_done(event)"></i>`;
};

var marks_done = function (even) {
  let elem = even.target;
  // console.log(elem.parentNode.parentNode.parentNode);
  let id_elem = elem.parentNode.parentNode.parentNode.getAttribute("id");
  let ids = id_elem.split("-");
  console.log(id_elem);
  // let id_str = elem.getAttribute("id");
  // var ids = id_str.split("-");
  let done_elem = document.querySelector(".student-marks-input");
  elem.parentNode.innerHTML = `${done_elem.value}<i class="fas fa-edit edit-student-marks" onclick="marks_edit(event)"></i>`;
  // console.log("done elem typeof", typeof(done_elem.value));
  let marks = parseInt(done_elem.value);
  // console.log("marks", marks);
  // console.log("elem", elem);
  // console.log(ids);
  updateMarks(ids, marks);
};

var updateMarks = function (ids, marks) {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/exam/api/marksupdate/",
    data: {
      score: marks,
      exam_held: parseInt(ids[0]),
      stu: parseInt(ids[1]),
    },
    // xsrfHeaderName: "X-CSRFToken",
    // headers: { "X-CSRFToken": CSRF_TOKEN },
  })
    .then((res) => console.log(res.data.msg))
    .catch((err) => console.log(err));
};

// var student_elems = document.querySelectorAll(".marks-stud-list");
// console.log(student_elems);
// student_elems.forEach((elem) => {
//   elem.addEventListener("click", function () {
//     // console.log(elem)
//     let id_str = elem.getAttribute("id");
//     let ids = id_str.split("-");
//     // exam_id - student_id
//     console.log(typeof parseInt(ids[0]));
//     axios({
//       method: "post",
//       url: "http://127.0.0.1:8000/exam/api/marksupdate/",
//       data: {
//         score: 21,
//         exam: parseInt(ids[0]),
//         stu: parseInt(ids[1]),
//       },
//       // xsrfHeaderName: "X-CSRFToken",
//       // headers: { "X-CSRFToken": CSRF_TOKEN },
//     })
//       .then((res) => console.log(res))
//       .catch((err) => console.log(err));
//   });
// });

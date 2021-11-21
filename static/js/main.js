console.log("main js added");

// var elems = document.querySelectorAll(".att-student-list button");
// var elems = document.getElementsByClassName("att-btn")
// console.log(elems)
// elems.forEach((elem) => {
//   elem.addEventListener("click", (event) => {
//     clickHandler(event);
//   });
// });

// var clickHandler = function (event) {
//   // console.log("clicked")
//   // console.log(event.target)
//   event.target.classList.toggle("btn-clicked");

//   console.log(event.target);
//   let elem = event.target;
//   if (elem.parentNode.childNodes[3] === elem) {
//     console.log("print here");
//     toggle(elem.parentNode.childNodes[1]);
//   }

//   // console.log(elem.parentNode.childNodes[3])
//   // event.target.classList.toggle("btn-clicked")
// };

// var toggle = function (eleme) {
//   console.log("here eleme", eleme);
//   console.log(!("btn-clicked" in eleme.classList))
// //   if (eleme.classList.includes("btn-clicked")) {
// //     console.log("yes");
// //   }
// };

var requestHandler = function (req, value, student_id) {
  console.log("inside request handler");
  axios({
      method: req,
      url: "http://127.0.0.1:8000/attendance/teacher/api/saveAttendance/",
      data: {
          present: value,
          student: student_id,
          date: "2021-10-16",
      },
  })
    .then((res) => console.log(res))
    .catch((err) => console.log(err))
};

var btnHandler = function (event) {
  //   console.log(event);
  var elem = event.target;
  console.log(elem);
  let value = elem.value;
  let student_id = elem.parentNode.id;
  //   to find the sibling element and check if it is clicked or not

  if (
    elem.previousElementSibling &&
    elem.previousElementSibling.classList.contains("btn-clicked")
  ) {
    elem.previousElementSibling.classList.toggle("btn-clicked");
    elem.classList.toggle("btn-clicked");
    requestHandler("patch", value, student_id)
  } else if (
    elem.nextElementSibling &&
    elem.nextElementSibling.classList.contains("btn-clicked")
  ) {
    elem.nextElementSibling.classList.toggle("btn-clicked");
    elem.classList.toggle("btn-clicked");
    requestHandler("patch", value, student_id)
  } else {
    elem.classList.toggle("btn-clicked");
    console.log("nothing");
    requestHandler("post", value, student_id)
  }
};


// modal JS

var modalBtn = document.querySelectorAll('.modal-btn');
var modalBg = document.querySelector('.modal-bg');
var modalClose = document.querySelector('.modal-close')


modalBtn.forEach(element => {
  element.addEventListener('click' , function(){
    modalBg.classList.add('modal-active')
  });
});

modalClose.addEventListener('click' , function(){
    modalBg.classList.remove('modal-active')
  });
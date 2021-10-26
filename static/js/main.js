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

var btnHandler = function (event) {
  //   console.log(event);
  var elem = event.target;
  console.log(elem);
  elem.classList.toggle("btn-clicked");
  if (elem.previousElementSibling) {
    if (elem.previousElementSibling.classList.contains("btn-clicked")) {
      elem.previousElementSibling.classList.toggle("btn-clicked");
    }
  } else {
    if (elem.nextElementSibling) {
      if (elem.nextElementSibling.classList.contains("btn-clicked")) {
        elem.nextElementSibling.classList.toggle("btn-clicked");
      }
    }
  }
};

console.log("superadminExam.js");

let submitHandler = function (event) {
  event.preventDefault();
  // console.log("submitHandler");
  // console.log(event.target.value);
  let current_class = event.target.value;
  let exam_classes = document.querySelectorAll(".exam-class");
//   console.log(exam_classes);
  exam_classes.forEach((exam_class) => {
    // console.log(exam_class);
    // console.log(exam_class.innerHTML);
    let removing_elem =
      exam_class.parentElement.parentElement.parentElement.parentElement
        .parentElement;
    // console.log(current_class)
    if (exam_class.innerHTML !== current_class) {
    //   console.log("removing");
    //   console.log(removing_elem.classList);
      removing_elem.classList.add("none");
    } else {
        // console.log("adding");
        removing_elem.classList.remove("none");
    }
    // console.log(typeof(exam_class.innerHTML), typeof(current_class));
  });
};

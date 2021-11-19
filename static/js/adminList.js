console.log("added adminList.js");

// to find the height of the element from bottom of the page
// let elem = document.getElementsByClassName("tech-exam-list")[1]
// elem.scrollHeight - elem.scrollTop === elem.clientHeight
// elem.getBoundingClientRect().bottom
// window.innerHeight - elem.getBoundingClientRect().bottom

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

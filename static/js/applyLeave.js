// console.log("added adminList.js");

// let studs_list = document.querySelectorAll(".stud-list-elem");
// console.log(studs_list);

// let compHandler = function (elem) {
//   console.log(elem);
//   //   elemInnerHTML = elem.innerHTML;
//   //   elem.innerHTML = elemInnerHTML + `Hello`;
//   console.log(elem.parentNode.parentNode.childNodes[7]);
//   let btnElem = elem.parentNode.parentNode.childNodes[7];
//   console.log(btnElem)
//   btnElem.classList.toggle("active-block");

//   studs_list.forEach((elem_) => {
//     if (elem_ !== elem) {
//       // console.log("yes");
//       elem_.parentNode.parentNode.childNodes[7].classList.remove("active-block");
//     }
//     // else {
//     //   console.log("no");
//     // }
//   });
// };

// studs_list.forEach((elem) => {
//   elem.addEventListener("click", function () {
//     compHandler(elem);
//   });
// });

var applyLeave = document.querySelectorAll(".applyLeave")

applyLeave.forEach(element => {
  element.addEventListener('click' , function(){
    modalBg.classList.add('modal-active')
  });
});

modalClose.addEventListener('click' , function(){
    modalBg.classList.remove('modal-active')
  });
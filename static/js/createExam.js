console.log("added createExam.js");
let sub_input = document.querySelector(".sub-checkboxes");
console.log("sub_input: ", sub_input);

var obj = [
  {
    id: 1,
    name: "English",
  },
  {
    id: 2,
    name: "Hindi",
  },
  {
    id: 3,
    name: "Physics",
  },
  {
    id: 4,
    name: "Maths",
  },
];

let submitHandler = function (event) {
  console.log("function here");
  sub_input.innerHTML = "";
  let subInnerHTML = "";
  obj.forEach((elem) => {
    subInnerHTML =
      subInnerHTML +
      `<input type="checkbox" name="sub${elem.id}" id="sub${elem.id}">
      <label for="sub${elem.id}">${elem.name}</label> <br>`;
  });
  console.log(subInnerHTML);
  sub_input.innerHTML = subInnerHTML;
};

obj.forEach((elem) => {
  console.log(elem.name);
});

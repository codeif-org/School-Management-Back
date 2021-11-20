console.log("added createExam.js");
let sub_input = document.querySelector(".sub-checkboxes");
console.log("sub_input: ", sub_input);

console.log("user is: ", user)

// var obj = [
//   {
//     id: 1,
//     name: "English",
//   },
//   {
//     id: 2,
//     name: "Hindi",
//   },
//   {
//     id: 3,
//     name: "Physics",
//   },
//   {
//     id: 4,
//     name: "Maths",
//   },
// ];

let responseHandler = function (res) {
  console.log("inside responseHandler:", res.data);
  obj = res.data;
  sub_input.innerHTML = "";
  let subInnerHTML = "";
  obj.forEach((elem) => {
    subInnerHTML =
      subInnerHTML +
      `<input type="checkbox" name="sub" id="sub${elem.id}" value="${elem.id}">
      <label for="sub${elem.id}">${elem.subject}</label> <br>`;
  });
  // console.log(subInnerHTML);
  sub_input.innerHTML = subInnerHTML;
};

let requestHandler = function (event) {
  console.log("requestHandler Inside:", event.target.value);
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/teacher/api/subject/?user=${user}&class=${event.target.value}`,
  })
    .then((res) => responseHandler(res))
    .catch((err) => console.log(err));
};

let submitHandler = function (event) {
  obj = requestHandler(event);
  // console.log(obj)
  console.log("function here");
};

// obj.forEach((elem) => {
//   console.log(elem.name);
// });

console.log("progress js added");

let btns = document.querySelectorAll(".subject-btn");
let prevBtn = document.querySelectorAll(".subject-arrow")[0];
let nextBtn = document.querySelectorAll(".subject-arrow")[1];

let counter = 0;
let counterMax = btns.length - 3;

nextBtn.addEventListener("click", function () {
  if (counter < counterMax) {
    counter++;
    carousel();
    console.log(counter);
  } else {
    counter = 0;
    carousel();
    console.log(counter);
  }
});

prevBtn.addEventListener("click", function() {
    if (counter > 0){
        counter--
        carousel()
        console.log(counter)
    }
})

function carousel() {
  console.log("carousel calls");
  btns.forEach(function (btn) {
    btn.style.transform = `translateX(-${counter * 200}px)`;
  });
}
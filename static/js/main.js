console.log("main js added")

let elems = document.querySelectorAll('.att-student-list button')
elems.forEach((elem) => {
    elem.addEventListener('click', (event) => {
        clickHandler(event)
    })
})

function clickHandler(event) {
    // console.log("clicked")
    // console.log(event.target)
    console.log(event.target.tag)
    event.target.classList.toggle("btn-clicked")

}
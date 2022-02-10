console.log("searchStudent.js");

window.onload = function () {
  let search_add_no = document.getElementById("search-add-no");
  search_add_no.focus();
};

let searchStud = function (event, search_func) {
    // console.log(event.target.value);
    let input_value = event.target.value;
    // console.log(input_value);
    let table = document.getElementById("student-table");
    // console.log(table);
    let table_rows = table.getElementsByTagName("tr");
    // console.log(table_rows);

    // Loop through all table rows, and hide those who don't match the search query
    for (let i = 1; i < table_rows.length; i++) {
        let row = table_rows[i];
        let row_value = row.childNodes[search_func].innerText.toLowerCase();
        // console.log(row.childNodes)
        console.log(row_value);
        if (row_value.indexOf(input_value) === -1) {
            row.style.display = "none";
        } else {
            row.style.display = "";
        }
    }
}
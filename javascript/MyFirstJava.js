var initialValue = document.getElementById("Test1").innerHTML; 
function changeToNew() {
    document.getElementById("Test1").innerHTML = "This is changed to Bla Bla";
}
function changeToInitial() {
    document.getElementById("Test1").innerHTML = initialValue;
}

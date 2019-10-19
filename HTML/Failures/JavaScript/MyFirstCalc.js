function add(x,y) {
    var x = document.getElementById("x").innerHTML;
    var y = document.getElementById("y").innerHTML;
    x = parseFloat(x);
    x = parseFloat(x);
    total = x+y;
    displayResult(total);
    displayX(x);
    displayY(y);
}
function sub(x,y) {
    total = x-y;
    displayResult(total);
    displayX(x);
    displayY(y);
}
function mult(x,y) {
    total = x*y;
    displayResult(total);
    displayX(x);
    displayY(y);
}
function div(x,y) {
    total = x/y;
    displayResult(total);
    displayX(x);
    displayY(y);
}
function displayResult(total) {
    document.getElementById("Result").innerHTML = total;
}
function displayX(x) {
    document.getElementById("lineX").innerHTML = x;
}
function displayY(y) {
    document.getElementById("lineY").innerHTML = y;
}
var inputString = document.getElementById("inputString");

function pushedButton(obj) {
    debugger;
    var pushed = obj.innerHTML;

    if(pushed == '='){
        inputString.innerHTML = eval(inputString.innerHTML);
    }else if (pushed == 'AC'){
        inputString.innerHTML = '0';
    }else{
        if (inputString == '0'){
            inputString.innerHTML = pushed;
        }else{
            inputString.innerHTML += pushed;
        }

    }

}
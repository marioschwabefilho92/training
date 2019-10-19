var inputStringCalculator = document.getElementById('inputStringCalculator');

function pushedButton(obj){
    var whenPushed = obj.innerHTML;

    if(whenPushed == '='){
        inputStringCalculator.innerHTML = eval(inputStringCalculator.innerHTML);
    }else if (whenPushed == 'AC'){
        inputStringCalculator.innerHTML = '0';
    }else{
        if(inputStringCalculator.innerHTML == '0'){
            inputStringCalculator.innerHTML = whenPushed;
        }else{
            inputStringCalculator.innerHTML += whenPushed;
        }
    }
}
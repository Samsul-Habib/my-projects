//CALCULATOR PROGRAM

const display=document.getElementById('display');

function appendToDisplay(input){
    display.value+=input;
}

function clearDisplay(){
    display.value="";
}

function calculate(){
    try{
        display.value=eval(display.value);
        if (display.value.includes('%')) {
            // Remove the percentage sign and divide by 100 to get the actual percentage value
            let percentageValue = parseFloat(display.value.replace('%', '')) / 100;
            // Multiply the result by the percentage value
            display.value *= percentageValue;
        }
    }
    catch(error){
        display.value='Error';
    }
}


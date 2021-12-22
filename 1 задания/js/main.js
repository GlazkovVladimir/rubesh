const form = document.forms["form"];

form.addEventListener("input", inputHandler);

function inputHandler({target}) {
    if (targer.hasAttribute("data-reg")) {
        inputCheck(target);
    }
}

function inputCheck(el) {
    const inputValue = el.value;
    const inputReg = el.getAttribute("data-reg");
    const reg = new RegExp(inputReg);
    console.log(inputValue, reg);
    if(reg.test(inputValue)) {
        el.style.border = "2px solid rgb(0, 196, 0)"
    } else {
        el.style.border = "2px solid rgb(0, 255, 0)"
    }
}
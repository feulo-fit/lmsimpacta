const inputs = document.querySelectorAll("div.form-group input")

for(let i = 0; i < inputs.length; i++){
    inputs[i].classList.add("form-control")
}
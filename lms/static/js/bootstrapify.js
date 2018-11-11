const inputs = document.querySelectorAll("div.form-group input, div.form-group textarea, div.form-group select")

for(let i = 0; i < inputs.length; i++){
    inputs[i].classList.add("form-control")
}
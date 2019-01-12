const inputs = document.querySelectorAll("div.form-group input, div.form-group textarea, div.form-group select")

for(let i = 0; i < inputs.length; i++){
    if(inputs[i].type === 'file'){
        inputs[i].classList.add("form-control-file")
    } else {
        inputs[i].classList.add("form-control")
        if(i == 0) {
            inputs[i].focus()
        }
    }
}
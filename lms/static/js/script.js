function confirmar(event, objeto, href) {
    event.preventDefault()
    if(confirm('Deseja remover o objeto "'+objeto+'"?')){
        window.location = href
    }
}
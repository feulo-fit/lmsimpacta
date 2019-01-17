function confirmarRemocao(event, objeto, href) {
    event.preventDefault()
    if(confirm('Deseja remover o objeto "'+objeto+'"?')){
        window.location = href
    }
}

function confirmarSolicitacao(event, objeto, href) {
    event.preventDefault()
    if(confirm('Deseja solicitar a matrícula para a disciplina "'+objeto+'"?')){
        window.location = href
    }
}
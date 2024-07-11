window.onload = function() {
    // Chama a função para mostrar/ocultar campos com base na seleção da caixa de seleção "Defesa"
    showArtigoField();
    showBolsaField();

    /* Adicione um ouvinte de evento ao formulário para validar a URL antes de enviar
    document.getElementById("editar-aluno-form").addEventListener("submit", function(event) {
        // Chama a função de validação da URL antes de enviar o formulário
        if (!validarURL()) {
            // Impede o envio do formulário se a URL for inválida
            event.preventDefault();
        }
    });
    */
}

// Show "artigo" field only if "defesa" checkbox is checked.
function showArtigoField() {
    var checkBox = document.getElementById("id_defesa");
    var artigoField = document.getElementById("artigoField");
    var artigoDate = document.getElementById("artigoDate");
    
    if (checkBox.checked) {
        artigoField.style.display = "block";
        artigoDate.style.display = "block";
        
    } else {
        artigoField.style.display = "none";
        artigoDate.style.display = "none";
    }
}

function showBolsaField() {
    var checkBox = document.getElementById("id_eh_bolsista");
    var bolsaField = document.getElementById("bolsaField");

    if (checkBox.checked) {
        bolsaField.style.display = "block";
    } else {
        bolsaField.style.display = "none";
    }
}

/* Validate URL function
function validarURL() {
    var urlInput = document.getElementById("id_artigo");
    var urlError = document.getElementById("urlError");
    var url = urlInput.value.trim();
    
    var urlPattern = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/;

    if (!urlPattern.test(url)) {
        urlError.innerText = "URL inválida"; // Define a mensagem de erro
        urlInput.focus();
        return false;
    } 
    else {
        urlError.innerText = ""; // Limpa a mensagem de erro
        return true;
    }
}
*/
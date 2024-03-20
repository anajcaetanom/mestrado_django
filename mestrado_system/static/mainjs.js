function toggleArtigoField() {
    var artigoDate = document.getElementById("");
    var artigoField = document.getElementById("artigoField");
    var checkBox = document.getElementById("id_defesa");
    if (checkBox.checked) {
        artigoField.style.display = "block";
    } else {
        artigoField.style.display = "none";
    }
}

function validarURL() {
    var urlInput = document.getElementById("id_artigo");
    var urlError = document.getElementById("urlError");
    var urlErrorMessage = document.getElementById("urlErrorMessage"); // Adicione esta linha
    var url = urlInput.value.trim();
    
    var urlPattern = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/;

    if (!urlPattern.test(url)) {
        urlErrorMessage.style.display = "block";// Exibe a mensagem de erro
        urlInput.focus();
        return false;
    } 
    else {
        urlErrorMessage.style.display = "none"; // Oculta a mensagem de erro
        return true;
    }
}

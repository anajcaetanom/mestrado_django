// ############## JavaScript Functions ############## 


document.addEventListener('DOMContentLoaded', function() {
    // Show "artigo" field only if "defesa" checkbox is checked.
    function showArtigoField() {
        var checkBox = document.getElementById("id_defesa");
        var artigoField = document.getElementById("artigoField");
        var artigoDate = document.getElementById("");
        
        if (checkBox.checked) {
            artigoField.style.display = "block";
        } else {
            artigoField.style.display = "none";
        }
    }
}, false);


/*
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
*/
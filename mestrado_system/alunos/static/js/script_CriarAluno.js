window.onload = function() {
    // Chama a função para mostrar/ocultar campos com base na seleção das caixas de seleção "Defesa" e "Bolsista"
    showBolsaField();
};

// Função para mostrar/ocultar campos com base na seleção da caixa de seleção "Bolsista"
function showBolsaField() {
    var checkBox = document.getElementById("id_eh_bolsista");
    var bolsaField = document.getElementById("bolsaField");
    var nomeBolsaInput = document.getElementById("id_nome_da_bolsa")

    if (checkBox.checked) {
        bolsaField.style.display = "block";
        nomeBolsaInput.setAttribute("required", "true");
    } else {
        bolsaField.style.display = "none";
        
        // Limpar o valor do campo ao desmarcar o checkbox
        nomeBolsaInput.value = "";
        nomeBolsaInput.removeAttribute("required");
    }
}

// Adiciona ouvintes de evento às caixas de seleção para acionar as funções de mostrar/ocultar campos
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("id_eh_bolsista").addEventListener("change", showBolsaField);
});

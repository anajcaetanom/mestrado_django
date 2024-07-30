window.onload = function() {
    // Chama a função para mostrar/ocultar campos com base na seleção das caixas de seleção "Defesa" e "Bolsista"
    showArtigoField();
    showBolsaField();
};

// Função para mostrar/ocultar campos com base na seleção da caixa de seleção "Defesa"
function showArtigoField() {
    var checkBox = document.getElementById("id_defesa");
    var artigoField = document.getElementById("artigoField");
    var artigoDate = document.getElementById("artigoDate");
    var artigoInput = document.getElementById("id_artigo");
    var dataDefesaInput = document.getElementById("id_data_defesa");

    if (checkBox.checked) {
        // Exibe os campos de artigo e data
        artigoField.style.display = "block";
        artigoDate.style.display = "block";
        
        // Define os campos como obrigatórios
        artigoInput.setAttribute("required", "true");
        dataDefesaInput.setAttribute("required", "true");
    } else {
        // Oculta os campos de artigo e data
        artigoField.style.display = "none";
        artigoDate.style.display = "none";
        
        // Limpa os valores dos campos ao desmarcar o checkbox
        artigoInput.value = "";
        dataDefesaInput.value = "";
        
        // Remove a obrigatoriedade dos campos
        artigoInput.removeAttribute("required");
        dataDefesaInput.removeAttribute("required");
    }
}

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
    document.getElementById("id_defesa").addEventListener("change", showArtigoField);
    document.getElementById("id_eh_bolsista").addEventListener("change", showBolsaField);
});

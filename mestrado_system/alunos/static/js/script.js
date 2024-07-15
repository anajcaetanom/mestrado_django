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

    if (checkBox.checked) {
        artigoField.style.display = "block";
        artigoDate.style.display = "block";
    } else {
        artigoField.style.display = "none";
        artigoDate.style.display = "none";
        
        // Limpar os valores dos campos ao desmarcar o checkbox
        document.getElementById("id_artigo").value = "";
        document.getElementById("id_data_defesa").value = "";
    }
}

// Função para mostrar/ocultar campos com base na seleção da caixa de seleção "Bolsista"
function showBolsaField() {
    var checkBox = document.getElementById("id_eh_bolsista");
    var bolsaField = document.getElementById("bolsaField");

    if (checkBox.checked) {
        bolsaField.style.display = "block";
    } else {
        bolsaField.style.display = "none";
        
        // Limpar o valor do campo ao desmarcar o checkbox
        document.getElementById("id_nome_da_bolsa").value = "";
    }
}

// Adiciona ouvintes de evento às caixas de seleção para acionar as funções de mostrar/ocultar campos
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("id_defesa").addEventListener("change", showArtigoField);
    document.getElementById("id_eh_bolsista").addEventListener("change", showBolsaField);
});

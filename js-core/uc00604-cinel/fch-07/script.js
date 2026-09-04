// (8.1) Nome deve ter entre 5 e 10 caracteres

const formulario = document.querySelector("form");

const nome = document.getElementById("nome");

const email = document.getElementById("email");

// (8.3) Verificar se os campos foram preenchidos

const tipoBilhete = document.getElementById("tipoBilhete");

const termos = document.getElementById("termos");

const generos = document.querySelectorAll('input[name="genero"]');

const mensagem = document.getElementById("mensagem");


formulario.addEventListener("submit", function (evento) {

    evento.preventDefault();

    let formularioValido = true;

    const nomeValor = nome.value.trim();

    const emailValor = email.value.trim();


    // (8.1) Nome deve ter entre 5 e 10 caracteres

    if (nomeValor.length < 5 || nomeValor.length > 10) {

        formularioValido = false;

    }


    // (8.2) Email deve conter @

    if (!emailValor.includes("@")) {

        formularioValido = false;

    }


    // (8.3) Verificar se o tipo de bilhete foi selecionado

    if (tipoBilhete.value === "") {

        formularioValido = false;

    }


    // (8.3) Verificar se os Termos e Condições foram aceitos

    if (!termos.checked) {

        formularioValido = false;

    }


    // (8.3) Verificar se o género foi selecionado

    const generoSelecionado = document.querySelector(
        'input[name="genero"]:checked'
    );

    if (!generoSelecionado) {

        formularioValido = false;

    }


    // (9.1) Mensagem de sucesso

    if (!formularioValido) {

        // (9.2) Mensagem de erro

        mensagem.textContent =
            "Por favor, preencha corretamente todos os campos.";

        mensagem.style.color = "red";

    } else {

        // (9.1.1) Mensagem personalizada conforme o tipo de bilhete

        if (tipoBilhete.value === "geral") {

            mensagem.textContent =
                "Compra realizada com sucesso! Você comprou um Bilhete Geral.";

        } else if (tipoBilhete.value === "vip") {

            mensagem.textContent =
                "Compra realizada com sucesso! Você comprou um Bilhete VIP.";

        } else if (tipoBilhete.value === "estudante") {

            mensagem.textContent =
                "Compra realizada com sucesso! Você comprou um Bilhete Estudante.";

        }

        mensagem.style.color = "green";

    }

});
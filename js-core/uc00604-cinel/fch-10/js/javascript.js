// ==============================
// CARRINHO
// ==============================

let carrinho = [];


// ==============================
// ELEMENTOS
// ==============================

const botoesInscricao =
    document.querySelectorAll(".btn-inscricao");

const listaCarrinho =
    document.getElementById("lista-carrinho");

const totalElemento =
    document.getElementById("total");

const formulario =
    document.getElementById("form-inscricao");

const mensagem =
    document.getElementById("mensagem");


// ==============================
// ERRO PERSONALIZADO
// ==============================

class ErroInscricao extends Error {

    constructor(mensagem) {

        super(mensagem);

        this.name = "ErroInscricao";
    }
}


// ==============================
// ADICIONAR CURSO
// ==============================

function adicionarCurso(botao) {

    try {

        const curso = botao.dataset.curso;
        const preco = Number(botao.dataset.preco);
        const avancado = botao.dataset.avancado === "true";


        // Verifica curso avançado

        if (avancado) {

            throw new ErroInscricao(
                "O JavaScript Avançado está bloqueado. " +
                "É obrigatório concluir o JavaScript Básico primeiro."
            );
        }


        // Verifica dados

        if (!curso || isNaN(preco)) {

            throw new ErroInscricao(
                "Não foi possível adicionar este curso."
            );
        }


        // Verifica duplicação

        const jaExiste =
            carrinho.some(item => item.curso === curso);

        if (jaExiste) {

            throw new ErroInscricao(
                "Este curso já foi adicionado ao plano."
            );
        }


        // Adiciona ao carrinho

        carrinho.push({
            curso: curso,
            preco: preco
        });


        atualizarCarrinho();

        mostrarMensagem(
            `Curso "${curso}" adicionado ao plano.`,
            "sucesso"
        );

    } catch (erro) {

        mostrarMensagem(
            erro.message,
            "erro"
        );
    }
}


// ==============================
// ATUALIZAR CARRINHO
// ==============================

function atualizarCarrinho() {

    listaCarrinho.innerHTML = "";


    if (carrinho.length === 0) {

        listaCarrinho.innerHTML =
            '<p class="carrinho-vazio">' +
            'Nenhum curso selecionado.' +
            '</p>';

        totalElemento.textContent = "0,00 €";

        return;
    }


    carrinho.forEach((item, indice) => {

        const div =
            document.createElement("div");

        div.classList.add("item-carrinho");


        div.innerHTML = `
            <span>
                ${item.curso}
            </span>

            <span>
                ${formatarPreco(item.preco)}
            </span>

            <button
                type="button"
                onclick="removerCurso(${indice})">
                Remover
            </button>
        `;


        listaCarrinho.appendChild(div);
    });


    atualizarTotal();
}


// ==============================
// REMOVER CURSO
// ==============================

function removerCurso(indice) {

    try {

        if (
            indice < 0 ||
            indice >= carrinho.length
        ) {

            throw new ErroInscricao(
                "Curso inválido."
            );
        }


        carrinho.splice(indice, 1);

        atualizarCarrinho();

        mostrarMensagem(
            "Curso removido do plano.",
            "sucesso"
        );

    } catch (erro) {

        mostrarMensagem(
            erro.message,
            "erro"
        );
    }
}


// ==============================
// CALCULAR TOTAL
// ==============================

function calcularTotal() {

    return carrinho.reduce(
        (total, item) => total + item.preco,
        0
    );
}


// ==============================
// ATUALIZAR TOTAL
// ==============================

function atualizarTotal() {

    const total = calcularTotal();

    totalElemento.textContent =
        formatarPreco(total);
}


// ==============================
// FORMATAR PREÇO
// ==============================

function formatarPreco(valor) {

    return valor.toLocaleString(
        "pt-PT",
        {
            style: "currency",
            currency: "EUR"
        }
    );
}


// ==============================
// MENSAGENS
// ==============================

function mostrarMensagem(texto, tipo) {

    mensagem.textContent = texto;

    mensagem.className =
        `mensagem ${tipo}`;
}


// ==============================
// VALIDAR FORMULÁRIO
// ==============================

function validarFormulario() {

    const nome =
        document.getElementById("nome").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const termos =
        document.getElementById("termos").checked;


    // Verificar carrinho

    if (carrinho.length === 0) {

        throw new ErroInscricao(
            "Selecione pelo menos um curso."
        );
    }


    // Verificar nome

    if (!nome) {

        throw new ErroInscricao(
            "Preencha o campo Nome."
        );
    }


    // Verificar email

    if (!email) {

        throw new ErroInscricao(
            "Preencha o campo Email."
        );
    }


    // Verificar formato do email

    const formatoEmail =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    if (!formatoEmail.test(email)) {

        throw new ErroInscricao(
            "Insira um email válido."
        );
    }


    // Verificar termos

    if (!termos) {

        throw new ErroInscricao(
            "É necessário aceitar os Termos e Condições."
        );
    }


    return {
        nome: nome,
        email: email
    };
}


// ==============================
// FINALIZAR INSCRIÇÃO
// ==============================

function finalizarInscricao(evento) {

    evento.preventDefault();


    try {

        const dados =
            validarFormulario();

        const total =
            calcularTotal();


        const cursos =
            carrinho
                .map(item => item.curso)
                .join(", ");


        mostrarMensagem(
            `Inscrição realizada com sucesso, ${dados.nome}! ` +
            `Cursos: ${cursos}. ` +
            `Total a pagar: ${formatarPreco(total)}.`,
            "sucesso"
        );


    } catch (erro) {

        mostrarMensagem(
            erro.message,
            "erro"
        );
    }
}


// ==============================
// EVENTOS DOS BOTÕES
// ==============================

botoesInscricao.forEach(botao => {

    botao.addEventListener(
        "click",
        () => adicionarCurso(botao)
    );

});


// ==============================
// EVENTO DO FORMULÁRIO
// ==============================

formulario.addEventListener(
    "submit",
    finalizarInscricao
);


// ==============================
// INICIALIZAÇÃO
// ==============================

atualizarCarrinho();
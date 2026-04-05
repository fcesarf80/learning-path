package vetapp;

public class Vetapp {

    public static void main(String[] args) {

        Funcionario funcionario = new Funcionario();
        funcionario.setNome("Dr. House");
        funcionario.setFuncao("Veterinario");
        funcionario.setTelefone("900000000");
        funcionario.setEmail("house@vet.com");

        FuncionarioDAO dao = new FuncionarioDAO();
        dao.inserir(funcionario);
        dao.listar();
    }
}
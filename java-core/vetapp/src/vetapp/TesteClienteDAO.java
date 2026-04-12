package vetapp;

import vetapp.dao.ClienteDAO;
import vetapp.model.Cliente;

public class TesteClienteDAO {

    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.setNome("Fulano");
        cliente.setTelefone("919999999");
        cliente.setEmail("fulano@email.com");
        cliente.setEndereco("Rua X");

        ClienteDAO dao = new ClienteDAO();

        boolean sucesso = dao.inserir(cliente);

        if (sucesso) {
            System.out.println("Cliente inserido com sucesso!");
        } else {
            System.out.println("Erro ao inserir cliente.");
        }
    }
}
package vetapp;

import java.util.List;
import vetapp.dao.ClienteDAO;
import vetapp.model.Cliente;

public class TesteListarClientes {

    public static void main(String[] args) {
        ClienteDAO dao = new ClienteDAO();
        List<Cliente> clientes = dao.listar();

        for (Cliente c : clientes) {
            System.out.println("ID: " + c.getIdCliente());
            System.out.println("Nome: " + c.getNome());
            System.out.println("Telefone: " + c.getTelefone());
            System.out.println("Email: " + c.getEmail());
            System.out.println("Endereço: " + c.getEndereco());
            System.out.println("--------------------------");
        }
    }
}
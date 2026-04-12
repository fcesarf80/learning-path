package vetapp;

import vetapp.dao.ClienteDAO;
import vetapp.model.Cliente;

public class TesteClienteDAO {

    public static void main(String[] args) {

        Cliente cliente = new Cliente(
                "Tio Tomás Chorão",
                "912345678",
                "jchorão@email.com",
                "Rua Carroça a Vapor, 8"
        );

        ClienteDAO dao = new ClienteDAO();
        dao.inserir(cliente);
    }
}
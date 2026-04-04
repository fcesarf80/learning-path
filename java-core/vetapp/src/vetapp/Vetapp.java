package vetapp;

public class Vetapp {

    public static void main(String[] args) {

        ClienteDAO clienteDAO = new ClienteDAO();
        clienteDAO.listar();
    }
}
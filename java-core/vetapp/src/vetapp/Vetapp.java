package vetapp;

import vetapp.model.Cliente;
import vetapp.dao.ClienteDAO;

public class Vetapp {

    public static void main(String[] args) {
        // 1. Criar o cliente de teste
        Cliente c1 = new Cliente("Ana Souza", "912345678", "anaFerreira@email.com", "Rua de Cima, 10");

        // 2. Usar o DAO
        ClienteDAO dao = new ClienteDAO();
        
        System.out.println("A tentar inserir...");
        if (dao.inserir(c1)) {
            System.out.println("Inserção concluída com sucesso!");
        } else {
            System.out.println("Erro na inserção.");
        }

        // 3. Listar
        System.out.println("\n--- Lista de Clientes ---");
        for (Cliente c : dao.listar()) {
            System.out.println("ID: " + c.getIdCliente() + 
                               " | Nome: " + c.getNome() + 
                               " | Endereço: " + c.getEndereco());
        }
    } // Fecha o método main
} // Fecha a classe Vetapp (ESTA É A ÚLTIMA LINHA)

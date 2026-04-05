package vetapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class ClienteDAO {

    public void inserir(Cliente cliente) {

        String sql = "INSERT INTO cliente (nome, telefone, email) VALUES (?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, cliente.getNome());
            stmt.setString(2, cliente.getTelefone());
            stmt.setString(3, cliente.getEmail());

            stmt.executeUpdate();
            System.out.println("Cliente inserido com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir cliente:");
            e.printStackTrace();
        }
    }

    public void listar() {

        String sql = "SELECT * FROM cliente";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id_cliente"));
                System.out.println("Nome: " + rs.getString("nome"));
                System.out.println("Telefone: " + rs.getString("telefone"));
                System.out.println("Email: " + rs.getString("email"));
                System.out.println("-----------------------------");
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar clientes:");
            e.printStackTrace();
        }
    }
    public void atualizar(Cliente cliente) {

    String sql = "UPDATE cliente SET nome = ?, telefone = ?, email = ? WHERE id_cliente = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setString(1, cliente.getNome());
        stmt.setString(2, cliente.getTelefone());
        stmt.setString(3, cliente.getEmail());
        stmt.setInt(4, cliente.getIdCliente());

        stmt.executeUpdate();
        System.out.println("Cliente atualizado com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao atualizar cliente:");
        e.printStackTrace();
    }
}
    public void deletar(int idCliente) {

    String sql = "DELETE FROM cliente WHERE id_cliente = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setInt(1, idCliente);

        stmt.executeUpdate();
        System.out.println("Cliente deletado com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao deletar cliente:");
        e.printStackTrace();
    }
}
}
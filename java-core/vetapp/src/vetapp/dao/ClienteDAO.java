package vetapp.dao;

import vetapp.model.Cliente;
import vetapp.util.Conexao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ClienteDAO {

    public boolean inserir(Cliente cliente) {
        String sql = "INSERT INTO cliente (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, cliente.getNome());
            stmt.setString(2, cliente.getTelefone());
            stmt.setString(3, cliente.getEmail());
            stmt.setString(4, cliente.getEndereco());

            int linhasAfetadas = stmt.executeUpdate();

            if (linhasAfetadas > 0) {
                System.out.println("Cliente inserido com sucesso!");
                return true;
            } else {
                System.out.println("Nenhum cliente foi inserido.");
                return false;
            }

        } catch (SQLException e) {
            System.out.println("Erro ao inserir cliente:");
            e.printStackTrace();
            return false;
        }
    }

    public List<Cliente> listarClientes() {
    List<Cliente> lista = new ArrayList<>();
    String sql = "SELECT * FROM cliente ORDER BY id_cliente";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql);
         ResultSet rs = stmt.executeQuery()) {

        while (rs.next()) {
            Cliente cliente = new Cliente();

            cliente.setIdCliente(rs.getInt("id_cliente"));
            cliente.setNome(rs.getString("nome"));
            cliente.setTelefone(rs.getString("telefone"));
            cliente.setEmail(rs.getString("email"));
            cliente.setEndereco(rs.getString("endereco"));

            lista.add(cliente);
        }

    } catch (SQLException e) {
        System.out.println("Erro ao listar clientes:");
        e.printStackTrace();
    }

    return lista;
}

    public Cliente buscarPorId(int idCliente) {
        String sql = "SELECT * FROM cliente WHERE id_cliente = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idCliente);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Cliente cliente = new Cliente();

                    cliente.setIdCliente(rs.getInt("id_cliente"));
                    cliente.setNome(rs.getString("nome"));
                    cliente.setTelefone(rs.getString("telefone"));
                    cliente.setEmail(rs.getString("email"));
                    cliente.setEndereco(rs.getString("endereco"));

                    return cliente;
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar cliente por ID:");
            e.printStackTrace();
        }

        return null;
    }

    public boolean atualizar(Cliente cliente) {
        String sql = "UPDATE cliente SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id_cliente = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, cliente.getNome());
            stmt.setString(2, cliente.getTelefone());
            stmt.setString(3, cliente.getEmail());
            stmt.setString(4, cliente.getEndereco());
            stmt.setInt(5, cliente.getIdCliente());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar cliente:");
            e.printStackTrace();
            return false;
        }
    }

    public boolean deletar(int idCliente) {
        String sql = "DELETE FROM cliente WHERE id_cliente = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idCliente);

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            if (e.getSQLState() != null && e.getSQLState().startsWith("23")) {
                System.out.println("Não é possível excluir o cliente porque ele possui registros relacionados.");
            } else {
                System.out.println("Erro ao deletar cliente:");
                e.printStackTrace();
            }
            return false;
        }
    }
}
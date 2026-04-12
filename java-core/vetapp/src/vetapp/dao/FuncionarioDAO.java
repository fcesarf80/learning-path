package vetapp.dao;

import vetapp.model.Funcionario;
import vetapp.util.Conexao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class FuncionarioDAO {

    public boolean inserir(Funcionario funcionario) {
        String sql = "INSERT INTO funcionario (nome, funcao, telefone, email) VALUES (?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, funcionario.getNome());
            stmt.setString(2, funcionario.getFuncao());
            stmt.setString(3, funcionario.getTelefone());
            stmt.setString(4, funcionario.getEmail());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao inserir funcionário:");
            e.printStackTrace();
            return false;
        }
    }

    public List<Funcionario> listarFuncionarios() {
        List<Funcionario> lista = new ArrayList<>();
        String sql = "SELECT * FROM funcionario ORDER BY id_funcionario";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Funcionario funcionario = new Funcionario();

                funcionario.setIdFuncionario(rs.getInt("id_funcionario"));
                funcionario.setNome(rs.getString("nome"));
                funcionario.setFuncao(rs.getString("funcao"));
                funcionario.setTelefone(rs.getString("telefone"));
                funcionario.setEmail(rs.getString("email"));

                lista.add(funcionario);
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar funcionários:");
            e.printStackTrace();
        }

        return lista;
    }

    public Funcionario buscarPorId(int idFuncionario) {
        String sql = "SELECT * FROM funcionario WHERE id_funcionario = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idFuncionario);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Funcionario funcionario = new Funcionario();

                    funcionario.setIdFuncionario(rs.getInt("id_funcionario"));
                    funcionario.setNome(rs.getString("nome"));
                    funcionario.setFuncao(rs.getString("funcao"));
                    funcionario.setTelefone(rs.getString("telefone"));
                    funcionario.setEmail(rs.getString("email"));

                    return funcionario;
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar funcionário por ID:");
            e.printStackTrace();
        }

        return null;
    }

    public boolean atualizar(Funcionario funcionario) {
        String sql = "UPDATE funcionario SET nome = ?, funcao = ?, telefone = ?, email = ? WHERE id_funcionario = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, funcionario.getNome());
            stmt.setString(2, funcionario.getFuncao());
            stmt.setString(3, funcionario.getTelefone());
            stmt.setString(4, funcionario.getEmail());
            stmt.setInt(5, funcionario.getIdFuncionario());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar funcionário:");
            e.printStackTrace();
            return false;
        }
    }

    public boolean deletar(int idFuncionario) {
        String sql = "DELETE FROM funcionario WHERE id_funcionario = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idFuncionario);

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao deletar funcionário:");
            e.printStackTrace();
            return false;
        }
    }
}
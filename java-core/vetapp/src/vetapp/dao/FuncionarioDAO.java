package vetapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class FuncionarioDAO {

    public void inserir(Funcionario funcionario) {

        String sql = "INSERT INTO funcionario (nome, funcao, telefone, email) VALUES (?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, funcionario.getNome());
            stmt.setString(2, funcionario.getFuncao());
            stmt.setString(3, funcionario.getTelefone());
            stmt.setString(4, funcionario.getEmail());

            stmt.executeUpdate();
            System.out.println("Funcionario inserido com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir funcionario:");
            e.printStackTrace();
        }
    }

    public void listar() {

        String sql = "SELECT * FROM funcionario";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id_funcionario"));
                System.out.println("Nome: " + rs.getString("nome"));
                System.out.println("Funcao: " + rs.getString("funcao"));
                System.out.println("Telefone: " + rs.getString("telefone"));
                System.out.println("Email: " + rs.getString("email"));
                System.out.println("-----------------------------");
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar funcionarios:");
            e.printStackTrace();
        }
    }
    public void atualizar(Funcionario funcionario) {

    String sql = "UPDATE funcionario SET nome = ?, funcao = ?, telefone = ?, email = ? WHERE id_funcionario = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setString(1, funcionario.getNome());
        stmt.setString(2, funcionario.getFuncao());
        stmt.setString(3, funcionario.getTelefone());
        stmt.setString(4, funcionario.getEmail());
        stmt.setInt(5, funcionario.getIdFuncionario());

        stmt.executeUpdate();
        System.out.println("Funcionario atualizado com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao atualizar funcionario:");
        e.printStackTrace();
    }
}
    public void deletar(int idFuncionario) {

    String sql = "DELETE FROM funcionario WHERE id_funcionario = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setInt(1, idFuncionario);

        stmt.executeUpdate();
        System.out.println("Funcionario deletado com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao deletar funcionario:");
        e.printStackTrace();
    }
}
}
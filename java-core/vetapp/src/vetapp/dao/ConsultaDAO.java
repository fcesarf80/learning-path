package vetapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ConsultaDAO {

    public void inserir(Consulta consulta) {

        String sql = "INSERT INTO consulta (data_consulta, descricao, valor, id_animal, id_funcionario) VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, consulta.getDataConsulta());
            stmt.setString(2, consulta.getDescricao());
            stmt.setDouble(3, consulta.getValor());
            stmt.setInt(4, consulta.getIdAnimal());
            stmt.setInt(5, consulta.getIdFuncionario());

            stmt.executeUpdate();
            System.out.println("Consulta inserida com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir consulta:");
            e.printStackTrace();
        }
    }

    public void listar() {

        String sql = "SELECT * FROM consulta";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id_consulta"));
                System.out.println("Data: " + rs.getString("data_consulta"));
                System.out.println("Descricao: " + rs.getString("descricao"));
                System.out.println("Valor: " + rs.getDouble("valor"));
                System.out.println("ID Animal: " + rs.getInt("id_animal"));
                System.out.println("ID Funcionario: " + rs.getInt("id_funcionario"));
                System.out.println("-----------------------------");
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar consultas:");
            e.printStackTrace();
        }
    }
    public void atualizar(Consulta consulta) {

    String sql = "UPDATE consulta SET data_consulta = ?, descricao = ?, valor = ?, id_animal = ?, id_funcionario = ? WHERE id_consulta = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setString(1, consulta.getDataConsulta());
        stmt.setString(2, consulta.getDescricao());
        stmt.setDouble(3, consulta.getValor());
        stmt.setInt(4, consulta.getIdAnimal());
        stmt.setInt(5, consulta.getIdFuncionario());
        stmt.setInt(6, consulta.getIdConsulta());

        stmt.executeUpdate();
        System.out.println("Consulta atualizada com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao atualizar consulta:");
        e.printStackTrace();
    }
}

public void deletar(int idConsulta) {

    String sql = "DELETE FROM consulta WHERE id_consulta = ?";

    try (Connection conn = Conexao.conectar();
         PreparedStatement stmt = conn.prepareStatement(sql)) {

        stmt.setInt(1, idConsulta);

        stmt.executeUpdate();
        System.out.println("Consulta deletada com sucesso!");

    } catch (SQLException e) {
        System.out.println("Erro ao deletar consulta:");
        e.printStackTrace();
    }
}
}

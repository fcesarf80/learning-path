package vetapp.dao;

import vetapp.model.Consulta;
import vetapp.util.Conexao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ConsultaDAO {

    public boolean inserir(Consulta consulta) {
        String sql = "INSERT INTO consulta (data_consulta, hora_consulta, observacao, id_animal, id_funcionario) VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, consulta.getDataConsulta());
            stmt.setString(2, consulta.getHoraConsulta());
            stmt.setString(3, consulta.getObservacao());
            stmt.setInt(4, consulta.getIdAnimal());
            stmt.setInt(5, consulta.getIdFuncionario());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao inserir consulta:");
            e.printStackTrace();
            return false;
        }
    }

    public List<Consulta> listarConsultas() {
        List<Consulta> lista = new ArrayList<>();

        String sql = "SELECT * FROM consulta ORDER BY id_consulta DESC";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Consulta consulta = new Consulta();

                consulta.setIdConsulta(rs.getInt("id_consulta"));
                consulta.setDataConsulta(rs.getString("data_consulta"));
                consulta.setHoraConsulta(rs.getString("hora_consulta"));
                consulta.setObservacao(rs.getString("observacao"));
                consulta.setIdAnimal(rs.getInt("id_animal"));
                consulta.setIdFuncionario(rs.getInt("id_funcionario"));

                lista.add(consulta);
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar consultas:");
            e.printStackTrace();
        }

        return lista;
    }

    public Consulta buscarPorId(int idConsulta) {
        String sql = "SELECT * FROM consulta WHERE id_consulta = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idConsulta);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Consulta consulta = new Consulta();

                    consulta.setIdConsulta(rs.getInt("id_consulta"));
                    consulta.setDataConsulta(rs.getString("data_consulta"));
                    consulta.setHoraConsulta(rs.getString("hora_consulta"));
                    consulta.setObservacao(rs.getString("observacao"));
                    consulta.setIdAnimal(rs.getInt("id_animal"));
                    consulta.setIdFuncionario(rs.getInt("id_funcionario"));

                    return consulta;
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar consulta por ID:");
            e.printStackTrace();
        }

        return null;
    }

    public boolean atualizar(Consulta consulta) {
        String sql = "UPDATE consulta SET data_consulta = ?, hora_consulta = ?, observacao = ?, id_animal = ?, id_funcionario = ? WHERE id_consulta = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, consulta.getDataConsulta());
            stmt.setString(2, consulta.getHoraConsulta());
            stmt.setString(3, consulta.getObservacao());
            stmt.setInt(4, consulta.getIdAnimal());
            stmt.setInt(5, consulta.getIdFuncionario());
            stmt.setInt(6, consulta.getIdConsulta());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar consulta:");
            e.printStackTrace();
            return false;
        }
    }

    public boolean deletar(int idConsulta) {
        String sql = "DELETE FROM consulta WHERE id_consulta = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idConsulta);

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao deletar consulta:");
            e.printStackTrace();
            return false;
        }
    }
}
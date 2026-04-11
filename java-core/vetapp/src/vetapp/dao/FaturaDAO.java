package vetapp.dao;

import vetapp.model.Fatura;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import vetapp.util.Conexao;

public class FaturaDAO {

    public boolean inserir(Fatura fatura) {
        String sql = "INSERT INTO fatura (data_emissao, valor_total, estado, id_cliente, id_consulta) VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, fatura.getDataEmissao());
            stmt.setDouble(2, fatura.getValorTotal());
            stmt.setString(3, fatura.getEstado());
            stmt.setInt(4, fatura.getIdCliente());
            stmt.setInt(5, fatura.getIdConsulta());

            stmt.executeUpdate();
            return true;

        } catch (SQLException e) {
            System.out.println("Erro ao inserir fatura:");
            e.printStackTrace();
            return false;
        }
    }

    public List<Fatura> listar() {
        List<Fatura> lista = new ArrayList<>();
        String sql = "SELECT * FROM fatura ORDER BY id_fatura";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Fatura fatura = new Fatura();

                fatura.setIdFatura(rs.getInt("id_fatura"));
                fatura.setDataEmissao(rs.getString("data_emissao"));
                fatura.setValorTotal(rs.getDouble("valor_total"));
                fatura.setEstado(rs.getString("estado"));
                fatura.setIdCliente(rs.getInt("id_cliente"));
                fatura.setIdConsulta(rs.getInt("id_consulta"));

                lista.add(fatura);
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar faturas:");
            e.printStackTrace();
        }

        return lista;
    }

    public Fatura buscarPorId(int idFatura) {
        String sql = "SELECT * FROM fatura WHERE id_fatura = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idFatura);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Fatura fatura = new Fatura();

                    fatura.setIdFatura(rs.getInt("id_fatura"));
                    fatura.setDataEmissao(rs.getString("data_emissao"));
                    fatura.setValorTotal(rs.getDouble("valor_total"));
                    fatura.setEstado(rs.getString("estado"));
                    fatura.setIdCliente(rs.getInt("id_cliente"));
                    fatura.setIdConsulta(rs.getInt("id_consulta"));

                    return fatura;
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar fatura por ID:");
            e.printStackTrace();
        }

        return null;
    }

    public boolean atualizar(Fatura fatura) {
        String sql = "UPDATE fatura SET data_emissao = ?, valor_total = ?, estado = ?, id_cliente = ?, id_consulta = ? WHERE id_fatura = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, fatura.getDataEmissao());
            stmt.setDouble(2, fatura.getValorTotal());
            stmt.setString(3, fatura.getEstado());
            stmt.setInt(4, fatura.getIdCliente());
            stmt.setInt(5, fatura.getIdConsulta());
            stmt.setInt(6, fatura.getIdFatura());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar fatura:");
            e.printStackTrace();
            return false;
        }
    }

    public boolean deletar(int idFatura) {
        String sql = "DELETE FROM fatura WHERE id_fatura = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idFatura);

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao deletar fatura:");
            e.printStackTrace();
            return false;
        }
    }
}
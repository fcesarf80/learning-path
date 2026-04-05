package vetapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class FaturaDAO {

    public void inserir(Fatura fatura) {

        String sql = "INSERT INTO fatura (data_emissao, valor_total, estado, id_cliente, id_consulta) VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, fatura.getDataEmissao());
            stmt.setDouble(2, fatura.getValorTotal());
            stmt.setString(3, fatura.getEstado());
            stmt.setInt(4, fatura.getIdCliente());
            stmt.setInt(5, fatura.getIdConsulta());

            stmt.executeUpdate();
            System.out.println("Fatura inserida com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir fatura:");
            e.printStackTrace();
        }
    }

    public void listar() {

        String sql = "SELECT * FROM fatura";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                System.out.println("ID Fatura: " + rs.getInt("id_fatura"));
                System.out.println("Data Emissao: " + rs.getString("data_emissao"));
                System.out.println("Valor Total: " + rs.getDouble("valor_total"));
                System.out.println("Estado: " + rs.getString("estado"));
                System.out.println("ID Cliente: " + rs.getInt("id_cliente"));
                System.out.println("ID Consulta: " + rs.getInt("id_consulta"));
                System.out.println("-----------------------------");
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar faturas:");
            e.printStackTrace();
        }
    }
}
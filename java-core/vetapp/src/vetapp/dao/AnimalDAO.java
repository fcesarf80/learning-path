package vetapp;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class AnimalDAO {

    public void inserir(Animal animal) {

        String sql = "INSERT INTO animal (nome, especie, raca, id_cliente) VALUES (?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, animal.getNome());
            stmt.setString(2, animal.getEspecie());
            stmt.setString(3, animal.getRaca());
            stmt.setInt(4, animal.getIdCliente());

            stmt.executeUpdate();
            System.out.println("Animal inserido com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir animal:");
            e.printStackTrace();
        }
    }

    public void listar() {

        String sql = "SELECT * FROM animal";

        try (Connection conn = Conexao.conectar();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                System.out.println("ID Animal: " + rs.getInt("id_animal"));
                System.out.println("Nome: " + rs.getString("nome"));
                System.out.println("Especie: " + rs.getString("especie"));
                System.out.println("Raca: " + rs.getString("raca"));
                System.out.println("ID Cliente: " + rs.getInt("id_cliente"));
                System.out.println("-----------------------------");
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar animais:");
            e.printStackTrace();
        }
    }

    public void atualizar(Animal animal) {

        String sql = "UPDATE animal SET nome = ?, especie = ?, raca = ? WHERE id_animal = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, animal.getNome());
            stmt.setString(2, animal.getEspecie());
            stmt.setString(3, animal.getRaca());
            stmt.setInt(4, animal.getIdAnimal());

            stmt.executeUpdate();
            System.out.println("Animal atualizado com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar animal:");
            e.printStackTrace();
        }
    }

    public void deletar(int idAnimal) {

        String sql = "DELETE FROM animal WHERE id_animal = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idAnimal);

            stmt.executeUpdate();
            System.out.println("Animal deletado com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao deletar animal:");
            e.printStackTrace();
        }
    }
}
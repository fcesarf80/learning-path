package vetapp.dao;

import vetapp.model.Animal;
import vetapp.util.Conexao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class AnimalDAO {

    public boolean inserir(Animal animal) {
        String sql = "INSERT INTO animal (nome, especie, raca, sexo, data_nascimento, id_cliente) VALUES (?, ?, ?, ?, ?, ?)";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, animal.getNome());
            stmt.setString(2, animal.getEspecie());
            stmt.setString(3, animal.getRaca());
            stmt.setString(4, animal.getSexo());
            stmt.setString(5, animal.getDataNascimento());
            stmt.setInt(6, animal.getIdCliente());

            int linhasAfetadas = stmt.executeUpdate();

            if (linhasAfetadas > 0) {
                System.out.println("Animal inserido com sucesso!");
                return true;
            } else {
                System.out.println("Nenhum animal foi inserido.");
                return false;
            }

        } catch (SQLException e) {
            System.out.println("Erro ao inserir animal:");
            e.printStackTrace();
            return false;
        }
    }

    public List<Animal> listar() {
        List<Animal> lista = new ArrayList<>();
        String sql = "SELECT * FROM animal ORDER BY id_animal DESC";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Animal animal = new Animal();

                animal.setIdAnimal(rs.getInt("id_animal"));
                animal.setNome(rs.getString("nome"));
                animal.setEspecie(rs.getString("especie"));
                animal.setRaca(rs.getString("raca"));
                animal.setSexo(rs.getString("sexo"));
                animal.setDataNascimento(rs.getString("data_nascimento"));
                animal.setIdCliente(rs.getInt("id_cliente"));

                lista.add(animal);
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar animais:");
            e.printStackTrace();
        }

        return lista;
    }

    public Animal buscarPorId(int idAnimal) {
        String sql = "SELECT * FROM animal WHERE id_animal = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idAnimal);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Animal animal = new Animal();

                    animal.setIdAnimal(rs.getInt("id_animal"));
                    animal.setNome(rs.getString("nome"));
                    animal.setEspecie(rs.getString("especie"));
                    animal.setRaca(rs.getString("raca"));
                    animal.setSexo(rs.getString("sexo"));
                    animal.setDataNascimento(rs.getString("data_nascimento"));
                    animal.setIdCliente(rs.getInt("id_cliente"));

                    return animal;
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar animal por ID:");
            e.printStackTrace();
        }

        return null;
    }

    public boolean atualizar(Animal animal) {
        String sql = "UPDATE animal SET nome = ?, especie = ?, raca = ?, sexo = ?, data_nascimento = ?, id_cliente = ? WHERE id_animal = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, animal.getNome());
            stmt.setString(2, animal.getEspecie());
            stmt.setString(3, animal.getRaca());
            stmt.setString(4, animal.getSexo());
            stmt.setString(5, animal.getDataNascimento());
            stmt.setInt(6, animal.getIdCliente());
            stmt.setInt(7, animal.getIdAnimal());

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar animal:");
            e.printStackTrace();
            return false;
        }
    }

    public boolean deletar(int idAnimal) {
        String sql = "DELETE FROM animal WHERE id_animal = ?";

        try (Connection conn = Conexao.conectar();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, idAnimal);

            int linhasAfetadas = stmt.executeUpdate();
            return linhasAfetadas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao deletar animal:");
            e.printStackTrace();
            return false;
        }
    }
}
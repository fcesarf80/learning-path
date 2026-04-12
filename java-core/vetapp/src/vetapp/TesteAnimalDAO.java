package vetapp;

import vetapp.dao.AnimalDAO;
import vetapp.model.Animal;

import java.util.List;

public class TesteAnimalDAO {

    public static void main(String[] args) {

        AnimalDAO dao = new AnimalDAO();

        // TESTE 1 - Inserir
        Animal animal = new Animal();
        animal.setNome("Zumba");
        animal.setEspecie("Cachorro");
        animal.setRaca("SRD");
        animal.setSexo("M");
        animal.setDataNascimento("2020-05-10");
        animal.setIdCliente(1); // ⚠️ use um ID que exista na tabela cliente

        dao.inserir(animal);

        // TESTE 2 - Listar
        System.out.println("===== LISTANDO ANIMAIS =====");

        List<Animal> lista = dao.listar();

        for (Animal a : lista) {
            System.out.println("ID: " + a.getIdAnimal());
            System.out.println("Nome: " + a.getNome());
            System.out.println("Espécie: " + a.getEspecie());
            System.out.println("Raça: " + a.getRaca());
            System.out.println("Sexo: " + a.getSexo());
            System.out.println("Data Nascimento: " + a.getDataNascimento());
            System.out.println("ID Cliente: " + a.getIdCliente());
            System.out.println("--------------------------");
        }
    }
}
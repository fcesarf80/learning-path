package vetapp;

public class Vetapp {

    public static void main(String[] args) {

        ConsultaDAO dao = new ConsultaDAO();
        dao.deletar(1);
        dao.listar();
    }
}
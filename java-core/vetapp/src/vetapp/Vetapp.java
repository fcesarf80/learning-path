package vetapp;

public class Vetapp {

    public static void main(String[] args) {

        FaturaDAO dao = new FaturaDAO();
        dao.deletar(1);
        dao.listar();
    }
}
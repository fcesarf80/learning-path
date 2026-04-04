package vetapp;

import java.sql.Connection;
import java.sql.SQLException;

public class Vetapp {

    public static void main(String[] args) {

        try {
            Connection conn = Conexao.conectar();
            System.out.println("Conectado com sucesso ao MySQL!");
        } catch (SQLException e) {
            System.out.println("Erro ao conectar:");
            e.printStackTrace();
        }
    }
}




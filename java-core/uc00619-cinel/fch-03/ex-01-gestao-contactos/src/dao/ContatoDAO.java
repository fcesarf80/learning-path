package dao;

import model.Contato;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class ContatoDAO {

    private static final String ARQUIVO = "contatos.txt";

    public void salvar(Contato contato) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(ARQUIVO, true));
        bw.write(contato.toFileString());
        bw.newLine();
        bw.close();
    }
}
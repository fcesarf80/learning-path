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
    
    public java.util.List<Contato> listar() throws IOException {
    java.util.List<Contato> lista = new java.util.ArrayList<>();

    java.io.File file = new java.io.File(ARQUIVO);
    if (!file.exists()) {
        return lista;
    }

    try (java.io.BufferedReader br = new java.io.BufferedReader(new java.io.FileReader(file))) {
        String linha;

        while ((linha = br.readLine()) != null) {
            String[] dados = linha.split(";");

            if (dados.length == 4) {
                Contato contato = new Contato(dados[0], dados[1], dados[2], dados[3]);
                lista.add(contato);
            }
        }
    }

    return lista;
  }
    
    public void regravar(java.util.List<Contato> lista) throws IOException {
    java.io.BufferedWriter bw = new java.io.BufferedWriter(new java.io.FileWriter(ARQUIVO, false));

    for (Contato c : lista) {
        bw.write(c.toFileString());
        bw.newLine();
    }

    bw.close();
}
    
    public boolean excluir(String nome) throws IOException {
    java.util.List<Contato> lista = listar();
    boolean removido = false;

    java.util.Iterator<Contato> it = lista.iterator();

    while (it.hasNext()) {
        Contato c = it.next();

        if (c.getNome().equalsIgnoreCase(nome)) {
            it.remove();
            removido = true;
            break;
        }
    }

    if (removido) {
        regravar(lista);
    }

    return removido;
}    
    
}
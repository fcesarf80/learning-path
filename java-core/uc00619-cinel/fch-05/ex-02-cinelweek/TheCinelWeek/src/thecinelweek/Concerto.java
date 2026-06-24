package thecinelweek;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import javax.swing.JOptionPane;

public class Concerto {

    // 1. ATRIBUTOS
    String concertoCidade;
    String concertoData;
    float concertoPreco;
    int concertoTotal;
    float valorTotal;

    // 2. CONSTRUTOR COMPLETO
    public Concerto(String concertoCidade, String concertoData, float concertoPreco, int concertoTotal) {
        this.concertoCidade = concertoCidade;
        this.concertoData = concertoData;
        this.concertoPreco = concertoPreco;
        this.concertoTotal = concertoTotal;
        this.valorTotal = this.concertoPreco * this.concertoTotal;
    }

    // 3. CONSTRUTOR VAZIO (Importante se for instanciar sem passar dados logo no início)
    public Concerto() {
    }

    // 4. MÉTODO PARA GRAVAR NO FICHEIRO
    public void GuardarConcerto() {
        try (BufferedWriter escrever = new BufferedWriter(new FileWriter("dados/ficheiros/concertos.txt", true))) {

            String linha = this.concertoCidade + ";" +
                           this.concertoData + ";" +
                           this.concertoPreco + ";" +
                           this.concertoTotal + ";" +
                           this.valorTotal;

            escrever.write(linha);
            escrever.newLine();

            JOptionPane.showMessageDialog(null, "Concerto gravado com sucesso!", "Sucesso", JOptionPane.INFORMATION_MESSAGE);

        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Algo correu mal ao guardar no ficheiro!", "ERRO", JOptionPane.ERROR_MESSAGE);
        }
    }
    
} // <- Esta última chave fecha a classe Concerto.
      
import javax.swing.*;
import java.awt.*;
import java.io.*;

public class Ex06GestaoTurneJava extends JFrame {

    JTextField cidade = new JTextField();
    JTextField data = new JTextField();
    JTextField preco = new JTextField();
    JTextField vendidos = new JTextField();
    JTextArea lista = new JTextArea(15, 30);

    public Ex06GestaoTurneJava() {
        setTitle("Turne");
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new GridLayout(0, 1));

        add(new JLabel("Cidade"));
        add(cidade);

        add(new JLabel("Data"));
        add(data);

        add(new JLabel("Preco"));
        add(preco);

        add(new JLabel("Bilhetes vendidos"));
        add(vendidos);

        JButton guardar = new JButton("Guardar");
        JButton carregar = new JButton("Carregar");
        JButton limpar = new JButton("Limpar");

        add(guardar);
        add(carregar);
        add(limpar);

        add(new JScrollPane(lista));

        guardar.addActionListener(e -> guardar());
        carregar.addActionListener(e -> carregar());
        limpar.addActionListener(e -> lista.setText(""));

        carregar();

        setVisible(true);
    }

    void guardar() {
        try {
            FileWriter f = new FileWriter("concertos.txt", true);

            double p = Double.parseDouble(preco.getText());
            int v = Integer.parseInt(vendidos.getText());
            double total = p * v;

            f.write(cidade.getText() + " | " +
                    data.getText() + " | " +
                    preco.getText() + " | " +
                    vendidos.getText() + " | " +
                    total + "\n");

            f.close();

            carregar();

            cidade.setText("");
            data.setText("");
            preco.setText("");
            vendidos.setText("");

        } catch (Exception e) {
        }
    }

    void carregar() {
        try {
            lista.setText("");

            BufferedReader br = new BufferedReader(new FileReader("concertos.txt"));

            String linha;

            while ((linha = br.readLine()) != null) {
                lista.append(linha + "\n");
            }

            br.close();

        } catch (Exception e) {
        }
    }

    public static void main(String[] args) {
        new Ex06GestaoTurneJava();
    }
}



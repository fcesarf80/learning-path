package view;

import javax.swing.*;
import java.awt.*;

public class TelaFatura extends JFrame {

    public TelaFatura() {
        setTitle("Faturas");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JLabel lbl = new JLabel("Tela de Faturas (em construção)", SwingConstants.CENTER);
        add(lbl, BorderLayout.CENTER);

        JButton btnVoltar = new JButton("Voltar");
        add(btnVoltar, BorderLayout.SOUTH);

        btnVoltar.addActionListener(e -> {
            new TelaPrincipal().setVisible(true);
            dispose();
        });

        setVisible(true);
    }
}
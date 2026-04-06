package view;

import javax.swing.*;
import java.awt.*;

public class TelaCliente extends JFrame {

    private JButton btnVoltar;

    public TelaCliente() {
        setTitle("Gestão de Clientes");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        JLabel lblTitulo = new JLabel("TelaCliente funcionando", SwingConstants.CENTER);
        add(lblTitulo, BorderLayout.CENTER);

        btnVoltar = new JButton("Voltar");
        add(btnVoltar, BorderLayout.SOUTH);

        btnVoltar.addActionListener(e -> {
            new TelaPrincipal().setVisible(true);
            dispose();
        });

        setVisible(true);
    }
}
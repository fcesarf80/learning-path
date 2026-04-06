package view;

import javax.swing.*;
import java.awt.*;

public class TelaPrincipal extends JFrame {

    private JButton btnClientes;
    private JButton btnAnimais;
    private JButton btnFuncionarios;
    private JButton btnConsultas;
    private JButton btnFaturas;
    private JButton btnSair;

    public TelaPrincipal() {
        configurarJanela();
        criarComponentes();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("VetApp - Tela Principal");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new BorderLayout(10, 10));
    }

    private void criarComponentes() {

        // ===== TOPO =====
        JPanel pnlTopo = new JPanel();
        pnlTopo.setLayout(new BoxLayout(pnlTopo, BoxLayout.Y_AXIS));

        JLabel lblTitulo = new JLabel("VetApp", SwingConstants.CENTER);
        lblTitulo.setFont(new Font("Dialog", Font.BOLD, 18));
        lblTitulo.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel lblSubtitulo = new JLabel("Sistema de Gestão Veterinária", SwingConstants.CENTER);
        lblSubtitulo.setFont(new Font("Dialog", Font.PLAIN, 14));
        lblSubtitulo.setAlignmentX(Component.CENTER_ALIGNMENT);

        pnlTopo.add(Box.createVerticalStrut(10));
        pnlTopo.add(lblTitulo);
        pnlTopo.add(Box.createVerticalStrut(5));
        pnlTopo.add(lblSubtitulo);
        pnlTopo.add(Box.createVerticalStrut(10));

        // ===== CENTRO =====
        JPanel pnlMenu = new JPanel(new GridLayout(3, 2, 10, 10));
        pnlMenu.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));

        btnClientes = new JButton("Clientes");
        btnAnimais = new JButton("Animais");
        btnFuncionarios = new JButton("Funcionários");
        btnConsultas = new JButton("Consultas");
        btnFaturas = new JButton("Faturas");
        btnSair = new JButton("Sair");

        pnlMenu.add(btnClientes);
        pnlMenu.add(btnAnimais);
        pnlMenu.add(btnFuncionarios);
        pnlMenu.add(btnConsultas);
        pnlMenu.add(btnFaturas);
        pnlMenu.add(btnSair);

        // ===== RODAPÉ =====
        JLabel lblRodape = new JLabel("Bem-vindo ao sistema VetApp", SwingConstants.CENTER);

        add(pnlTopo, BorderLayout.NORTH);
        add(pnlMenu, BorderLayout.CENTER);
        add(lblRodape, BorderLayout.SOUTH);

        configurarEventos();
    }

   private void configurarEventos() {

    btnSair.addActionListener(e -> System.exit(0));

    btnClientes.addActionListener(e -> {
        new TelaCliente().setVisible(true);
        dispose();
    });
    
    btnAnimais.addActionListener(e -> {
    new TelaAnimal().setVisible(true);
    dispose();
});

btnFuncionarios.addActionListener(e -> {
    new TelaFuncionario().setVisible(true);
    dispose();
});

btnConsultas.addActionListener(e -> {
    new TelaConsulta().setVisible(true);
    dispose();
});

btnFaturas.addActionListener(e -> {
    new TelaFatura().setVisible(true);
    dispose();
});
}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TelaPrincipal::new);
    }
}
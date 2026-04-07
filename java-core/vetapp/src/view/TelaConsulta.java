package view;

import javax.swing.*;
import java.awt.*;

public class TelaConsulta extends JFrame {

    // Painéis
    private JPanel pnlDadosConsulta;
    private JPanel pnlAcoes;
    private JPanel pnlListagemConsultas;

    // Campos
    private JTextField txtId;
    private JTextField txtData;
    private JTextField txtHora;
    private JTextField txtAnimal;
    private JTextField txtTutor;
    private JTextField txtVeterinario;
    private JTextField txtObservacoes;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Tabela
    private JTable tblConsultas;

    // Peixe
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaConsulta() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Consultas");
        setSize(980, 680);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new BorderLayout(10, 10));
    }

    private void carregarImagens() {
        iconeSerio = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/peixe-serio.png");
        iconeFeliz = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/peixe-feliz.png");
    }

    private void criarComponentes() {
        criarPainelDadosConsulta();
        criarPainelAcoes();
        criarPainelListagem();

        add(pnlDadosConsulta, BorderLayout.NORTH);
        add(pnlAcoes, BorderLayout.CENTER);
        add(pnlListagemConsultas, BorderLayout.SOUTH);
    }

    private void criarPainelDadosConsulta() {
        pnlDadosConsulta = new JPanel(new BorderLayout(10, 10));
        pnlDadosConsulta.setBorder(BorderFactory.createTitledBorder("Dados da Consulta"));

        JPanel pnlForm = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel lblId = new JLabel("ID:");
        JLabel lblAuto = new JLabel("(auto)");
        JLabel lblData = new JLabel("Data:");
        JLabel lblHora = new JLabel("Hora:");
        JLabel lblAnimal = new JLabel("Animal:");
        JLabel lblTutor = new JLabel("Tutor:");
        JLabel lblVeterinario = new JLabel("Veterinário:");
        JLabel lblObservacoes = new JLabel("Observações:");

        txtId = new JTextField(10);
        txtId.setEditable(false);

        txtData = new JTextField(12);
        txtHora = new JTextField(10);
        txtAnimal = new JTextField(20);
        txtTutor = new JTextField(20);
        txtVeterinario = new JTextField(20);
        txtObservacoes = new JTextField(30);

        // linha 1
        gbc.gridx = 0; gbc.gridy = 0;
        pnlForm.add(lblId, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtId, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblAuto, gbc);

        // linha 2
        gbc.gridx = 0; gbc.gridy = 1;
        pnlForm.add(lblData, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtData, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblHora, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtHora, gbc);

        // linha 3
        gbc.gridx = 0; gbc.gridy = 2;
        pnlForm.add(lblAnimal, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtAnimal, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblTutor, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtTutor, gbc);

        // linha 4
        gbc.gridx = 0; gbc.gridy = 3;
        pnlForm.add(lblVeterinario, gbc);

        gbc.gridx = 1; gbc.gridwidth = 3;
        pnlForm.add(txtVeterinario, gbc);

        // linha 5
        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 1;
        pnlForm.add(lblObservacoes, gbc);

        gbc.gridx = 1; gbc.gridwidth = 3;
        pnlForm.add(txtObservacoes, gbc);

        JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        lblFotoAnimal = new JLabel();
        lblFotoAnimal.setIcon(iconeSerio);
        lblFotoAnimal.setPreferredSize(new Dimension(170, 260));
        pnlImagem.add(lblFotoAnimal);

        pnlDadosConsulta.add(pnlForm, BorderLayout.CENTER);
        pnlDadosConsulta.add(pnlImagem, BorderLayout.EAST);
    }

    private void criarPainelAcoes() {
        pnlAcoes = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 12));
        pnlAcoes.setBorder(BorderFactory.createTitledBorder("Ações"));

        btnNovo = new JButton("Novo");
        btnSalvar = new JButton("Salvar");
        btnBuscar = new JButton("Buscar");
        btnAtualizar = new JButton("Atualizar");
        btnExcluir = new JButton("Excluir");
        btnLimpar = new JButton("Limpar");
        btnVoltar = new JButton("Voltar");

        pnlAcoes.add(btnNovo);
        pnlAcoes.add(btnSalvar);
        pnlAcoes.add(btnBuscar);
        pnlAcoes.add(btnAtualizar);
        pnlAcoes.add(btnExcluir);
        pnlAcoes.add(btnLimpar);
        pnlAcoes.add(btnVoltar);
    }

    private void criarPainelListagem() {
        pnlListagemConsultas = new JPanel(new BorderLayout());
        pnlListagemConsultas.setBorder(BorderFactory.createTitledBorder("Listagem de Consultas"));
        pnlListagemConsultas.setPreferredSize(new Dimension(900, 240));

        String[] colunas = {"ID", "Data", "Hora", "Animal", "Tutor", "Veterinário"};
        Object[][] dados = {
            {1, "10/04/2026", "10:00", "Thor", "Ana Souza", "Mariana Costa"},
            {2, "11/04/2026", "14:30", "Luna", "Carlos Lima", "Mariana Costa"}
        };

        tblConsultas = new JTable(dados, colunas);
        JScrollPane scroll = new JScrollPane(tblConsultas);

        pnlListagemConsultas.add(scroll, BorderLayout.CENTER);
    }

    private void configurarEventos() {
        btnVoltar.addActionListener(e -> {
            new TelaPrincipal().setVisible(true);
            dispose();
        });

        btnLimpar.addActionListener(e -> limparCampos());

        btnNovo.addActionListener(e -> {
            limparCampos();
            alternarHumor(false);
        });

        btnSalvar.addActionListener(e -> {
            if (camposPreenchidos()) {
                JOptionPane.showMessageDialog(this, "Consulta salva com sucesso!");
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
            }
        });
    }

    private boolean camposPreenchidos() {
        return !txtData.getText().trim().isEmpty()
                && !txtHora.getText().trim().isEmpty()
                && !txtAnimal.getText().trim().isEmpty()
                && !txtTutor.getText().trim().isEmpty()
                && !txtVeterinario.getText().trim().isEmpty()
                && !txtObservacoes.getText().trim().isEmpty();
    }

    private void alternarHumor(boolean feliz) {
        lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);
    }

    private void limparCampos() {
        txtId.setText("");
        txtData.setText("");
        txtHora.setText("");
        txtAnimal.setText("");
        txtTutor.setText("");
        txtVeterinario.setText("");
        txtObservacoes.setText("");
        txtData.requestFocusInWindow();
    }
}
package view;

import javax.swing.*;
import java.awt.*;

public class TelaFuncionario extends JFrame {

    // Painéis
    private JPanel pnlDadosFuncionario;
    private JPanel pnlAcoes;
    private JPanel pnlListagemFuncionarios;

    // Campos
    private JTextField txtId;
    private JTextField txtNome;
    private JTextField txtCargo;
    private JFormattedTextField fmtTelefone;
    private JTextField txtEmail;
    private JTextField txtTurno;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Tabela
    private JTable tblFuncionarios;

    // Hamster
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaFuncionario() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Funcionários");
        setSize(980, 680);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new BorderLayout(10, 10));
    }

    private void carregarImagens() {
        iconeSerio = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/hamster-serio.png");
        iconeFeliz = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/hamster-feliz.png");
    }

    private void criarComponentes() {
        criarPainelDadosFuncionario();
        criarPainelAcoes();
        criarPainelListagem();

        add(pnlDadosFuncionario, BorderLayout.NORTH);
        add(pnlAcoes, BorderLayout.CENTER);
        add(pnlListagemFuncionarios, BorderLayout.SOUTH);
    }

    private void criarPainelDadosFuncionario() {
        pnlDadosFuncionario = new JPanel(new BorderLayout(10, 10));
        pnlDadosFuncionario.setBorder(BorderFactory.createTitledBorder("Dados do Funcionário"));

        JPanel pnlForm = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel lblId = new JLabel("ID:");
        JLabel lblAuto = new JLabel("(auto)");
        JLabel lblNome = new JLabel("Nome:");
        JLabel lblCargo = new JLabel("Cargo:");
        JLabel lblTelefone = new JLabel("Telefone:");
        JLabel lblEmail = new JLabel("E-mail:");
        JLabel lblTurno = new JLabel("Turno:");

        txtId = new JTextField(10);
        txtId.setEditable(false);

        txtNome = new JTextField(25);
        txtCargo = new JTextField(20);

        try {
            fmtTelefone = new JFormattedTextField(
                new javax.swing.text.MaskFormatter("(##) #####-####")
            );
            fmtTelefone.setColumns(14);
        } catch (java.text.ParseException e) {
            fmtTelefone = new JFormattedTextField();
            fmtTelefone.setColumns(14);
        }

        txtEmail = new JTextField(25);
        txtTurno = new JTextField(15);

        // linha 1
        gbc.gridx = 0; gbc.gridy = 0;
        pnlForm.add(lblId, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtId, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblAuto, gbc);

        // linha 2
        gbc.gridx = 0; gbc.gridy = 1;
        pnlForm.add(lblNome, gbc);

        gbc.gridx = 1; gbc.gridwidth = 2;
        pnlForm.add(txtNome, gbc);

        // linha 3
        gbc.gridx = 0; gbc.gridy = 2; gbc.gridwidth = 1;
        pnlForm.add(lblCargo, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtCargo, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblTurno, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtTurno, gbc);

        // linha 4
        gbc.gridx = 0; gbc.gridy = 3;
        pnlForm.add(lblTelefone, gbc);

        gbc.gridx = 1;
        pnlForm.add(fmtTelefone, gbc);

        // linha 5
        gbc.gridx = 0; gbc.gridy = 4;
        pnlForm.add(lblEmail, gbc);

        gbc.gridx = 1; gbc.gridwidth = 3;
        pnlForm.add(txtEmail, gbc);

        JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        lblFotoAnimal = new JLabel();
        lblFotoAnimal.setIcon(iconeSerio);
        lblFotoAnimal.setPreferredSize(new Dimension(170, 260));
        pnlImagem.add(lblFotoAnimal);

        pnlDadosFuncionario.add(pnlForm, BorderLayout.CENTER);
        pnlDadosFuncionario.add(pnlImagem, BorderLayout.EAST);
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
        pnlListagemFuncionarios = new JPanel(new BorderLayout());
        pnlListagemFuncionarios.setBorder(BorderFactory.createTitledBorder("Listagem de Funcionários"));
        pnlListagemFuncionarios.setPreferredSize(new Dimension(900, 240));

        String[] colunas = {"ID", "Nome", "Cargo", "Telefone", "E-mail", "Turno"};
        Object[][] dados = {
            {1, "Mariana Costa", "Veterinária", "(11) 98888-1111", "mariana@vetapp.com", "Manhã"},
            {2, "João Pedro", "Recepcionista", "(21) 97777-2222", "joao@vetapp.com", "Tarde"}
        };

        tblFuncionarios = new JTable(dados, colunas);
        JScrollPane scroll = new JScrollPane(tblFuncionarios);

        pnlListagemFuncionarios.add(scroll, BorderLayout.CENTER);
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
                JOptionPane.showMessageDialog(this, "Funcionário salvo com sucesso!");
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
            }
        });
    }

    private boolean camposPreenchidos() {
        return !txtNome.getText().trim().isEmpty()
                && !txtCargo.getText().trim().isEmpty()
                && !fmtTelefone.getText().trim().isEmpty()
                && !txtEmail.getText().trim().isEmpty()
                && !txtTurno.getText().trim().isEmpty();
    }

    private void alternarHumor(boolean feliz) {
        lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);
    }

    private void limparCampos() {
        txtId.setText("");
        txtNome.setText("");
        txtCargo.setText("");
        fmtTelefone.setValue(null);
        txtEmail.setText("");
        txtTurno.setText("");
        txtNome.requestFocusInWindow();
    }
}
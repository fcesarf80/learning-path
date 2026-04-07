package view;

import javax.swing.*;
import java.awt.*;

public class TelaCliente extends JFrame {

    // Painéis
    private JPanel pnlDadosCliente;
    private JPanel pnlAcoes;
    private JPanel pnlListagemClientes;

    // Campos
    private JTextField txtId;
    private JTextField txtNome;
    private JFormattedTextField fmtTelefone;
    private JTextField txtEmail;
    private JTextField txtEndereco;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Tabela
    private JTable tblClientes;

    // Bulldog
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaCliente() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Clientes");
        setSize(720, 520);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
    }

    private void carregarImagens() {
        iconeSerio = carregarIconeRedimensionado(
            "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/bulldog-serio.png",
            110, 160
        );

        iconeFeliz = carregarIconeRedimensionado(
            "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/bulldog-feliz.png",
            110, 160
        );
    }

    private ImageIcon carregarIconeRedimensionado(String caminho, int largura, int altura) {
        ImageIcon iconeOriginal = new ImageIcon(caminho);
        Image imagemRedimensionada = iconeOriginal.getImage().getScaledInstance(
            largura, altura, Image.SCALE_SMOOTH
        );
        return new ImageIcon(imagemRedimensionada);
    }

    private void criarComponentes() {
    criarPainelDadosCliente();
    criarPainelAcoes();
    criarPainelListagem();

    JPanel pnlPrincipal = new JPanel();
    pnlPrincipal.setLayout(new BoxLayout(pnlPrincipal, BoxLayout.Y_AXIS));

    pnlDadosCliente.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlAcoes.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlListagemClientes.setAlignmentX(Component.CENTER_ALIGNMENT);

    pnlPrincipal.add(pnlDadosCliente);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlAcoes);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlListagemClientes);

    add(pnlPrincipal);
}

    private void criarPainelDadosCliente() {
    pnlDadosCliente = new JPanel(new BorderLayout(10, 10));
    pnlDadosCliente.setBorder(BorderFactory.createTitledBorder("Dados do Cliente"));
    pnlDadosCliente.setPreferredSize(new Dimension(680, 230));

    JPanel pnlForm = new JPanel(new GridBagLayout());
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(5, 5, 5, 5);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.fill = GridBagConstraints.NONE;

    JLabel lblId = new JLabel("ID:");
    JLabel lblAuto = new JLabel("(auto)");
    JLabel lblNome = new JLabel("Nome:");
    JLabel lblTelefone = new JLabel("Telefone:");
    JLabel lblEmail = new JLabel("E-mail:");
    JLabel lblEndereco = new JLabel("Endereço:");

    txtId = new JTextField(6);
    txtId.setEditable(false);
    txtId.setPreferredSize(new Dimension(60, 25));

    txtNome = new JTextField(18);
    txtNome.setPreferredSize(new Dimension(180, 25));

    try {
        fmtTelefone = new JFormattedTextField(
            new javax.swing.text.MaskFormatter("(##) #####-####")
        );
    } catch (java.text.ParseException e) {
        fmtTelefone = new JFormattedTextField();
    }

    fmtTelefone.setColumns(12);
    fmtTelefone.setPreferredSize(new Dimension(120, 25));

    txtEmail = new JTextField(18);
    txtEmail.setPreferredSize(new Dimension(180, 25));

    txtEndereco = new JTextField(18);
    txtEndereco.setPreferredSize(new Dimension(180, 25));

    // linha 1
    gbc.gridx = 0;
    gbc.gridy = 0;
    gbc.gridwidth = 1;
    pnlForm.add(lblId, gbc);

    gbc.gridx = 1;
    pnlForm.add(txtId, gbc);

    gbc.gridx = 2;
    pnlForm.add(lblAuto, gbc);

    // linha 2
    gbc.gridx = 0;
    gbc.gridy = 1;
    gbc.gridwidth = 1;
    pnlForm.add(lblNome, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtNome, gbc);

    // linha 3
    gbc.gridx = 0;
    gbc.gridy = 2;
    gbc.gridwidth = 1;
    pnlForm.add(lblTelefone, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 1;
    pnlForm.add(fmtTelefone, gbc);

    // linha 4
    gbc.gridx = 0;
    gbc.gridy = 3;
    gbc.gridwidth = 1;
    pnlForm.add(lblEmail, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtEmail, gbc);

    // linha 5
    gbc.gridx = 0;
    gbc.gridy = 4;
    gbc.gridwidth = 1;
    pnlForm.add(lblEndereco, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtEndereco, gbc);

    JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
    lblFotoAnimal = new JLabel();
    lblFotoAnimal.setIcon(iconeSerio);
    lblFotoAnimal.setPreferredSize(new Dimension(110, 160));
    pnlImagem.add(lblFotoAnimal);

    pnlDadosCliente.add(pnlForm, BorderLayout.CENTER);
    pnlDadosCliente.add(pnlImagem, BorderLayout.EAST);
}

    private void criarPainelAcoes() {
        pnlAcoes = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 12));
        pnlAcoes.setBorder(BorderFactory.createTitledBorder("Ações"));
        pnlAcoes.setPreferredSize(new Dimension(680, 80));

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
        pnlListagemClientes = new JPanel(new BorderLayout());
        pnlListagemClientes.setBorder(BorderFactory.createTitledBorder("Listagem de Clientes"));
        pnlListagemClientes.setPreferredSize(new Dimension(680, 150));

        String[] colunas = {"ID", "Nome", "Telefone", "E-mail", "Endereço"};
        Object[][] dados = {
            {1, "Ana Souza", "(11) 99999-1111", "ana@email.com", "Rua A, 100"},
            {2, "Carlos Lima", "(21) 98888-2222", "carlos@email.com", "Av. Central, 250"}
        };

        tblClientes = new JTable(dados, colunas);
        JScrollPane scroll = new JScrollPane(tblClientes);

        pnlListagemClientes.add(scroll, BorderLayout.CENTER);
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
                JOptionPane.showMessageDialog(this, "Cliente salvo com sucesso!");
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
            }
        });
    }

    private boolean camposPreenchidos() {
        return !txtNome.getText().trim().isEmpty()
                && !fmtTelefone.getText().trim().isEmpty()
                && !txtEmail.getText().trim().isEmpty()
                && !txtEndereco.getText().trim().isEmpty();
    }

    private void alternarHumor(boolean feliz) {
        lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);
    }

    private void limparCampos() {
        txtId.setText("");
        txtNome.setText("");
        fmtTelefone.setValue(null);
        txtEmail.setText("");
        txtEndereco.setText("");
        txtNome.requestFocusInWindow();
    }
}
package view;

import javax.swing.*;
import java.awt.*;

public class TelaFuncionario extends JFrame {

    // Painéis
    private JPanel pnlDadosFuncionario;
    private JPanel pnlAcoes;
    private JPanel pnlListagemFuncionarios;
    private JTable tblFuncionarios;

    // Campos
    private JTextField txtId;
    private JTextField txtNome;
    private JTextField txtCargo;
    private JFormattedTextField fmtTelefone;
    private JTextField txtEmail;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Hamster
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaFuncionario() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        SwingUtilities.invokeLater(() -> txtNome.requestFocusInWindow());
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Funcionários");
        setSize(720, 520);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
    }

    private void carregarImagens() {
    iconeSerio = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/hamster-serio.png",
        110, 160
    );

    iconeFeliz = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/hamster-feliz.png",
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
    criarPainelDadosFuncionario();
    criarPainelAcoes();
    criarPainelListagem();

    JPanel pnlPrincipal = new JPanel();
    pnlPrincipal.setLayout(new BoxLayout(pnlPrincipal, BoxLayout.Y_AXIS));

    pnlDadosFuncionario.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlAcoes.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlListagemFuncionarios.setAlignmentX(Component.CENTER_ALIGNMENT);

    pnlPrincipal.add(pnlDadosFuncionario);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlAcoes);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlListagemFuncionarios);

    add(pnlPrincipal);
}

    private void criarPainelDadosFuncionario(){
    pnlDadosFuncionario = new JPanel(new BorderLayout(10, 10));
    pnlDadosFuncionario.setBorder(BorderFactory.createTitledBorder("Dados do Funcionário"));
    pnlDadosFuncionario.setPreferredSize(new Dimension(680, 230));

    JPanel pnlForm = new JPanel(new GridBagLayout());
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(5, 5, 5, 5);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.fill = GridBagConstraints.NONE;

    JLabel lblId = new JLabel("ID:");
    JLabel lblAuto = new JLabel("(auto)");
    JLabel lblNome = new JLabel("Nome:");
    JLabel lblCargo = new JLabel("Cargo:");
    JLabel lblTelefone = new JLabel("Telefone:");
    JLabel lblEmail = new JLabel("E-mail:");

    txtNome = new JTextField(18);
    txtNome.setPreferredSize(new Dimension(180, 25));

    txtCargo = new JTextField(18);
    txtCargo.setPreferredSize(new Dimension(180, 25));

    txtId = new JTextField(6);
    txtId.setEditable(false);
    txtId.setFocusable(false);
    txtId.setPreferredSize(new Dimension(60, 25));
    
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
    pnlForm.add(lblCargo, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtCargo, gbc);

    // linha 4
    gbc.gridx = 0;
    gbc.gridy = 3;
    gbc.gridwidth = 1;
    pnlForm.add(lblTelefone, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 1;
    pnlForm.add(fmtTelefone, gbc);

    // linha 5
    gbc.gridx = 0;
    gbc.gridy = 4;
    gbc.gridwidth = 1;
    pnlForm.add(lblEmail, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtEmail, gbc);
    JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
    lblFotoAnimal = new JLabel();
    lblFotoAnimal.setIcon(iconeSerio);
    lblFotoAnimal.setPreferredSize(new Dimension(110, 160));
    pnlImagem.add(lblFotoAnimal);

    pnlDadosCliente.add(pnlForm, BorderLayout.CENTER);
    pnlDadosCliente.add(pnlImagem, BorderLayout.EAST);
    
    lblFotoAnimal.setFocusable(false);
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
        
        estilizarBotoes();
    }

    private void criarPainelListagem() {
        pnlListagemFuncionarios = new JPanel(new BorderLayout());
    pnlListagemFuncionarios.setBorder(BorderFactory.createTitledBorder("Listagem de Funcionários"));
    pnlListagemFuncionarios.setPreferredSize(new Dimension(680, 150));

        String[] colunas ={"ID", "Nome", "Cargo", "Telefone", "E-mail"};
        Object[][] dados = {
    {1, "Marcos Silva", "Recepcionista", "(11) 99999-1111", "marcos@email.com"},
    {2, "Luciana Costa", "Veterinária", "(21) 98888-2222", "luciana@email.com"}
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
                && !fmtTelefone.getText().trim().isEmpty()
                && !txtEmail.getText().trim().isEmpty()
                && !txtCargo.getText().trim().isEmpty();
    }

    private void limparCampos() {
        txtId.setText("");
        txtNome.setText("");
        txtCargo.setText("");
        fmtTelefone.setValue(null);
        txtEmail.setText("");
        txtNome.requestFocusInWindow();
    }
    
   private void estilizarBotoes() {
    btnNovo.setBackground(new Color(102, 255, 255));
    btnSalvar.setBackground(new Color(102, 255, 102));
    btnBuscar.setBackground(new Color(102, 153, 255));
    btnAtualizar.setBackground(new Color(255, 153, 51));
    btnExcluir.setBackground(Color.RED);
    btnLimpar.setBackground(Color.LIGHT_GRAY);
    btnVoltar.setBackground(new Color(255, 204, 51));

    JButton[] botoes = {
        btnNovo, btnSalvar, btnBuscar, btnAtualizar,
        btnExcluir, btnLimpar, btnVoltar
    };

    for (JButton botao : botoes) {
        botao.setFocusPainted(false);
        botao.setFocusable(false); 
    }
}
    
    private void alternarHumor(boolean feliz) {
    lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);

    if (feliz) {
        Timer timer = new Timer(4000, e -> lblFotoAnimal.setIcon(iconeSerio));
        timer.setRepeats(false);
        timer.start();
    }
    
}
    
}
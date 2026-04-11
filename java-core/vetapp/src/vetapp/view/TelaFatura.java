package vetapp.view;

import javax.swing.*;
import java.awt.*;

public class TelaFatura extends JFrame {

    // Painéis
    private JPanel pnlAcoes;
    private JPanel pnlListagemFaturas;
    private JPanel pnlDadosFatura;
    
    // Painéis
    private JTable tblFaturas;

    // Campos
    private JTextField txtId;
    private JTextField txtCliente;
    private JTextField txtServico;
    private JTextField txtValor;
    private JTextField txtData;
    private JTextField txtStatus;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Gato
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaFatura() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        SwingUtilities.invokeLater(() -> txtCliente.requestFocusInWindow());
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Faturas");
        setSize(720, 520);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
    }

    private void carregarImagens() {
    iconeSerio = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/gato-serio.png",
        110, 160
    );

    iconeFeliz = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/gato-feliz.png",
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
    private void criarPainelDadosFatura() {
    pnlDadosFatura = new JPanel(new BorderLayout(10, 10));
    pnlDadosFatura.setBorder(BorderFactory.createTitledBorder("Dados da Fatura"));
    pnlDadosFatura.setPreferredSize(new Dimension(680, 260));

    JPanel pnlForm = new JPanel(new GridBagLayout());
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(5, 5, 5, 5);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.fill = GridBagConstraints.NONE;

    JLabel lblId = new JLabel("ID:");
    JLabel lblAuto = new JLabel("(auto)");
    JLabel lblCliente = new JLabel("Cliente:");
    JLabel lblServico = new JLabel("Serviço:");
    JLabel lblValor = new JLabel("Valor:");
    JLabel lblData = new JLabel("Data:");
    JLabel lblStatus = new JLabel("Status:");

    txtId = new JTextField(6);
    txtId.setEditable(false);
    txtId.setFocusable(false);
    txtId.setPreferredSize(new Dimension(60, 25));

    txtCliente = new JTextField(18);
    txtCliente.setPreferredSize(new Dimension(180, 25));

    txtServico = new JTextField(18);
    txtServico.setPreferredSize(new Dimension(180, 25));

    txtValor = new JTextField(18);
    txtValor.setPreferredSize(new Dimension(180, 25));

    txtData = new JTextField(18);
    txtData.setPreferredSize(new Dimension(180, 25));

    txtStatus = new JTextField(18);
    txtStatus.setPreferredSize(new Dimension(180, 25));

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
    pnlForm.add(lblCliente, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtCliente, gbc);

    // linha 3
    gbc.gridx = 0;
    gbc.gridy = 2;
    gbc.gridwidth = 1;
    pnlForm.add(lblServico, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtServico, gbc);

    // linha 4
    gbc.gridx = 0;
    gbc.gridy = 3;
    gbc.gridwidth = 1;
    pnlForm.add(lblValor, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtValor, gbc);

    // linha 5
    gbc.gridx = 0;
    gbc.gridy = 4;
    gbc.gridwidth = 1;
    pnlForm.add(lblData, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtData, gbc);

    // linha 6
    gbc.gridx = 0;
    gbc.gridy = 5;
    gbc.gridwidth = 1;
    pnlForm.add(lblStatus, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtStatus, gbc);

    JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
    lblFotoAnimal = new JLabel();
    lblFotoAnimal.setIcon(iconeSerio);
    lblFotoAnimal.setPreferredSize(new Dimension(110, 160));
    lblFotoAnimal.setFocusable(false);
    pnlImagem.add(lblFotoAnimal);

    pnlDadosFatura.add(pnlForm, BorderLayout.CENTER);
    pnlDadosFatura.add(pnlImagem, BorderLayout.EAST);
}
    
    private boolean camposPreenchidos() {
    return !txtCliente.getText().trim().isEmpty()
            && !txtServico.getText().trim().isEmpty()
            && !txtValor.getText().trim().isEmpty()
            && !txtData.getText().trim().isEmpty()
            && !txtStatus.getText().trim().isEmpty();
}
    
    private void criarComponentes() {
    criarPainelDadosFatura();
    criarPainelAcoes();
    criarPainelListagem();

    JPanel pnlPrincipal = new JPanel();
    pnlPrincipal.setLayout(new BoxLayout(pnlPrincipal, BoxLayout.Y_AXIS));

    pnlDadosFatura.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlAcoes.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlListagemFaturas.setAlignmentX(Component.CENTER_ALIGNMENT);

    pnlPrincipal.add(pnlDadosFatura);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlAcoes);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlListagemFaturas);

    add(pnlPrincipal);
}

    private void criarPainelListagem() {
    pnlListagemFaturas = new JPanel(new BorderLayout());
    pnlListagemFaturas.setBorder(BorderFactory.createTitledBorder("Listagem de Faturas"));
    pnlListagemFaturas.setPreferredSize(new Dimension(680, 150));

    String[] colunas = {"ID", "Cliente", "Serviço", "Valor", "Status"};
    Object[][] dados = {
        {1, "Ana Souza", "Consulta", "80,00 €", "Paga"},
        {2, "Carlos Lima", "Vacinação", "45,00 €", "Pendente"}
    };

    tblFaturas = new JTable(dados, colunas);
    JScrollPane scroll = new JScrollPane(tblFaturas);

    pnlListagemFaturas.add(scroll, BorderLayout.CENTER);
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
                JOptionPane.showMessageDialog(this, "Fatura salva com sucesso!");
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
            }
        });
    }

    private void limparCampos() {
    txtId.setText("");
    txtCliente.setText("");
    txtServico.setText("");
    txtValor.setText("");
    txtData.setText("");
    txtStatus.setText("");
    txtCliente.requestFocusInWindow();
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

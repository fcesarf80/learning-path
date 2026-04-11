package vetapp.view;

import javax.swing.*;
import java.awt.*;

public class TelaConsulta extends JFrame {

    // Painéis
    private JPanel pnlDadosConsulta;
    private JPanel pnlAcoes;
    private JPanel pnlListagemConsultas;

    // Tabela
    private JTable tblConsultas;

    // Campos
    private JTextField txtId;
    private JTextField txtData;
    private JTextField txtHora;
    private JTextField txtAnimal;
    private JTextField txtVeterinario;
    private JTextField txtObservacao;
    
    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Peixe
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaConsulta() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        SwingUtilities.invokeLater(() -> txtData.requestFocusInWindow());
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Consultas");
        setSize(720, 520);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
    }

    private void carregarImagens() {
    iconeSerio = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/peixe-serio.png",
        110, 160
    );

    iconeFeliz = carregarIconeRedimensionado(
        "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/peixe-feliz.png",
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
    criarPainelDadosConsulta();
    criarPainelAcoes();
    criarPainelListagem();

    JPanel pnlPrincipal = new JPanel();
    pnlPrincipal.setLayout(new BoxLayout(pnlPrincipal, BoxLayout.Y_AXIS));

    pnlDadosConsulta.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlAcoes.setAlignmentX(Component.CENTER_ALIGNMENT);
    pnlListagemConsultas.setAlignmentX(Component.CENTER_ALIGNMENT);

    pnlPrincipal.add(pnlDadosConsulta);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlAcoes);
    pnlPrincipal.add(Box.createVerticalStrut(8));
    pnlPrincipal.add(pnlListagemConsultas);

    add(pnlPrincipal);
}
    private void criarPainelDadosConsulta() {
    pnlDadosConsulta = new JPanel(new BorderLayout(10, 10));
    pnlDadosConsulta.setBorder(BorderFactory.createTitledBorder("Dados da Consulta"));
    pnlDadosConsulta.setPreferredSize(new Dimension(680, 260));

    JPanel pnlForm = new JPanel(new GridBagLayout());
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.insets = new Insets(5, 5, 5, 5);
    gbc.anchor = GridBagConstraints.WEST;
    gbc.fill = GridBagConstraints.NONE;

    JLabel lblId = new JLabel("ID:");
    JLabel lblAuto = new JLabel("(auto)");
    JLabel lblData = new JLabel("Data:");
    JLabel lblHora = new JLabel("Hora:");
    JLabel lblAnimal = new JLabel("Animal:");
    JLabel lblVeterinario = new JLabel("Veterinário:");
    JLabel lblObservacao = new JLabel("Observação:");

    txtId = new JTextField(6);
    txtId.setEditable(false);
    txtId.setFocusable(false);
    txtId.setPreferredSize(new Dimension(60, 25));

    txtData = new JTextField(18);
    txtData.setPreferredSize(new Dimension(180, 25));

    txtHora = new JTextField(18);
    txtHora.setPreferredSize(new Dimension(180, 25));

    txtAnimal = new JTextField(18);
    txtAnimal.setPreferredSize(new Dimension(180, 25));

    txtVeterinario = new JTextField(18);
    txtVeterinario.setPreferredSize(new Dimension(180, 25));

    txtObservacao = new JTextField(18);
    txtObservacao.setPreferredSize(new Dimension(180, 25));

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
    pnlForm.add(lblData, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtData, gbc);

    // linha 3
    gbc.gridx = 0;
    gbc.gridy = 2;
    gbc.gridwidth = 1;
    pnlForm.add(lblHora, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtHora, gbc);

    // linha 4
    gbc.gridx = 0;
    gbc.gridy = 3;
    gbc.gridwidth = 1;
    pnlForm.add(lblAnimal, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtAnimal, gbc);

    // linha 5
    gbc.gridx = 0;
    gbc.gridy = 4;
    gbc.gridwidth = 1;
    pnlForm.add(lblVeterinario, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtVeterinario, gbc);

    // linha 6
    gbc.gridx = 0;
    gbc.gridy = 5;
    gbc.gridwidth = 1;
    pnlForm.add(lblObservacao, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    pnlForm.add(txtObservacao, gbc);

    JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
    lblFotoAnimal = new JLabel();
    lblFotoAnimal.setIcon(iconeSerio);
    lblFotoAnimal.setPreferredSize(new Dimension(110, 160));
    lblFotoAnimal.setFocusable(false);
    pnlImagem.add(lblFotoAnimal);

    pnlDadosConsulta.add(pnlForm, BorderLayout.CENTER);
    pnlDadosConsulta.add(pnlImagem, BorderLayout.EAST);
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
    pnlListagemConsultas = new JPanel(new BorderLayout());
    pnlListagemConsultas.setBorder(BorderFactory.createTitledBorder("Listagem de Consultas"));
    pnlListagemConsultas.setPreferredSize(new Dimension(680, 150));

    String[] colunas = {"ID", "Data", "Hora", "Animal", "Veterinário"};
    Object[][] dados = {
        {1, "10/04/2026", "09:00", "Rex", "Dr. Marcos"},
        {2, "11/04/2026", "14:30", "Mimi", "Dra. Luciana"}
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
            && !txtVeterinario.getText().trim().isEmpty()
            && !txtObservacao.getText().trim().isEmpty();
    }

    private void limparCampos() {
    txtId.setText("");
    txtData.setText("");
    txtHora.setText("");
    txtAnimal.setText("");
    txtVeterinario.setText("");
    txtObservacao.setText("");
    txtData.requestFocusInWindow();
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

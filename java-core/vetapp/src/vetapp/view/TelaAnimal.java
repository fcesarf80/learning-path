package vetapp.view;

import javax.swing.*;
import java.awt.*;

public class TelaAnimal extends JFrame {

    // Painéis
    private JPanel pnlDadosAnimal;
    private JPanel pnlAcoes;
    private JPanel pnlListagemAnimais;

    // Tabela
    private JTable tblAnimais;

    // Campos
    private JTextField txtId;
    private JTextField txtNomeAnimal;
    private JTextField txtEspecie;
    private JTextField txtRaca;
    private JTextField txtIdade;
    private JTextField txtTutor;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Camaleão
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaAnimal() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        SwingUtilities.invokeLater(() -> txtNomeAnimal.requestFocusInWindow());
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Animais");
        setSize(720, 520);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));
    }

    private void carregarImagens() {
        iconeSerio = carregarIconeRedimensionado(
            "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/camaleao-serio.png",
            110, 160
        );

        iconeFeliz = carregarIconeRedimensionado(
            "C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/camaleao-feliz.png",
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
        criarPainelDadosAnimal();
        criarPainelAcoes();
        criarPainelListagem();

        JPanel pnlPrincipal = new JPanel();
        pnlPrincipal.setLayout(new BoxLayout(pnlPrincipal, BoxLayout.Y_AXIS));

        pnlDadosAnimal.setAlignmentX(Component.CENTER_ALIGNMENT);
        pnlAcoes.setAlignmentX(Component.CENTER_ALIGNMENT);
        pnlListagemAnimais.setAlignmentX(Component.CENTER_ALIGNMENT);

        pnlPrincipal.add(pnlDadosAnimal);
        pnlPrincipal.add(Box.createVerticalStrut(8));
        pnlPrincipal.add(pnlAcoes);
        pnlPrincipal.add(Box.createVerticalStrut(8));
        pnlPrincipal.add(pnlListagemAnimais);

        add(pnlPrincipal);
    }

    private void criarPainelDadosAnimal() {
        pnlDadosAnimal = new JPanel(new BorderLayout(10, 10));
        pnlDadosAnimal.setBorder(BorderFactory.createTitledBorder("Dados do Animal"));
        pnlDadosAnimal.setPreferredSize(new Dimension(680, 260));

        JPanel pnlForm = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.NONE;

        JLabel lblId = new JLabel("ID:");
        JLabel lblAuto = new JLabel("(auto)");
        JLabel lblNomeAnimal = new JLabel("Nome:");
        JLabel lblEspecie = new JLabel("Espécie:");
        JLabel lblRaca = new JLabel("Raça:");
        JLabel lblIdade = new JLabel("Idade:");
        JLabel lblTutor = new JLabel("Tutor:");

        txtId = new JTextField(6);
        txtId.setEditable(false);
        txtId.setFocusable(false);
        txtId.setPreferredSize(new Dimension(60, 25));

        txtNomeAnimal = new JTextField(18);
        txtNomeAnimal.setPreferredSize(new Dimension(180, 25));

        txtEspecie = new JTextField(18);
        txtEspecie.setPreferredSize(new Dimension(180, 25));

        txtRaca = new JTextField(18);
        txtRaca.setPreferredSize(new Dimension(180, 25));

        txtIdade = new JTextField(18);
        txtIdade.setPreferredSize(new Dimension(180, 25));

        txtTutor = new JTextField(18);
        txtTutor.setPreferredSize(new Dimension(180, 25));

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
        pnlForm.add(lblNomeAnimal, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtNomeAnimal, gbc);

        // linha 3
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        pnlForm.add(lblEspecie, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtEspecie, gbc);

        // linha 4
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 1;
        pnlForm.add(lblRaca, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtRaca, gbc);

        // linha 5
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.gridwidth = 1;
        pnlForm.add(lblIdade, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtIdade, gbc);

        // linha 6
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 1;
        pnlForm.add(lblTutor, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtTutor, gbc);

        JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 5));
        lblFotoAnimal = new JLabel();
        lblFotoAnimal.setIcon(iconeSerio);
        lblFotoAnimal.setPreferredSize(new Dimension(110, 160));
        lblFotoAnimal.setFocusable(false);
        pnlImagem.add(lblFotoAnimal);

        pnlDadosAnimal.add(pnlForm, BorderLayout.CENTER);
        pnlDadosAnimal.add(pnlImagem, BorderLayout.EAST);
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
        pnlListagemAnimais = new JPanel(new BorderLayout());
        pnlListagemAnimais.setBorder(BorderFactory.createTitledBorder("Listagem de Animais"));
        pnlListagemAnimais.setPreferredSize(new Dimension(680, 150));

        String[] colunas = {"ID", "Nome", "Espécie", "Raça", "Tutor"};
        Object[][] dados = {
            {1, "Rex", "Cachorro", "Bulldog Francês", "Ana Souza"},
            {2, "Mimi", "Gato", "Siamês", "Carlos Lima"}
        };

        tblAnimais = new JTable(dados, colunas);
        JScrollPane scroll = new JScrollPane(tblAnimais);

        pnlListagemAnimais.add(scroll, BorderLayout.CENTER);
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
                JOptionPane.showMessageDialog(this, "Animal salvo com sucesso!");
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
            }
        });
    }

    private boolean camposPreenchidos() {
        return !txtNomeAnimal.getText().trim().isEmpty()
                && !txtEspecie.getText().trim().isEmpty()
                && !txtRaca.getText().trim().isEmpty()
                && !txtIdade.getText().trim().isEmpty()
                && !txtTutor.getText().trim().isEmpty();
    }

    private void limparCampos() {
        txtId.setText("");
        txtNomeAnimal.setText("");
        txtEspecie.setText("");
        txtRaca.setText("");
        txtIdade.setText("");
        txtTutor.setText("");
        txtNomeAnimal.requestFocusInWindow();
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
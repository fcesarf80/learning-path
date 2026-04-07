package view;

import javax.swing.*;
import java.awt.*;

public class TelaAnimal extends JFrame {

    // Painéis
    private JPanel pnlDadosAnimal;
    private JPanel pnlAcoes;
    private JPanel pnlListagemAnimais;

    // Campos
    private JTextField txtId;
    private JTextField txtNomeAnimal;
    private JTextField txtEspecie;
    private JTextField txtRaca;
    private JTextField txtIdade;
    private JTextField txtPeso;
    private JTextField txtTutor;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Tabela
    private JTable tblAnimais;

    // Camaleão
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaAnimal() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Animais");
        setSize(980, 680);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new BorderLayout(10, 10));
    }

    private void carregarImagens() {
        iconeSerio = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/camaleao-serio.png");
        iconeFeliz = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/camaleao-feliz.png");
    }

    private void criarComponentes() {
        criarPainelDadosAnimal();
        criarPainelAcoes();
        criarPainelListagem();

        add(pnlDadosAnimal, BorderLayout.NORTH);
        add(pnlAcoes, BorderLayout.CENTER);
        add(pnlListagemAnimais, BorderLayout.SOUTH);
    }

    private void criarPainelDadosAnimal() {
        pnlDadosAnimal = new JPanel(new BorderLayout(10, 10));
        pnlDadosAnimal.setBorder(BorderFactory.createTitledBorder("Dados do Animal"));

        JPanel pnlForm = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel lblId = new JLabel("ID:");
        JLabel lblAuto = new JLabel("(auto)");
        JLabel lblNomeAnimal = new JLabel("Nome do Animal:");
        JLabel lblEspecie = new JLabel("Espécie:");
        JLabel lblRaca = new JLabel("Raça:");
        JLabel lblIdade = new JLabel("Idade:");
        JLabel lblPeso = new JLabel("Peso:");
        JLabel lblTutor = new JLabel("Tutor:");

        txtId = new JTextField(10);
        txtId.setEditable(false);

        txtNomeAnimal = new JTextField(25);
        txtEspecie = new JTextField(20);
        txtRaca = new JTextField(20);
        txtIdade = new JTextField(10);
        txtPeso = new JTextField(10);
        txtTutor = new JTextField(25);

        // linha 1
        gbc.gridx = 0; gbc.gridy = 0;
        pnlForm.add(lblId, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtId, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblAuto, gbc);

        // linha 2
        gbc.gridx = 0; gbc.gridy = 1;
        pnlForm.add(lblNomeAnimal, gbc);

        gbc.gridx = 1; gbc.gridwidth = 2;
        pnlForm.add(txtNomeAnimal, gbc);

        // linha 3
        gbc.gridx = 0; gbc.gridy = 2; gbc.gridwidth = 1;
        pnlForm.add(lblEspecie, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtEspecie, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblRaca, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtRaca, gbc);

        // linha 4
        gbc.gridx = 0; gbc.gridy = 3;
        pnlForm.add(lblIdade, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtIdade, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblPeso, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtPeso, gbc);

        // linha 5
        gbc.gridx = 0; gbc.gridy = 4;
        pnlForm.add(lblTutor, gbc);

        gbc.gridx = 1; gbc.gridwidth = 3;
        pnlForm.add(txtTutor, gbc);

        JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        lblFotoAnimal = new JLabel();
        lblFotoAnimal.setIcon(iconeSerio);
        lblFotoAnimal.setPreferredSize(new Dimension(170, 260));
        pnlImagem.add(lblFotoAnimal);

        pnlDadosAnimal.add(pnlForm, BorderLayout.CENTER);
        pnlDadosAnimal.add(pnlImagem, BorderLayout.EAST);
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
        pnlListagemAnimais = new JPanel(new BorderLayout());
        pnlListagemAnimais.setBorder(BorderFactory.createTitledBorder("Listagem de Animais"));
        pnlListagemAnimais.setPreferredSize(new Dimension(900, 240));

        String[] colunas = {"ID", "Nome", "Espécie", "Raça", "Idade", "Peso", "Tutor"};
        Object[][] dados = {
            {1, "Thor", "Cachorro", "Bulldog Francês", "3", "12 kg", "Ana Souza"},
            {2, "Luna", "Gato", "Siamês", "2", "4 kg", "Carlos Lima"}
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
                && !txtPeso.getText().trim().isEmpty()
                && !txtTutor.getText().trim().isEmpty();
    }

    private void alternarHumor(boolean feliz) {
        lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);
    }

    private void limparCampos() {
        txtId.setText("");
        txtNomeAnimal.setText("");
        txtEspecie.setText("");
        txtRaca.setText("");
        txtIdade.setText("");
        txtPeso.setText("");
        txtTutor.setText("");
        txtNomeAnimal.requestFocusInWindow();
    }
}
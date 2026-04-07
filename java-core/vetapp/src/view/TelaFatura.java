package view;

import javax.swing.*;
import java.awt.*;

public class TelaFatura extends JFrame {

    // Painéis
    private JPanel pnlDadosFatura;
    private JPanel pnlAcoes;
    private JPanel pnlListagemFaturas;

    // Campos
    private JTextField txtId;
    private JTextField txtData;
    private JTextField txtCliente;
    private JTextField txtServico;
    private JTextField txtValor;
    private JTextField txtFormaPagamento;
    private JTextField txtStatus;

    // Botões
    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    // Tabela
    private JTable tblFaturas;

    // Gato
    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaFatura() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        configurarEventos();
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Faturas");
        setSize(980, 680);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(new BorderLayout(10, 10));
    }

    private void carregarImagens() {
        iconeSerio = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/gato-serio.png");
        iconeFeliz = new ImageIcon("C:/Users/fcesa/Documents/learning-path/java-core/vetapp/src/img/gato-feliz.png");
    }

    private void criarComponentes() {
        criarPainelDadosFatura();
        criarPainelAcoes();
        criarPainelListagem();

        add(pnlDadosFatura, BorderLayout.NORTH);
        add(pnlAcoes, BorderLayout.CENTER);
        add(pnlListagemFaturas, BorderLayout.SOUTH);
    }

    private void criarPainelDadosFatura() {
        pnlDadosFatura = new JPanel(new BorderLayout(10, 10));
        pnlDadosFatura.setBorder(BorderFactory.createTitledBorder("Dados da Fatura"));

        JPanel pnlForm = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 8, 8, 8);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel lblId = new JLabel("ID:");
        JLabel lblAuto = new JLabel("(auto)");
        JLabel lblData = new JLabel("Data:");
        JLabel lblCliente = new JLabel("Cliente:");
        JLabel lblServico = new JLabel("Serviço:");
        JLabel lblValor = new JLabel("Valor:");
        JLabel lblFormaPagamento = new JLabel("Forma de Pagamento:");
        JLabel lblStatus = new JLabel("Status:");

        txtId = new JTextField(10);
        txtId.setEditable(false);

        txtData = new JTextField(12);
        txtCliente = new JTextField(20);
        txtServico = new JTextField(20);
        txtValor = new JTextField(12);
        txtFormaPagamento = new JTextField(20);
        txtStatus = new JTextField(15);

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
        pnlForm.add(lblStatus, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtStatus, gbc);

        // linha 3
        gbc.gridx = 0; gbc.gridy = 2;
        pnlForm.add(lblCliente, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtCliente, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblServico, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtServico, gbc);

        // linha 4
        gbc.gridx = 0; gbc.gridy = 3;
        pnlForm.add(lblValor, gbc);

        gbc.gridx = 1;
        pnlForm.add(txtValor, gbc);

        gbc.gridx = 2;
        pnlForm.add(lblFormaPagamento, gbc);

        gbc.gridx = 3;
        pnlForm.add(txtFormaPagamento, gbc);

        JPanel pnlImagem = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        lblFotoAnimal = new JLabel();
        lblFotoAnimal.setIcon(iconeSerio);
        lblFotoAnimal.setPreferredSize(new Dimension(170, 260));
        pnlImagem.add(lblFotoAnimal);

        pnlDadosFatura.add(pnlForm, BorderLayout.CENTER);
        pnlDadosFatura.add(pnlImagem, BorderLayout.EAST);
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
        pnlListagemFaturas = new JPanel(new BorderLayout());
        pnlListagemFaturas.setBorder(BorderFactory.createTitledBorder("Listagem de Faturas"));
        pnlListagemFaturas.setPreferredSize(new Dimension(900, 240));

        String[] colunas = {"ID", "Data", "Cliente", "Serviço", "Valor", "Pagamento", "Status"};
        Object[][] dados = {
            {1, "10/04/2026", "Ana Souza", "Consulta", "50,00", "Cartão", "Paga"},
            {2, "11/04/2026", "Carlos Lima", "Vacinação", "35,00", "Dinheiro", "Pendente"}
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

    private boolean camposPreenchidos() {
        return !txtData.getText().trim().isEmpty()
                && !txtCliente.getText().trim().isEmpty()
                && !txtServico.getText().trim().isEmpty()
                && !txtValor.getText().trim().isEmpty()
                && !txtFormaPagamento.getText().trim().isEmpty()
                && !txtStatus.getText().trim().isEmpty();
    }

    private void alternarHumor(boolean feliz) {
        lblFotoAnimal.setIcon(feliz ? iconeFeliz : iconeSerio);
    }

    private void limparCampos() {
        txtId.setText("");
        txtData.setText("");
        txtCliente.setText("");
        txtServico.setText("");
        txtValor.setText("");
        txtFormaPagamento.setText("");
        txtStatus.setText("");
        txtData.requestFocusInWindow();
    }
}
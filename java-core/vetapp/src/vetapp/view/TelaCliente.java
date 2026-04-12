package vetapp.view;

import vetapp.dao.ClienteDAO;
import vetapp.model.Cliente;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.List;

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
    
    private Cliente obterClienteDosCampos() {
    Cliente cliente = new Cliente();

    if (!txtId.getText().trim().isEmpty()) {
        cliente.setIdCliente(Integer.parseInt(txtId.getText().trim()));
    }

    cliente.setNome(txtNome.getText().trim());
    cliente.setTelefone(fmtTelefone.getText().trim());
    cliente.setEmail(txtEmail.getText().trim());
    cliente.setEndereco(txtEndereco.getText().trim());

    return cliente;
}

    public TelaCliente() {
    configurarJanela();
    carregarImagens();
    criarComponentes();
    configurarEventos();
    carregarTabela();
    SwingUtilities.invokeLater(() -> txtNome.requestFocusInWindow());
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
    txtId.setFocusable(false);
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
    pnlListagemClientes = new JPanel(new BorderLayout());
    pnlListagemClientes.setBorder(BorderFactory.createTitledBorder("Listagem de Clientes"));
    pnlListagemClientes.setPreferredSize(new Dimension(680, 150));

    String[] colunas = {"ID", "Nome", "Telefone", "E-mail", "Endereço"};

    DefaultTableModel modelo = new DefaultTableModel(colunas, 0) {
        @Override
        public boolean isCellEditable(int row, int column) {
            return false;
        }
    };

    tblClientes = new JTable(modelo);
    JScrollPane scroll = new JScrollPane(tblClientes);

    pnlListagemClientes.add(scroll, BorderLayout.CENTER);
}

    private void carregarTabela() {
    DefaultTableModel modelo = (DefaultTableModel) tblClientes.getModel();
    modelo.setRowCount(0);

    ClienteDAO dao = new ClienteDAO();
    List<Cliente> lista = dao.listar();

    for (Cliente cliente : lista) {
        modelo.addRow(new Object[]{
            cliente.getIdCliente(),
            cliente.getNome(),
            cliente.getTelefone(),
            cliente.getEmail(),
            cliente.getEndereco()
        });
    }
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

        if (!camposPreenchidos()) {
            JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
            alternarHumor(false);

        } else if (!emailValido(txtEmail.getText())) {
            JOptionPane.showMessageDialog(this, "E-mail inválido.");
            alternarHumor(false);

        } else {
            Cliente cliente = obterClienteDosCampos();
            ClienteDAO dao = new ClienteDAO();

            boolean sucesso = dao.inserir(cliente);

            if (sucesso) {
                JOptionPane.showMessageDialog(this, "Cliente salvo com sucesso!");
                carregarTabela();
                limparCampos();
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Erro ao salvar cliente.");
                alternarHumor(false);
            }
        }
    });

    btnAtualizar.addActionListener(e -> {

        if (txtId.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Selecione um cliente na tabela para atualizar.");
            alternarHumor(false);

        } else if (!camposPreenchidos()) {
            JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
            alternarHumor(false);

        } else if (!emailValido(txtEmail.getText())) {
            JOptionPane.showMessageDialog(this, "E-mail inválido.");
            alternarHumor(false);

        } else {
            Cliente cliente = obterClienteDosCampos();
            ClienteDAO dao = new ClienteDAO();

            boolean sucesso = dao.atualizar(cliente);

            if (sucesso) {
                JOptionPane.showMessageDialog(this, "Cliente atualizado com sucesso!");
                carregarTabela();
                limparCampos();
                alternarHumor(true);
            } else {
                JOptionPane.showMessageDialog(this, "Erro ao atualizar cliente.");
                alternarHumor(false);
            }
        }
    });

    tblClientes.getSelectionModel().addListSelectionListener(e -> {
        if (!e.getValueIsAdjusting()) {
            carregarCamposDaTabela();
        }
    });
    
    btnExcluir.addActionListener(e -> {

    if (txtId.getText().trim().isEmpty()) {
        JOptionPane.showMessageDialog(this, "Selecione um cliente na tabela para excluir.");
        alternarHumor(false);

    } else {
        int confirmacao = JOptionPane.showConfirmDialog(
                this,
                "Deseja realmente excluir este cliente?",
                "Confirmar exclusão",
                JOptionPane.YES_NO_OPTION
        );

        if (confirmacao == JOptionPane.YES_OPTION) {
            int idCliente = Integer.parseInt(txtId.getText().trim());

            ClienteDAO dao = new ClienteDAO();
            boolean sucesso = dao.deletar(idCliente);

            if (sucesso) {
                JOptionPane.showMessageDialog(this, "Cliente excluído com sucesso!");
                carregarTabela();
                limparCampos();
                alternarHumor(true);
                } else {
                JOptionPane.showMessageDialog(
                        this,
            "Não foi possível excluir o cliente.\nEle pode estar vinculado a um animal ou outro registro do sistema."
    );
                alternarHumor(false);
}
        }
    }
});
    
    btnBuscar.addActionListener(e -> {

    if (txtId.getText().trim().isEmpty()) {
        JOptionPane.showMessageDialog(this, "Informe ou selecione o ID do cliente para buscar.");
        alternarHumor(false);
        return;
    }

    try {
        int idCliente = Integer.parseInt(txtId.getText().trim());

        ClienteDAO dao = new ClienteDAO();
        Cliente cliente = dao.buscarPorId(idCliente);

        if (cliente != null) {
            preencherCamposComCliente(cliente);
            JOptionPane.showMessageDialog(this, "Cliente encontrado!");
            alternarHumor(true);
        } else {
            JOptionPane.showMessageDialog(this, "Cliente não encontrado.");
            alternarHumor(false);
        }

    } catch (NumberFormatException ex) {
        JOptionPane.showMessageDialog(this, "ID inválido.");
        alternarHumor(false);
    }
});
}

    private boolean camposPreenchidos() {
    String telefone = fmtTelefone.getText()
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
            .replace("_", "")
            .trim();

    return !txtNome.getText().trim().isEmpty()
            && !telefone.isEmpty()
            && !txtEmail.getText().trim().isEmpty()
            && !txtEndereco.getText().trim().isEmpty();
}
    
    private boolean emailValido(String email) {
    return email.contains("@") && email.contains(".");
}

    private void limparCampos() {
    txtId.setText("");
    txtNome.setText("");
    fmtTelefone.setValue(null);
    txtEmail.setText("");
    txtEndereco.setText("");
    tblClientes.clearSelection();
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
    
    private void carregarCamposDaTabela() {
    int linhaSelecionada = tblClientes.getSelectedRow();

    if (linhaSelecionada != -1) {
        txtId.setText(tblClientes.getValueAt(linhaSelecionada, 0).toString());
        txtNome.setText(tblClientes.getValueAt(linhaSelecionada, 1).toString());
        fmtTelefone.setText(tblClientes.getValueAt(linhaSelecionada, 2).toString());
        txtEmail.setText(tblClientes.getValueAt(linhaSelecionada, 3).toString());
        txtEndereco.setText(tblClientes.getValueAt(linhaSelecionada, 4).toString());
    }
}
    
    private void preencherCamposComCliente(Cliente cliente) {
    txtId.setText(String.valueOf(cliente.getIdCliente()));
    txtNome.setText(cliente.getNome());
    fmtTelefone.setText(cliente.getTelefone());
    txtEmail.setText(cliente.getEmail());
    txtEndereco.setText(cliente.getEndereco());
}
    
}
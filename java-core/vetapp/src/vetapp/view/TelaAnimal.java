package vetapp.view;

import vetapp.model.Cliente;
import vetapp.dao.ClienteDAO;
import vetapp.dao.AnimalDAO;
import vetapp.model.Animal;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.List;

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
    private JTextField txtSexo;
    private JFormattedTextField txtDataNascimento;
    private JComboBox<Cliente> cbTutor;

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
    carregarClientes();
    configurarEventos();
    carregarTabela();
    SwingUtilities.invokeLater(() -> txtNomeAnimal.requestFocusInWindow());
    setVisible(true);

}

    private void configurarJanela() {
        setTitle("Gestão de Animais");
        setSize(720, 560);
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
        pnlDadosAnimal.setPreferredSize(new Dimension(680, 290));

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
        JLabel lblSexo = new JLabel("Sexo:");
        JLabel lblDataNascimento = new JLabel("Data Nasc.:");
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

        txtSexo = new JTextField(18);
        txtSexo.setPreferredSize(new Dimension(180, 25));

        try {
            txtDataNascimento = new JFormattedTextField(
                    new javax.swing.text.MaskFormatter("####-##-##")
    );
        } catch (java.text.ParseException e) {
            txtDataNascimento = new JFormattedTextField();
        }
        
        txtDataNascimento.setPreferredSize(new Dimension(180, 25));

        cbTutor = new JComboBox<>();
        cbTutor.setPreferredSize(new Dimension(180, 25));

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
        pnlForm.add(lblSexo, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtSexo, gbc);

        // linha 6
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 1;
        pnlForm.add(lblDataNascimento, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(txtDataNascimento, gbc);

        // linha 7
        gbc.gridx = 0;
        gbc.gridy = 6;
        gbc.gridwidth = 1;
        pnlForm.add(lblTutor, gbc);

        gbc.gridx = 1;
        gbc.gridwidth = 2;
        pnlForm.add(cbTutor, gbc);

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

    DefaultTableModel modelo = new DefaultTableModel(colunas, 0) {
        @Override
        public boolean isCellEditable(int row, int column) {
            return false;
        }
    };

    tblAnimais = new JTable(modelo);
    JScrollPane scroll = new JScrollPane(tblAnimais);

    pnlListagemAnimais.add(scroll, BorderLayout.CENTER);
}
    
    private void carregarTabela() {
    DefaultTableModel modelo = (DefaultTableModel) tblAnimais.getModel();
    modelo.setRowCount(0);

    AnimalDAO dao = new AnimalDAO();
    List<Animal> lista = dao.listar();

    System.out.println("Quantidade de animais carregados: " + lista.size());

    for (Animal animal : lista) {
        modelo.addRow(new Object[]{
            animal.getIdAnimal(),
            animal.getNome(),
            animal.getEspecie(),
            animal.getRaca(),
            animal.getIdCliente()
        });
    }

    modelo.fireTableDataChanged();
    tblAnimais.revalidate();
    tblAnimais.repaint();
}
    private void carregarClientes() {
    ClienteDAO dao = new ClienteDAO();
    List<Cliente> lista = dao.listar();

    cbTutor.removeAllItems();

    for (Cliente cliente : lista) {
        cbTutor.addItem(cliente);
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
        return;
    }

    // 👇 VALIDAÇÃO DA DATA AQUI (ANTES DO TRY)
    if (!dataValida(txtDataNascimento.getText().trim())) {
        JOptionPane.showMessageDialog(this, "Data inválida. Use formato YYYY-MM-DD.");
        alternarHumor(false);
        return;
    }

    try {
        Animal animal = obterAnimalDosCampos();
        AnimalDAO dao = new AnimalDAO();

        boolean sucesso = dao.inserir(animal);

        if (sucesso) {
            JOptionPane.showMessageDialog(this, "Animal salvo com sucesso!");
            carregarTabela();
            limparCampos();
            alternarHumor(true);
        } else {
            JOptionPane.showMessageDialog(this, "Erro ao salvar animal.");
            alternarHumor(false);
        }

    } catch (Exception ex) {
        JOptionPane.showMessageDialog(this, "Erro ao salvar animal.");
        ex.printStackTrace();
        alternarHumor(false);
    }
});
        
        tblAnimais.getSelectionModel().addListSelectionListener(e -> {
    if (!e.getValueIsAdjusting()) {
        carregarCamposDaTabela();
    }
});
     
    btnAtualizar.addActionListener(e -> {

    if (txtId.getText().trim().isEmpty()) {
        JOptionPane.showMessageDialog(this, "Selecione um animal na tabela para atualizar.");
        alternarHumor(false);
        return;
    }

    if (!camposPreenchidos()) {
        JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
        alternarHumor(false);
        return;
    }

    if (!dataValida(txtDataNascimento.getText().trim())) {
        JOptionPane.showMessageDialog(this, "Data inválida. Use o formato YYYY-MM-DD.");
        alternarHumor(false);
        return;
    }

    try {
        Animal animal = obterAnimalDosCampos();
        AnimalDAO dao = new AnimalDAO();

        boolean sucesso = dao.atualizar(animal);

        if (sucesso) {
            JOptionPane.showMessageDialog(this, "Animal atualizado com sucesso!");
            carregarTabela();
            limparCampos();
            alternarHumor(true);
        } else {
            JOptionPane.showMessageDialog(this, "Erro ao atualizar animal.");
            alternarHumor(false);
        }

    } catch (Exception ex) {
        JOptionPane.showMessageDialog(this, "Erro ao atualizar animal.");
        ex.printStackTrace();
        alternarHumor(false);
    }
});
        
    }

    private boolean camposPreenchidos() {
    return !txtNomeAnimal.getText().trim().isEmpty()
            && !txtEspecie.getText().trim().isEmpty()
            && !txtRaca.getText().trim().isEmpty()
            && !txtSexo.getText().trim().isEmpty()
            && !txtDataNascimento.getText().trim().isEmpty()
            && cbTutor.getSelectedItem() != null;
}

private void limparCampos() {
    txtId.setText("");
    txtNomeAnimal.setText("");
    txtEspecie.setText("");
    txtRaca.setText("");
    txtSexo.setText("");
    txtDataNascimento.setText("");
    if (cbTutor.getItemCount() > 0) {
    cbTutor.setSelectedIndex(0);
    }
    txtNomeAnimal.requestFocusInWindow();
}

private void carregarCamposDaTabela() {
    int linhaSelecionada = tblAnimais.getSelectedRow();

    if (linhaSelecionada != -1) {
        txtId.setText(tblAnimais.getValueAt(linhaSelecionada, 0).toString());
        txtNomeAnimal.setText(tblAnimais.getValueAt(linhaSelecionada, 1).toString());
        txtEspecie.setText(tblAnimais.getValueAt(linhaSelecionada, 2).toString());
        txtRaca.setText(tblAnimais.getValueAt(linhaSelecionada, 3).toString());

        txtSexo.setText("");
        txtDataNascimento.setText("");

        int idClienteTabela = Integer.parseInt(tblAnimais.getValueAt(linhaSelecionada, 4).toString());

        for (int i = 0; i < cbTutor.getItemCount(); i++) {
            Cliente c = cbTutor.getItemAt(i);

            if (c.getIdCliente() == idClienteTabela) {
                cbTutor.setSelectedIndex(i);
                break;
            }
        }

        try {
            int idAnimal = Integer.parseInt(txtId.getText().trim());
            AnimalDAO dao = new AnimalDAO();
            Animal animal = dao.buscarPorId(idAnimal);

            if (animal != null) {
                txtSexo.setText(animal.getSexo() != null ? animal.getSexo() : "");
                txtDataNascimento.setText(animal.getDataNascimento() != null ? animal.getDataNascimento() : "");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
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

private Animal obterAnimalDosCampos() {
    Animal animal = new Animal();

    if (!txtId.getText().trim().isEmpty()) {
        animal.setIdAnimal(Integer.parseInt(txtId.getText().trim()));
    }

    animal.setNome(txtNomeAnimal.getText().trim());
    animal.setEspecie(txtEspecie.getText().trim());
    animal.setRaca(txtRaca.getText().trim());
    animal.setSexo(txtSexo.getText().trim());
    animal.setDataNascimento(txtDataNascimento.getText().trim());

    Cliente clienteSelecionado = (Cliente) cbTutor.getSelectedItem();
    animal.setIdCliente(clienteSelecionado.getIdCliente());

    return animal;
}

private boolean dataValida(String data) {
    try {
        java.time.LocalDate.parse(data);
        return true;
    } catch (Exception e) {
        return false;
    }
}

}
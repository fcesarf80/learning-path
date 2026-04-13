package vetapp.view;

import vetapp.dao.AnimalDAO;
import vetapp.dao.ConsultaDAO;
import vetapp.dao.FuncionarioDAO;
import vetapp.model.Animal;
import vetapp.model.Consulta;
import vetapp.model.Funcionario;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;
import java.util.List;

public class TelaConsulta extends JFrame {

    private JPanel pnlDadosConsulta;
    private JPanel pnlAcoes;
    private JPanel pnlListagemConsultas;

    private JTable tblConsultas;

    private JTextField txtId;
    private JFormattedTextField txtData;
    private JFormattedTextField txtHora;
    private JComboBox<Animal> cbAnimal;
    private JComboBox<Funcionario> cbFuncionario;
    private JTextArea txtObservacao;

    private JButton btnNovo;
    private JButton btnSalvar;
    private JButton btnBuscar;
    private JButton btnAtualizar;
    private JButton btnExcluir;
    private JButton btnLimpar;
    private JButton btnVoltar;

    private JLabel lblFotoAnimal;
    private ImageIcon iconeSerio;
    private ImageIcon iconeFeliz;

    public TelaConsulta() {
        configurarJanela();
        carregarImagens();
        criarComponentes();
        carregarAnimais();
        carregarFuncionarios();
        configurarEventos();
        carregarTabela();
        SwingUtilities.invokeLater(() -> txtData.requestFocusInWindow());
        setVisible(true);
    }

    private void configurarJanela() {
        setTitle("Gestão de Consultas");
        setSize(720, 540);
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
    gbc.fill = GridBagConstraints.HORIZONTAL;

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

    try {
        txtData = new JFormattedTextField(new javax.swing.text.MaskFormatter("####-##-##"));
    } catch (java.text.ParseException e) {
        txtData = new JFormattedTextField();
    }
    txtData.setColumns(10);
    txtData.setToolTipText("Formato: YYYY-MM-DD");

    try {
        txtHora = new JFormattedTextField(new javax.swing.text.MaskFormatter("##:##:##"));
    } catch (java.text.ParseException e) {
        txtHora = new JFormattedTextField();
    }
    txtHora.setColumns(8);
    txtHora.setToolTipText("Formato: HH:MM:SS");

    cbAnimal = new JComboBox<>();
    cbFuncionario = new JComboBox<>();
    cbAnimal.setPreferredSize(new Dimension(180, 25));
    cbFuncionario.setPreferredSize(new Dimension(180, 25));

    txtObservacao = new JTextArea(3, 18);
    txtObservacao.setLineWrap(true);
    txtObservacao.setWrapStyleWord(true);

    JScrollPane scrollObservacao = new JScrollPane(txtObservacao);
    scrollObservacao.setPreferredSize(new Dimension(180, 60));

    // linha 1 - ID
    gbc.gridx = 0;
    gbc.gridy = 0;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    pnlForm.add(lblId, gbc);

    gbc.gridx = 1;
    gbc.weightx = 0;
    pnlForm.add(txtId, gbc);

    gbc.gridx = 2;
    gbc.weightx = 0;
    pnlForm.add(lblAuto, gbc);

    // linha 2 - Data
    gbc.gridx = 0;
    gbc.gridy = 1;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    pnlForm.add(lblData, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    gbc.weightx = 1.0;
    pnlForm.add(txtData, gbc);

    // linha 3 - Hora
    gbc.gridx = 0;
    gbc.gridy = 2;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    pnlForm.add(lblHora, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    gbc.weightx = 1.0;
    pnlForm.add(txtHora, gbc);

    // linha 4 - Animal
    gbc.gridx = 0;
    gbc.gridy = 3;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    pnlForm.add(lblAnimal, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    gbc.weightx = 1.0;
    pnlForm.add(cbAnimal, gbc);

    // linha 5 - Veterinário
    gbc.gridx = 0;
    gbc.gridy = 4;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    pnlForm.add(lblVeterinario, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    gbc.weightx = 1.0;
    pnlForm.add(cbFuncionario, gbc);

    // linha 6 - Observação
    gbc.gridx = 0;
    gbc.gridy = 5;
    gbc.gridwidth = 1;
    gbc.weightx = 0;
    gbc.weighty = 0;
    pnlForm.add(lblObservacao, gbc);

    gbc.gridx = 1;
    gbc.gridwidth = 2;
    gbc.weightx = 1.0;
    gbc.weighty = 1.0;
    pnlForm.add(scrollObservacao, gbc);

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

        String[] colunas = {"ID", "Data", "Hora", "Animal", "Veterinário", "Observação"};

        DefaultTableModel modelo = new DefaultTableModel(colunas, 0) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };

        tblConsultas = new JTable(modelo);
        JScrollPane scroll = new JScrollPane(tblConsultas);

        pnlListagemConsultas.add(scroll, BorderLayout.CENTER);
    }

    private void carregarAnimais() {
        AnimalDAO dao = new AnimalDAO();
        List<Animal> lista = dao.listar();

        cbAnimal.removeAllItems();

        for (Animal animal : lista) {
            cbAnimal.addItem(animal);
        }
    }

    private void carregarFuncionarios() {
    FuncionarioDAO dao = new FuncionarioDAO();
    List<Funcionario> lista = dao.listarFuncionarios();

    System.out.println("Quantidade de funcionários no combo: " + lista.size());

    cbFuncionario.removeAllItems();

    for (Funcionario funcionario : lista) {
        System.out.println("Funcionário carregado: " 
            + funcionario.getIdFuncionario() + " - " 
            + funcionario.getNome());

        cbFuncionario.addItem(funcionario);
    }
}

    private void carregarTabela() {
        DefaultTableModel modelo = (DefaultTableModel) tblConsultas.getModel();
        modelo.setRowCount(0);

        ConsultaDAO consultaDAO = new ConsultaDAO();
        AnimalDAO animalDAO = new AnimalDAO();
        FuncionarioDAO funcionarioDAO = new FuncionarioDAO();

        List<Consulta> lista = consultaDAO.listarConsultas();

        for (Consulta consulta : lista) {
            Animal animal = animalDAO.buscarPorId(consulta.getIdAnimal());
            Funcionario funcionario = funcionarioDAO.buscarPorId(consulta.getIdFuncionario());

            modelo.addRow(new Object[]{
                consulta.getIdConsulta(),
                consulta.getDataConsulta(),
                consulta.getHoraConsulta(),
                animal != null ? animal.getNome() : "",
                funcionario != null ? funcionario.getNome() : "",
                consulta.getObservacao()
            });
        }
        
        tblConsultas.setRowHeight(22);
        tblConsultas.getTableHeader().setReorderingAllowed(false);
        
        DefaultTableCellRenderer centralizado = new DefaultTableCellRenderer();
        centralizado.setHorizontalAlignment(SwingConstants.CENTER);

        tblConsultas.getColumnModel().getColumn(0).setCellRenderer(centralizado); // ID
        tblConsultas.getColumnModel().getColumn(1).setCellRenderer(centralizado); // Data
        tblConsultas.getColumnModel().getColumn(2).setCellRenderer(centralizado); // Hora
        tblConsultas.getColumnModel().getColumn(0).setPreferredWidth(40); // ID
        tblConsultas.getColumnModel().getColumn(1).setPreferredWidth(80); // Data
        tblConsultas.getColumnModel().getColumn(2).setPreferredWidth(70); // Hora
        
        
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

            if (!dataValida(txtData.getText().trim())) {
                JOptionPane.showMessageDialog(this, "Data inválida. Use o formato YYYY-MM-DD.");
                alternarHumor(false);
                return;
            }

            if (!horaValida(txtHora.getText().trim())) {
                JOptionPane.showMessageDialog(this, "Hora inválida. Use o formato HH:MM:SS.");
                alternarHumor(false);
                return;
            }

            try {
                Consulta consulta = obterConsultaDosCampos();
                ConsultaDAO dao = new ConsultaDAO();

                boolean sucesso = dao.inserir(consulta);

                if (sucesso) {
                    JOptionPane.showMessageDialog(this, "Consulta salva com sucesso!");
                    carregarTabela();
                    limparCampos();
                    alternarHumor(true);
                } else {
                    JOptionPane.showMessageDialog(this, "Não foi possível salvar a consulta.");
                    alternarHumor(false);
                }

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao salvar consulta.");
                ex.printStackTrace();
                alternarHumor(false);
            }
        });

        tblConsultas.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                carregarCamposDaTabela();
            }
        });

        btnBuscar.addActionListener(e -> {
            if (txtId.getText().trim().isEmpty()) {
                JOptionPane.showMessageDialog(this, "Informe ou selecione o ID da consulta para buscar.");
                alternarHumor(false);
                return;
            }

            try {
                int idConsulta = Integer.parseInt(txtId.getText().trim());
                ConsultaDAO dao = new ConsultaDAO();
                Consulta consulta = dao.buscarPorId(idConsulta);

                if (consulta != null) {
                    preencherCamposComConsulta(consulta);
                    JOptionPane.showMessageDialog(this, "Consulta encontrada!");
                    alternarHumor(true);
                } else {
                    JOptionPane.showMessageDialog(this, "Consulta não encontrada.");
                    alternarHumor(false);
                }

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "ID inválido.");
                alternarHumor(false);
            }
        });

        btnAtualizar.addActionListener(e -> {
            if (txtId.getText().trim().isEmpty()) {
                JOptionPane.showMessageDialog(this, "Selecione uma consulta na tabela para atualizar.");
                alternarHumor(false);
                return;
            }

            if (!camposPreenchidos()) {
                JOptionPane.showMessageDialog(this, "Preencha todos os campos.");
                alternarHumor(false);
                return;
            }

            if (!dataValida(txtData.getText().trim())) {
                JOptionPane.showMessageDialog(this, "Data inválida. Use o formato YYYY-MM-DD.");
                alternarHumor(false);
                return;
            }

            if (!horaValida(txtHora.getText().trim())) {
                JOptionPane.showMessageDialog(this, "Hora inválida. Use o formato HH:MM:SS.");
                alternarHumor(false);
                return;
            }

            try {
                Consulta consulta = obterConsultaDosCampos();
                ConsultaDAO dao = new ConsultaDAO();

                boolean sucesso = dao.atualizar(consulta);

                if (sucesso) {
                    JOptionPane.showMessageDialog(this, "Consulta atualizada com sucesso!");
                    carregarTabela();
                    limparCampos();
                    alternarHumor(true);
                } else {
                    JOptionPane.showMessageDialog(this, "Erro ao atualizar consulta.");
                    alternarHumor(false);
                }

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao atualizar consulta.");
                ex.printStackTrace();
                alternarHumor(false);
            }
        });

        btnExcluir.addActionListener(e -> {
            if (txtId.getText().trim().isEmpty()) {
                JOptionPane.showMessageDialog(this, "Selecione uma consulta na tabela para excluir.");
                alternarHumor(false);
                return;
            }

            int confirmacao = JOptionPane.showConfirmDialog(
                this,
                "Deseja realmente excluir esta consulta?",
                "Confirmar exclusão",
                JOptionPane.YES_NO_OPTION
            );

            if (confirmacao != JOptionPane.YES_OPTION) {
                return;
            }

            try {
                int idConsulta = Integer.parseInt(txtId.getText().trim());
                ConsultaDAO dao = new ConsultaDAO();

                boolean sucesso = dao.deletar(idConsulta);

                if (sucesso) {
                    JOptionPane.showMessageDialog(this, "Consulta excluída com sucesso!");
                    carregarTabela();
                    limparCampos();
                    alternarHumor(true);
                } else {
                    JOptionPane.showMessageDialog(this, "Erro ao excluir consulta.");
                    alternarHumor(false);
                }

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao excluir consulta.");
                ex.printStackTrace();
                alternarHumor(false);
            }
        });
    }

    private Consulta obterConsultaDosCampos() {
    Consulta consulta = new Consulta();

    if (!txtId.getText().trim().isEmpty()) {
        consulta.setIdConsulta(Integer.parseInt(txtId.getText().trim()));
    }

    consulta.setDataConsulta(txtData.getText().trim());
    consulta.setHoraConsulta(txtHora.getText().trim());
    consulta.setObservacao(txtObservacao.getText().trim());

    Animal animalSelecionado = (Animal) cbAnimal.getSelectedItem();
    Funcionario funcionarioSelecionado = (Funcionario) cbFuncionario.getSelectedItem();

    consulta.setIdAnimal(animalSelecionado.getIdAnimal());
    consulta.setIdFuncionario(funcionarioSelecionado.getIdFuncionario());

    return consulta;
}

    private boolean camposPreenchidos() {
        return !txtData.getText().trim().isEmpty()
            && !txtHora.getText().trim().isEmpty()
            && cbAnimal.getSelectedItem() != null
            && cbFuncionario.getSelectedItem() != null
            && !txtObservacao.getText().trim().isEmpty();
}

    private void limparCampos() {
    txtId.setText("");
    txtData.setText("");
    txtHora.setText("");
    txtObservacao.setText("");

    if (cbAnimal.getItemCount() > 0) {
        cbAnimal.setSelectedIndex(0);
    }

    if (cbFuncionario.getItemCount() > 0) {
        cbFuncionario.setSelectedIndex(0);
    }

    tblConsultas.clearSelection();
    txtData.requestFocusInWindow();
}
private void carregarCamposDaTabela() {
    int linhaSelecionada = tblConsultas.getSelectedRow();

    if (linhaSelecionada != -1) {
        txtId.setText(tblConsultas.getValueAt(linhaSelecionada, 0).toString());

        try {
            int idConsulta = Integer.parseInt(txtId.getText().trim());
            ConsultaDAO dao = new ConsultaDAO();
            Consulta consulta = dao.buscarPorId(idConsulta);

            if (consulta != null) {
                preencherCamposComConsulta(consulta);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

private void preencherCamposComConsulta(Consulta consulta) {
    txtId.setText(String.valueOf(consulta.getIdConsulta()));
    txtData.setText(consulta.getDataConsulta());
    txtHora.setText(consulta.getHoraConsulta());
    txtObservacao.setText(consulta.getObservacao());

    // Selecionar Animal no ComboBox
    for (int i = 0; i < cbAnimal.getItemCount(); i++) {
        Animal animal = cbAnimal.getItemAt(i);
        if (animal.getIdAnimal() == consulta.getIdAnimal()) {
            cbAnimal.setSelectedIndex(i);
            break;
        }
    }

    // Debug do Funcionário
    System.out.println("ID funcionário da consulta: " + consulta.getIdFuncionario());

    // Selecionar Funcionário no ComboBox
    for (int i = 0; i < cbFuncionario.getItemCount(); i++) {
        Funcionario funcionario = cbFuncionario.getItemAt(i);
        System.out.println("Combo funcionário ID: " + funcionario.getIdFuncionario());

        if (funcionario.getIdFuncionario() == consulta.getIdFuncionario()) {
            cbFuncionario.setSelectedIndex(i);
            break;
        }
    }
}
    

    private boolean dataValida(String data) {
        try {
            java.time.LocalDate.parse(data);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private boolean horaValida(String hora) {
        try {
            java.time.LocalTime.parse(hora);
            return true;
        } catch (Exception e) {
            return false;
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
    
    
    
}
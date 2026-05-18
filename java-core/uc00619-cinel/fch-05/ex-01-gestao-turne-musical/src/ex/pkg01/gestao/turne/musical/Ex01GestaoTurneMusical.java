package ex.pkg06.gestao.turne.musical.view;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

// O nome da classe foi atualizado para condizer exatamente com o nome do ficheiro
public class Ex01GestaoTurneMusical extends JFrame {

    private JComboBox<String> comboCidades;
    private JTextField txtData, txtPreco, txtVendidos, txtPesquisaCidade;
    private JTable tabela;
    private DefaultTableModel modeloTabela;
    
    private final String FICHEIRO_CONCERTOS = "concertos.txt";
    private final String FICHEIRO_CIDADES = "cidades.txt";
    private final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    // Construtor com o mesmo nome da classe
    public Ex01GestaoTurneMusical() {
        setTitle("Before Midnight Tour - Gestão de Turné 2026");
        setSize(850, 720); 
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        // Carregamento do Ícone
        try {
            File ficheiroIcone = new File("img/cinel-icone.png");
            if (ficheiroIcone.exists()) {
                BufferedImage imgOriginal = ImageIO.read(ficheiroIcone);
                setIconImage(imgOriginal);
            }
        } catch (Exception e) {
            System.out.println("Não foi possível carregar o ícone do CINEL.");
        }

        inicializarFicheiroCidades();

        JPanel painelTopoAgrupado = new JPanel();
        painelTopoAgrupado.setLayout(new BoxLayout(painelTopoAgrupado, BoxLayout.Y_AXIS));

        ImageIcon iconBanner = new ImageIcon("img/banner.png"); 
        JLabel lblBanner = new JLabel(iconBanner);
        lblBanner.setAlignmentX(Component.CENTER_ALIGNMENT); 
        
        painelTopoAgrupado.add(lblBanner);
        painelTopoAgrupado.add(Box.createVerticalStrut(10)); 

        JPanel painelForm = new JPanel(new GridBagLayout());
        painelForm.setBorder(BorderFactory.createTitledBorder("Adicionar Novo Concerto"));
        GridBagConstraints gbc = new GridBagConstraints();
        gbClassico(gbc);

        painelForm.add(new JLabel("Cidade:"), gbc);
        gbc.gridx = 1;
        comboCidades = new JComboBox<>(carregarCidades());
        painelForm.add(comboCidades, gbc);

        gbc.gridx = 0; gbc.gridy = 1;
        painelForm.add(new JLabel("Data (AAAA-MM-DD):"), gbc);
        gbc.gridx = 1;
        txtData = new JTextField(10);
        painelForm.add(txtData, gbc);

        gbc.gridx = 2; gbc.gridy = 0;
        painelForm.add(new JLabel("Preço (€):"), gbc);
        gbc.gridx = 3;
        txtPreco = new JTextField(8);
        painelForm.add(txtPreco, gbc);

        gbc.gridx = 2; gbc.gridy = 1;
        painelForm.add(new JLabel("Bilhetes Vendidos:"), gbc);
        gbc.gridx = 3;
        txtVendidos = new JTextField(8);
        painelForm.add(txtVendidos, gbc);

        gbc.gridx = 4; gbc.gridy = 0; gbc.gridheight = 2;
        JButton btnAdicionar = new JButton("Agendar Concerto");
        btnAdicionar.setBackground(new Color(46, 204, 113));
        btnAdicionar.setForeground(Color.WHITE);
        painelForm.add(btnAdicionar, gbc);

        painelTopoAgrupado.add(painelForm);
        add(painelTopoAgrupado, BorderLayout.NORTH);

        String[] colunas = {"Cidade", "Data", "Preço (€)", "Bilhetes Vendidos", "Total Angariado (€)"};
        modeloTabela = new DefaultTableModel(colunas, 0) {
            @Override
            public boolean isCellEditable(int row, int column) { return false; }
        };
        tabela = new JTable(modeloTabela);
        add(new JScrollPane(tabela), BorderLayout.CENTER);

        JPanel painelInferior = new JPanel(new BorderLayout(5, 5));
        painelInferior.setBorder(BorderFactory.createEmptyBorder(5, 10, 10, 10));

        JPanel painelPesquisa = new JPanel(new FlowLayout(FlowLayout.LEFT));
        painelPesquisa.add(new JLabel("Pesquisar por Cidade:"));
        txtPesquisaCidade = new JTextField(12);
        painelPesquisa.add(txtPesquisaCidade);
        JButton btnPesquisar = new JButton("Filtrar");
        JButton btnLimparFiltro = new JButton("Mostrar Todos");
        painelPesquisa.add(btnPesquisar);
        painelPesquisa.add(btnLimparFiltro);
        painelInferior.add(painelPesquisa, BorderLayout.WEST);

        JPanel painelAcoes = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        JButton btnCalcular = new JButton("Faturação Total");
        JButton btnRemover = new JButton("Remover Cancelado");
        JButton btnSair = new JButton("Sair");
        
        btnCalcular.setBackground(new Color(52, 152, 219));
        btnCalcular.setForeground(Color.WHITE);
        btnRemover.setBackground(new Color(231, 76, 60));
        btnRemover.setForeground(Color.WHITE);
        btnSair.setBackground(new Color(149, 165, 166));
        btnSair.setForeground(Color.WHITE);

        painelAcoes.add(btnCalcular);
        painelAcoes.add(btnRemover);
        painelAcoes.add(btnSair);
        painelInferior.add(painelAcoes, BorderLayout.EAST);

        add(painelInferior, BorderLayout.SOUTH);

        btnAdicionar.addActionListener(e -> guardarConcerto());
        btnRemover.addActionListener(e -> removerConcertoSelecionado());
        btnPesquisar.addActionListener(e -> filtrarPorCidade());
        btnLimparFiltro.addActionListener(e -> carregarConcertosFicheiro());
        btnCalcular.addActionListener(e -> calcularFaturacaoTotal());
        btnSair.addActionListener(e -> System.exit(0));

        carregarConcertosFicheiro();
        setVisible(true);
    }

    private void gbClassico(GridBagConstraints gbc) {
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.gridx = 0;
        gbc.gridy = 0;
    }

    private void calcularFaturacaoTotal() {
        double totalGeral = 0;
        for (int i = 0; i < modeloTabela.getRowCount(); i++) {
            totalGeral += Double.parseDouble(modeloTabela.getValueAt(i, 4).toString());
        }
        JOptionPane.showMessageDialog(this, "A faturação total acumulada da Tournée é de: " + totalGeral + " €", "Faturação Global", JOptionPane.INFORMATION_MESSAGE);
    }

    private void guardarConcerto() {
        String cidade = (String) comboCidades.getSelectedItem();
        String dataStr = txtData.getText().trim();
        String precoStr = txtPreco.getText().trim();
        String vendidosStr = txtVendidos.getText().trim();

        if (dataStr.isEmpty() || precoStr.isEmpty() || vendidosStr.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Erro: Nenhum campo pode ficar vazio!", "Validação", JOptionPane.WARNING_MESSAGE);
            return;
        }

        try {
            LocalDate dataIntroduzida = LocalDate.parse(dataStr, formatter);
            LocalDate hoje = LocalDate.now();

            if (dataIntroduzida.isBefore(hoje)) {
                JOptionPane.showMessageDialog(this, "Erro: Não é permitido agendar concertos em datas passadas!", "Data Inválida", JOptionPane.ERROR_MESSAGE);
                return;
            }

            double preco = Double.parseDouble(precoStr);
            int vendidos = Integer.parseInt(vendidosStr);

            if (preco < 0 || vendidos < 0) {
                JOptionPane.showMessageDialog(this, "Erro: Valores não podem ser negativos.", "Erro Numérico", JOptionPane.ERROR_MESSAGE);
                return;
            }

            double total = preco * vendidos;

            try (FileWriter fw = new FileWriter(FICHEIRO_CONCERTOS, true);
                 PrintWriter pw = new PrintWriter(fw)) {
                pw.println(cidade + ";" + dataStr + ";" + preco + ";" + vendidos + ";" + total);
            }

            carregarConcertosFicheiro();
            limparFormulario();

        } catch (DateTimeParseException e) {
            JOptionPane.showMessageDialog(this, "Formato de data inválido! Use o padrão AAAA-MM-DD (Ex: 2026-07-15).", "Erro de Data", JOptionPane.ERROR_MESSAGE);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Preço ou quantidade de bilhetes inválidos!", "Erro de Formato", JOptionPane.ERROR_MESSAGE);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Erro ao gravar dados no ficheiro.", "Erro E/S", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void carregarConcertosFicheiro() {
        modeloTabela.setRowCount(0);
        File f = new File(FICHEIRO_CONCERTOS);
        if (!f.exists()) return;

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] dados = linha.split(";");
                if (dados.length == 5) {
                    modeloTabela.addRow(dados);
                }
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler ficheiro de concertos.");
        }
    }

    private void removerConcertoSelecionado() {
        int linhaSelecionada = tabela.getSelectedRow();
        if (linhaSelecionada == -1) {
            JOptionPane.showMessageDialog(this, "Selecione um concerto na tabela para o remover/cancelar.", "Aviso", JOptionPane.INFORMATION_MESSAGE);
            return;
        }

        int resposta = JOptionPane.showConfirmDialog(this, "Tem a certeza que deseja cancelar este concerto?", "Confirmar Remoção", JOptionPane.YES_NO_OPTION);
        if (resposta != JOptionPane.YES_OPTION) return;

        String cidadeSel = (String) tabela.getValueAt(linhaSelecionada, 0);
        String dataSel = (String) tabela.getValueAt(linhaSelecionada, 1);

        File fOriginal = new File(FICHEIRO_CONCERTOS);
        File fTemp = new File("concertos_temp.txt");

        try (BufferedReader br = new BufferedReader(new FileReader(fOriginal));
             PrintWriter pw = new PrintWriter(new FileWriter(fTemp))) {
            
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] dados = linha.split(";");
                if (dados.equals(cidadeSel) && dados.equals(dataSel)) {
                    continue; 
                }
                pw.println(linha);
            }
        } catch (IOException e) {
            System.out.println("Erro ao processar ficheiro temporário.");
        }

        fOriginal.delete();
        fTemp.renameTo(fOriginal);
        carregarConcertosFicheiro();
    }

    private void filtrarPorCidade() {
        String termo = txtPesquisaCidade.getText().trim().toLowerCase();
        if (termo.isEmpty()) {
            carregarConcertosFicheiro();
            return;
        }

        modeloTabela.setRowCount(0);
        try (BufferedReader br = new BufferedReader(new FileReader(FICHEIRO_CONCERTOS))) {
            String databaseLinha;
            while ((databaseLinha = br.readLine()) != null) {
                String[] dados = databaseLinha.split(";");
                if (dados.toLowerCase().contains(termo)) {
                    modeloTabela.addRow(dados);
                }
            }
        } catch (IOException e) {
            System.out.println("Erro na filtragem.");
        }
    }

    private String[] carregarCidades() {
        try (BufferedReader br = new BufferedReader(new FileReader(FICHEIRO_CIDADES))) {
            return br.lines().toArray(String[]::new);
        } catch (IOException e) {
            return new String[]{"Lisboa", "Porto", "Madrid", "Paris", "Londres"};
        }
    }

    private void inicializarFicheiroCidades() {
        File f = new File(FICHEIRO_CIDADES);
        if (!f.exists()) {
            try (PrintWriter pw = new PrintWriter(new FileWriter(f))) {
                pw.println("Lisboa");
                pw.println("Porto");
                pw.println("Madrid");
                pw.println("Paris");
                pw.println("Londres");
            } catch (IOException e) {
                System.out.println("Erro ao criar lista base de cidades.");
            }
        }
    }

    private void limparFormulario() {
        txtData.setText("");
        txtPreco.setText("");
        txtVendidos.setText("");
        comboCidades.setSelectedIndex(0);
    }

    public static void main(String[] args) {
        // Inicializa a classe com o nome correto
        SwingUtilities.invokeLater(() -> new Ex01GestaoTurneMusical());
    }
}

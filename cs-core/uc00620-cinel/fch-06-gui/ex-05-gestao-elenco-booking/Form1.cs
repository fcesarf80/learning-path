using MySql.Data.MySqlClient;
using System;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace ex_05_gestao_elenco_booking
{
    public partial class Form1 : Form
    {
        #region Inicialização e Variáveis Globais

        // Definição dos parâmetros de ligação à base de dados relacional
        private string stringConexao = "Server=localhost;Database=booking_artistico;Uid=root;Pwd=SUA_SENHA_AQUI;";
        private string caminhoImagemSelecionada = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Configurações estáticas de dimensionamento do ecrã (1024x768)
            this.Size = new Size(1024, 768);
            this.MinimumSize = new Size(1024, 768);
            this.MaximumSize = new Size(1024, 768);
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;

            // Restrição de tamanho máximo de caracteres conforme o VARCHAR da base de dados
            txtNomeArtistico.MaxLength = 100;

            // Bloqueio de redimensionamento manual das colunas da grelha de dados
            dgvArtistas.AllowUserToResizeColumns = false;
            dgvArtistas.AllowUserToResizeRows = false;

            // Associação manual dos eventos para evitar quebra no Designer
            this.Load += new System.EventHandler(this.Form1_Load);
            this.btnCarregarFoto.Click += new System.EventHandler(this.btnCarregarFoto_Click);
            this.btnInserir.Click += new System.EventHandler(this.btnInserir_Click);
            this.btnEditar.Click += new System.EventHandler(this.btnEditar_Click);
            this.btnEliminar.Click += new System.EventHandler(this.btnEliminar_Click);
            this.dgvArtistas.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvArtistas_CellClick);

            // Operações iniciais de conectividade e leitura
            CarregarCategorias();
            AtualizarGrelha();
        }

        #endregion

        #region Métodos de Base de Dados (Leitura)

        private void CarregarCategorias()
        {
            try
            {
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();
                    string query = "SELECT id_categoria, nome_categoria FROM categoria";
                    MySqlDataAdapter da = new MySqlDataAdapter(query, conn);
                    DataTable dt = new DataTable();
                    da.Fill(dt);

                    cmbCategoria.DataSource = dt;
                    cmbCategoria.DisplayMember = "nome_categoria";
                    cmbCategoria.ValueMember = "id_categoria";
                    cmbCategoria.SelectedIndex = -1; // Inicia sem nenhuma categoria pré-selecionada
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao carregar categorias: " + ex.Message, "Erro de Ligação", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void AtualizarGrelha()
        {
            try
            {
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();
                    string query = @"SELECT a.id_artista AS 'ID', 
                                            a.nome_artistico AS 'Nome Artístico', 
                                            c.nome_categoria AS 'Categoria', 
                                            a.caminho_foto AS 'Caminho da Foto' 
                                     FROM artista a 
                                     INNER JOIN categoria c ON a.fk_categoria = c.id_categoria";

                    MySqlDataAdapter da = new MySqlDataAdapter(query, conn);
                    DataTable dt = new DataTable();
                    da.Fill(dt);

                    dgvArtistas.DataSource = dt;
                }
                LimparFormulario();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao atualizar dados da grelha: " + ex.Message, "Erro de Consulta", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        #endregion

        #region Eventos dos Botões (Esboços para os próximos Commits)

        private void btnCarregarFoto_Click(object sender, EventArgs e)
        {
            // Será implementado no Commit 4
        }

        private void btnInserir_Click(object sender, EventArgs e)
        {
            // Será implementado no Commit 5
        }

        private void btnEditar_Click(object sender, EventArgs e)
        {
            // Será implementado no Commit 5
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            // Será implementado no Commit 5
        }

        private void dgvArtistas_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            // Será implementado no Commit 5
        }

        #endregion

        #region Métodos Auxiliares e Métodos Vazios do Designer

        private void LimparFormulario()
        {
            txtNomeArtistico.Clear();
            cmbCategoria.SelectedIndex = -1;
            picFotografia.Image = null;
            caminhoImagemSelecionada = "";
        }

        // Mantidos para evitar que o Designer acuse falta de referências antigas
        private void label1_Click(object sender, EventArgs e) { }
        private void label3_Click(object sender, EventArgs e) { }
        private void pictureBox3_Click(object sender, EventArgs e) { }
        private void dataGridView1_AutoSizeColumnsModeChanged(object sender, DataGridViewAutoSizeColumnsModeEventArgs e) { }

        #endregion
    }
}

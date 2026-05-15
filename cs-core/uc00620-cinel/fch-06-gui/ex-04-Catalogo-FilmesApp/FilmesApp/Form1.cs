using MySql.Data.MySqlClient;
using System;
using System.Windows.Forms;

namespace FilmesApp
{
    public partial class FormFilmes : Form
    {
        MySqlConnection conexao;

        List<Categoria> LTipoFilmes;

        BindingList<Filme>

        public FormFilmes()
        {
            InitializeComponent();
        }

        private void btnConectar_Click(object sender, EventArgs e)
        {
            try
            {
                string dataSource = txtDatasource.Text;
                string utilizador = txtUtilizador.Text;
                string password = txtPassword.Text;

                if (!int.TryParse(txtPorta.Text, out int porta))
                {
                    MessageBox.Show("Porta inválida!");
                    return;
                }

                // Certifique-se que o nome da base de dados 'catalogo_filmesapp' existe no seu MySQL
                string strConexao = $"server={dataSource};port={porta};user={utilizador};password={password};database=catalogo_filmesapp;";

                conexao = new MySqlConnection(strConexao);
                conexao.Open();

                MessageBox.Show("Conexão realizada com sucesso!");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao conectar: " + ex.Message);
            }
        }

        private void FormFilmes_Load(object sender, EventArgs e) { }
    }
}

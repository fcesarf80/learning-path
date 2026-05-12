using MySql.Data.MySqlClient;
using System;
using System.Windows.Forms;

namespace FilmesApp
{
    public partial class FormFilmes : Form
    {
        MySqlConnection conexao;

        public FormFilmes()
        {
            InitializeComponent();
        }

        private void FormFilmes_Load(object sender, EventArgs e)
        {
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

                string connectionInfo = $"server={dataSource};port={porta};user={utilizador};password={password};database=catalogo_filmesapp;";


                conexao = new MySqlConnection(connectionInfo);
                conexao.Open();

                MessageBox.Show("Conexão realizada com sucesso!");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        } // Fecha o btnConectar_Click

        private void txtPassword_TextChanged(object sender, EventArgs e)
        {
        }
    } // Fecha a classe FormFilmes
} // Fecha o namespace

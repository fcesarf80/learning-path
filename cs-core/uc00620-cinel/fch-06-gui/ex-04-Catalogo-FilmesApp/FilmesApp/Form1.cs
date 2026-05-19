using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Windows.Forms;

namespace FilmesApp
{
    public partial class FormFilmes : Form
    {
        private MySqlConnection conexao;
        private List<Categoria> LTipoFilmes;
        private BindingList<Filme> listaFilmes;

        public FormFilmes()
        {
            InitializeComponent();
        }

        private void FormFilmes_Load(object sender, EventArgs e)
        {
            listaFilmes = new BindingList<Filme>();
            tabelaFilmes.DataSource = listaFilmes;
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

                string strConexao = $"server={dataSource};port={porta};user={utilizador};password={password};database=catalogo_filmesapp;";

                conexao = new MySqlConnection(strConexao);
                conexao.Open();

                MessageBox.Show("Conexão realizada com sucesso!");

                PreencherCombo();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao conectar: " + ex.Message);
            }
        }

        private void PreencherCombo()
        {
            try
            {
                LTipoFilmes = new List<Categoria>();
                string sql = "SELECT id_categoria, descricao FROM categorias";

                using (MySqlCommand cmd = new MySqlCommand(sql, conexao))
                {
                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            int id = reader.GetInt32("id_categoria");
                            string desc = reader.GetString("descricao");

                            Categoria tipo = new Categoria(id, desc);
                            LTipoFilmes.Add(tipo);
                        }
                    }
                }

                cmbTipo.DataSource = LTipoFilmes;
                cmbTipo.DisplayMember = "Descricao";
                cmbTipo.ValueMember = "IdCategoria";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao carregar categorias: " + ex.Message);
            }
        }

        private void txtPassword_TextChanged(object sender, EventArgs e)
        {
            // Gerado automaticamente pelo designer
        }
    }
}

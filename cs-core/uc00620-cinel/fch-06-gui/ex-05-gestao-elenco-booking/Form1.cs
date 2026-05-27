using System;
using System.Data;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace ex_05_gestao_elenco_booking
{
    public partial class Form1 : Form
    {
        private string stringConexao = "Server=127.0.0.1;Port=3306;Database=booking_artistico;Uid=root;Pwd=;";
        private string caminhoImagemSelecionada = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1024, 657);
            this.MinimumSize = new Size(1024, 657);
            this.MaximumSize = new Size(1024, 657);
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;

            txtNomeArtistico.MaxLength = 100;

            dgvArtistas.AllowUserToResizeColumns = false;
            dgvArtistas.AllowUserToResizeRows = false;
            dgvArtistas.AutoGenerateColumns = false;

            dgvArtistas.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dgvArtistas.MultiSelect = false;
            dgvArtistas.ReadOnly = true;

            dgvArtistas.RowHeadersVisible = false;
            dgvArtistas.AllowUserToAddRows = false;

            colID.DataPropertyName = "id_artista";
            colNome.DataPropertyName = "nome_artistico";
            colCategoria.DataPropertyName = "nome_categoria";
            ColFoto.DataPropertyName = "caminho_foto";

            this.btnCarregarFoto.Click += new System.EventHandler(this.btnCarregarFoto_Click);
            this.btnInserir.Click += new System.EventHandler(this.btnInserir_Click);
            this.btnEditar.Click += new System.EventHandler(this.btnEditar_Click);
            this.btnEliminar.Click += new System.EventHandler(this.btnEliminar_Click);
            this.dgvArtistas.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvArtistas_CellClick);

            CarregarCategories();
            AtualizarGrelha();
                        
        }

        private void CarregarCategories()
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
                    cmbCategoria.SelectedIndex = -1;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        }

        private void AtualizarGrelha()
        {
            try
            {
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();
                    string query = "SELECT a.id_artista, a.nome_artistico, c.nome_categoria, a.caminho_foto FROM artista a INNER JOIN categoria c ON a.fk_categoria = c.id_categoria";
                    MySqlDataAdapter da = new MySqlDataAdapter(query, conn);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dgvArtistas.DataSource = dt;
                }
                LimparFormulario();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao atualizar grelha: " + ex.Message, "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void CarregarImagem(string caminho)
        {
            try
            {
                if (!string.IsNullOrEmpty(caminho) && File.Exists(caminho))
                {
                    byte[] bytes = File.ReadAllBytes(caminho);

                    using (MemoryStream ms = new MemoryStream(bytes))
                    {
                        picFotografia.Image = Image.FromStream(ms);
                    }
                }
                else
                {
                    picFotografia.Image = null;
                }
            }
            catch
            {
                picFotografia.Image = null;
            }
        }

        private void btnCarregarFoto_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog ofd = new OpenFileDialog())
            {
                ofd.Filter = "Imagens|*.jpg;*.jpeg;*.png;*.bmp";

                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    caminhoImagemSelecionada = ofd.FileName;

                    CarregarImagem(caminhoImagemSelecionada);
                }
            }
        }

        private void btnInserir_Click(object sender, EventArgs e)
        {
            if (!ValidarCampos()) return;

            try
            {
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();

                    string verificar = "SELECT COUNT(*) FROM artista WHERE nome_artistico = @nome";

                    using (MySqlCommand verificarCmd = new MySqlCommand(verificar, conn))
                    {
                        verificarCmd.Parameters.AddWithValue("@nome", txtNomeArtistico.Text.Trim());

                        int existe = Convert.ToInt32(verificarCmd.ExecuteScalar());

                        if (existe > 0)
                        {
                            MessageBox.Show("Artista já registado!");
                            return;
                        }
                    }

                    string query = "INSERT INTO artista (nome_artistico, caminho_foto, fk_categoria) VALUES (@nome, @foto, @categoria)";

                    using (MySqlCommand cmd = new MySqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@nome", txtNomeArtistico.Text.Trim());
                        cmd.Parameters.AddWithValue("@foto", caminhoImagemSelecionada);
                        cmd.Parameters.AddWithValue("@categoria", cmbCategoria.SelectedValue);

                        cmd.ExecuteNonQuery();
                    }
                }

                MessageBox.Show("Inserido com sucesso!");

                AtualizarGrelha();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        }

        private void btnEditar_Click(object sender, EventArgs e)
        {
            if (dgvArtistas.CurrentRow == null) return;
            if (!ValidarCampos()) return;
            try
            {
                int id = Convert.ToInt32(dgvArtistas.CurrentRow.Cells[0].Value);
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();
                    string query = "UPDATE artista SET nome_artistico=@nome, caminho_foto=@foto, fk_categoria=@categoria WHERE id_artista=@id";
                    using (MySqlCommand cmd = new MySqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@nome", txtNomeArtistico.Text.Trim());
                        cmd.Parameters.AddWithValue("@foto", caminhoImagemSelecionada);
                        cmd.Parameters.AddWithValue("@categoria", cmbCategoria.SelectedValue);
                        cmd.Parameters.AddWithValue("@id", id);
                        cmd.ExecuteNonQuery();
                    }
                }
                MessageBox.Show("Atualizado com sucesso!");
                AtualizarGrelha();
            }
            catch (Exception ex) { MessageBox.Show("Erro: " + ex.Message); }
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            if (dgvArtistas.CurrentRow == null) return;
            var res = MessageBox.Show("Deseja eliminar?", "Confirmação", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (res == DialogResult.No) return;
            try
            {
                int id = Convert.ToInt32(dgvArtistas.CurrentRow.Cells[0].Value);
                using (MySqlConnection conn = new MySqlConnection(stringConexao))
                {
                    conn.Open();
                    string query = "DELETE FROM artista WHERE id_artista = @id";
                    using (MySqlCommand cmd = new MySqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("@id", id);
                        cmd.ExecuteNonQuery();
                    }
                }
                AtualizarGrelha();
            }
            catch (Exception ex) { MessageBox.Show("Erro: " + ex.Message); }
        }

        private void dgvArtistas_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow linha = dgvArtistas.Rows[e.RowIndex];

                txtNomeArtistico.Text = linha.Cells[1].Value?.ToString() ?? "";

                cmbCategoria.Text = linha.Cells[2].Value?.ToString() ?? "";

                caminhoImagemSelecionada = linha.Cells[3].Value?.ToString() ?? "";

                CarregarImagem(caminhoImagemSelecionada);
            }
        }

        private bool ValidarCampos()
        {
            if (string.IsNullOrWhiteSpace(txtNomeArtistico.Text) || cmbCategoria.SelectedIndex == -1)
            {
                MessageBox.Show("Preencha todos os campos!", "Aviso", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return false;
            }
            return true;
        }

        private void LimparFormulario()
        {
            txtNomeArtistico.Clear();
            cmbCategoria.SelectedIndex = -1;
            picFotografia.Image = null;
            caminhoImagemSelecionada = "";
        }

        private void label1_Click(object sender, EventArgs e) { }
        private void label3_Click(object sender, EventArgs e) { }
        private void pictureBox3_Click(object sender, EventArgs e) { }
        private void dataGridView1_AutoSizeColumnsModeChanged(object sender, DataGridViewAutoSizeColumnsModeEventArgs e) { }

        private void btnInserir_Click_1(object sender, EventArgs e)
        {

        }

        private void picFotografia_Click(object sender, EventArgs e)
        {

        }
    }
}


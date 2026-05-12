using System;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using FontAwesome.Sharp;

namespace ex_01_windows_forms_app01
{
    public partial class Form1 : Form
    {
        private string acaoSelecionada = "";

        public Form1()
        {
            InitializeComponent();

            ConfigurarTela();
            ConfigurarBotoes();
            ConfigurarListView();
        }

        private void ConfigurarTela()
        {
            this.BackColor = Color.White;
            this.StartPosition = FormStartPosition.CenterScreen;

            grpBtns.ForeColor = Color.FromArgb(0, 70, 160);
            gbxInformacoes.ForeColor = Color.FromArgb(0, 70, 160);
            grpBxResultados.ForeColor = Color.FromArgb(0, 70, 160);

            lblRaiz.ForeColor = Color.Black;
            lblDestino.ForeColor = Color.Black;

            lblRaiz.Font = new Font("Segoe UI", 10, FontStyle.Bold);
            lblDestino.Font = new Font("Segoe UI", 10, FontStyle.Bold);
        }

        private void ConfigurarBotoes()
        {
            EstilizarBotaoPrincipal(
                btnIconMover,
                Color.FromArgb(230, 243, 255),
                Color.FromArgb(0, 102, 204)
            );

            EstilizarBotaoPrincipal(
                btnIconCopiar,
                Color.FromArgb(235, 250, 235),
                Color.FromArgb(0, 130, 0)
            );

            EstilizarBotaoPrincipal(
                btnIconListarArq,
                Color.FromArgb(255, 248, 225),
                Color.FromArgb(240, 160, 0)
            );

            EstilizarBotaoPrincipal(
                btnIconExcluir,
                Color.FromArgb(255, 235, 235),
                Color.FromArgb(180, 0, 0)
            );

            EstilizarBotaoPequeno(
                btnIconlocalizarPastaRaiz,
                Color.FromArgb(0, 120, 215)
            );

            EstilizarBotaoPequeno(
                btnIconlocalizarPastaDestino,
                Color.FromArgb(0, 140, 0)
            );

            btnIconIniciar.BackColor = Color.FromArgb(0, 120, 215);
            btnIconIniciar.ForeColor = Color.White;
            btnIconIniciar.IconColor = Color.White;
            btnIconIniciar.FlatStyle = FlatStyle.Flat;
            btnIconIniciar.FlatAppearance.BorderSize = 0;
            btnIconIniciar.Font = new Font("Segoe UI", 11, FontStyle.Bold);
            btnIconIniciar.Cursor = Cursors.Hand;
        }

        private void EstilizarBotaoPrincipal(FontAwesome.Sharp.IconButton botao, Color corFundo, Color corTexto)
        {
            botao.BackColor = corFundo;
            botao.ForeColor = corTexto;
            botao.IconColor = corTexto;
            botao.FlatStyle = FlatStyle.Flat;
            botao.FlatAppearance.BorderColor = corTexto;
            botao.FlatAppearance.BorderSize = 1;
            botao.Font = new Font("Segoe UI", 10, FontStyle.Bold);
            botao.Cursor = Cursors.Hand;
        }

        private void EstilizarBotaoPequeno(FontAwesome.Sharp.IconButton botao, Color corFundo)
        {
            botao.BackColor = corFundo;
            botao.ForeColor = Color.White;
            botao.IconColor = Color.White;
            botao.FlatStyle = FlatStyle.Flat;
            botao.FlatAppearance.BorderSize = 0;
            botao.Cursor = Cursors.Hand;
        }

        private void ConfigurarListView()
        {
            lstvResultados.View = View.Details;
            lstvResultados.FullRowSelect = true;
            lstvResultados.GridLines = true;
            lstvResultados.Font = new Font("Segoe UI", 10);
            lstvResultados.BackColor = Color.White;
            lstvResultados.ForeColor = Color.Black;

            lstvResultados.Columns.Clear();
            lstvResultados.Columns.Add("Nome", 250);
            lstvResultados.Columns.Add("Tipo", 100);
            lstvResultados.Columns.Add("Tamanho", 100);
        }

        private void btnIconlocalizarPastaRaiz_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog folder = new FolderBrowserDialog())
            {
                if (folder.ShowDialog() == DialogResult.OK)
                {
                    txtCaminhoRaiz.Text = folder.SelectedPath;
                }
            }
        }

        private void btnIconlocalizarPastaDestino_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog folder = new FolderBrowserDialog())
            {
                if (folder.ShowDialog() == DialogResult.OK)
                {
                    txtCaminhoDestino.Text = folder.SelectedPath;
                }
            }
        }

        private void btnIconListarArq_Click(object sender, EventArgs e)
        {
            string caminhoRaiz = txtCaminhoRaiz.Text;

            if (string.IsNullOrWhiteSpace(caminhoRaiz))
            {
                MessageBox.Show("Informe o diretório raiz.");
                return;
            }

            if (!Directory.Exists(caminhoRaiz))
            {
                MessageBox.Show("O diretório raiz não existe.");
                return;
            }

            lstvResultados.Items.Clear();

            string[] arquivos = Directory.GetFiles(caminhoRaiz);

            foreach (string arquivo in arquivos)
            {
                FileInfo info = new FileInfo(arquivo);

                ListViewItem item = new ListViewItem(info.Name);
                item.SubItems.Add(info.Extension);
                item.SubItems.Add((info.Length / 1024) + " KB");

                lstvResultados.Items.Add(item);
            }

            MessageBox.Show("Arquivos listados com sucesso.");
        }

        private void btnIconMover_Click(object sender, EventArgs e)
        {
            acaoSelecionada = "mover";

            btnIconMover.BackColor = Color.FromArgb(180, 220, 255);
            btnIconCopiar.BackColor = Color.FromArgb(235, 250, 235);

            MessageBox.Show("Modo mover selecionado.");
        }

        private void btnIconCopiar_Click(object sender, EventArgs e)
        {
            acaoSelecionada = "copiar";

            btnIconCopiar.BackColor = Color.FromArgb(180, 255, 180);
            btnIconMover.BackColor = Color.FromArgb(230, 243, 255);

            MessageBox.Show("Modo copiar selecionado.");
        }

    }
}